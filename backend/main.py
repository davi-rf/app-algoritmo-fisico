import os
import cv2
import easyocr
import tkinter as tk
from tkinter import filedialog


def selecionar_imagem():
    try:
        root = tk.Tk()
        root.withdraw()
        root.update()
        caminho = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.tiff *.tif *.webp *.gif")]
        )
        root.destroy()
        if caminho:
            return caminho
        else:
            print("⚠️ Nenhuma imagem selecionada.")
    except Exception:
        pass

    return input("Digite o caminho completo da imagem: ").strip()


def normalizar_imagem(caminho_imagem):
    img = cv2.imread(caminho_imagem)

    # Escala de cinza (menos ruído pro OCR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Normalização leve de contraste
    norm = cv2.normalize(
        gray, None,
        alpha=0, beta=255,
        norm_type=cv2.NORM_MINMAX
    )

    caminho_tmp = "imagem_normalizada.png"
    cv2.imwrite(caminho_tmp, norm)
    return caminho_tmp


def extrair_texto_com_easyocr(caminho_imagem):
    caminho_proc = normalizar_imagem(caminho_imagem)

    reader = easyocr.Reader(['pt'])
    results = reader.readtext(caminho_proc, detail=1)

    # Ordena por posição (linha e coluna)
    results.sort(key=lambda x: (x[0][0][1], x[0][0][0]))

    final_output_lines = []
    y_threshold = 20
    current_line = []

    for (bbox, text, conf) in results:
        y_center = bbox[0][1]

        if not current_line:
            current_line.append((bbox, text, conf))
        else:
            last_y_center = current_line[-1][0][0][1]

            if abs(y_center - last_y_center) < y_threshold:
                current_line.append((bbox, text, conf))
            else:
                final_output_lines.append(" ".join(t[1] for t in current_line))
                current_line = [(bbox, text, conf)]

    if current_line:
        final_output_lines.append(" ".join(t[1] for t in current_line))

    texto_final = "\n".join(final_output_lines)

    nome_base = os.path.splitext(os.path.basename(caminho_imagem))[0]
    caminho_saida_txt = f"{nome_base}_easyocr.txt"

    with open(caminho_saida_txt, "w", encoding="utf-8") as f:
        f.write(texto_final)

    print(f"✅ Texto extraído salvo em: {caminho_saida_txt}")
    return texto_final, caminho_saida_txt


def gerar_codigo(texto):
    return texto


# ===== EXECUÇÃO =====
caminho = selecionar_imagem()

if caminho:
    texto_extraido, caminho_txt = extrair_texto_com_easyocr(caminho)
    codigo_py = gerar_codigo(texto_extraido)

    if codigo_py.strip():
        nome_base = os.path.splitext(os.path.basename(caminho))[0]
        caminho_py = f"{nome_base}_gerado.py"

        with open(caminho_py, "w", encoding="utf-8") as f:
            f.write(codigo_py)

        print(f"✅ Código Python salvo em: {caminho_py}")
    else:
        print("⚠️ Nenhum código foi gerado.")
