import tkinter as tk
from tkinter import filedialog
import cv2
import easyocr


def select_image():
    try:
        root = tk.Tk()
        root.withdraw()
        caminho = filedialog.askopenfilename(
            title='Selecione uma imagem',
            filetypes=[('Imagens', '*.jpg *.jpeg *.png *.bmp *.tiff *.tif *.webp *.gif')]
        )
        if caminho:
            return caminho
    except Exception:
        pass
    return input('Digite o caminho completo da imagem: ').strip()


def normalize_image(caminho):
    img = cv2.imread(caminho)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(2.0, (8, 8))
    gray = clahe.apply(gray)

    out = 'imagem_normalizada.png'
    cv2.imwrite(out, gray)
    return out


def gerar_texto(results, y_threshold=25):
    linhas = []

    for bbox, txt, _ in results:
        y = sum(p[1] for p in bbox) / 4
        for linha in linhas:
            if abs(linha['y'] - y) < y_threshold:
                linha['itens'].append((bbox, txt))
                break
        else:
            linhas.append({'y': y, 'itens': [(bbox, txt)]})

    linhas.sort(key=lambda l: l['y'])

    texto_final = []
    for linha in linhas:
        linha['itens'].sort(key=lambda t: t[0][0][0])
        texto_final.append(' '.join(t[1] for t in linha['itens']))

    return texto_final


def read_img(caminho):
    reader = easyocr.Reader(['pt'], gpu=False)
    results = reader.readtext(
        caminho,
        detail=1,
        contrast_ths=0.05,
        adjust_contrast=0.7,
        decoder='greedy'
    )
    return gerar_texto(results)


caminho = select_image()

if caminho:
    img = normalize_image(caminho)
    blocos = read_img(img)

    with open('final_txt.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(blocos))
else: print('Nenhuma imagem selecionada.')