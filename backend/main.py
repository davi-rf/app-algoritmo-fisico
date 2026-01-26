#Obs.: Comentários feitos completamente a mão

#Bibliotecas importadas
import tkinter as tk
from tkinter import filedialog
import cv2
import easyocr


#Função para seleção de imagem por meio do gerenciador de arquivos
def select_image():
    try:
        #Inicializa uma janela root do Tkinter e a esconde
        root = tk.Tk()
        root.title("root")
        root.withdraw()
        root.update()

        #Abre o gerenciador de arquivos, permitindo que o usuário selecione apenas imagens dos tipos citados
        caminho = filedialog.askopenfilename(
            title = "Selecione uma imagem", 
            filetypes = [("Imagens", "*.jpg *.jpeg *.png *.bmp *.tiff *.tif *.webp *.gif")]
        )

        #Se houver um caminho dito, ele será retornado
        if caminho:
            return caminho
        else:
            print("Nada foi selecionado")

    except Exception as e:
        pass
    
    #A função chega aqui se nenhum caminho valido for selecionado pelo gerenciador de arquivos
    return input("Digite o caminho completo da imagem: ").strip()

#Função que melhora a imagem para que o OCR seja feito mais facilmente
def normalize_image(caminho):
    #Transforma a imagem em um conjunto de dados que pode ser analisado computadoramente
    img = cv2.imread(caminho)

    #Converte a imagem para tons de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Cria um objeto que tem a funçã de aumentar o contraste em imagens
    #cliplimit: limita o tanto de contraste
    #tileGridSize: divide a imagem em blocos 8x8, ajustando cada um separadamente
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    
    #Aplica a mudança na imagem anteriormente convertida para cinza
    gray = clahe.apply(gray)
    
    #Salva a imagem normalizada na pasta do projeto e retorna seu caminho
    caminho_tmp = "imagem_normalizada.png"
    cv2.imwrite(caminho_tmp, gray)
    return caminho_tmp


#Função que monta as linhas lidas com base nos resultados da leitura
#y_threshold=25: limita o quanto que uma palavra pode descer pra ser ou nao considerada da mesma linha que outra
def agrupar_em_blocos(results, y_threshold=25):

    #Cada linha será salva como um item da lista
    linhas = []

    for bbox, txt, _ in results:

        #Calcula o centro do eixo vertical de uma palavra usando o seus pontos do salvos no bbox
        y_center = sum(p[1] for p in bbox) / 4

        #Identifica se uma palavra ja foi ou não colocada em uma linha
        colocado = False

        #Percorre a lista procurando onde encaixar a palavra atual
        for linha in linhas:
            if abs(linha["y"] - y_center) < y_threshold:
                linha["textos"].append((bbox, txt))
                colocado = True
                break
        
        #Caso nao encaixe em nenhuma linha por causa da diferença de altura muito grande. Cria uma nova linha
        if not colocado:
            linhas.append({
                "y": y_center,
                "textos": [(bbox, txt)]
            })

    #Retorna todas as linhas alocadas
    return linhas

#Função que monta o texto de maneira legível
def montar_texto_blocos(linhas):

    #Organiza de cima para baixo as linhas salvas no dicionario de linhas
    linhas.sort(key=lambda l: l["y"])

    #Lista que armazena cada linha como um texto legível
    blocos = []

    #Percorre a lista de linhas
    for linha in linhas:

        #Salva o texto da linha
        textos = linha["textos"]
        #Organiza as palavras pelo bbox. Agora utilizando o eixo x
        textos.sort(key=lambda t: t[0][0][0])
        #Junta todas as palavras em uma unica linha separadas por espaço
        frase = " ".join(t[1] for t in textos)

        blocos.append(frase)

    return blocos

#Função que lê a imagem e transforma em texto
def read_img(caminho):
    
    #Cria um objeto leitor da biblioteca easyocr
    #gpu=False: Força a utilização da CPU. Deixando mais lento, porém mais preciso
    reader = easyocr.Reader(["pt"], gpu=False)
    #Cria uma lista com 3 informações distintas sobre cada coisa lida (bbox, txt e confidence)
    #bbox é um valor que armazena as posiçoes dos cantos da caixa formada ao redor de cada trecho identificado
    results = reader.readtext(caminho, detail=1, contrast_ths=0.05, adjust_contrast=0.7, decoder="greedy")   
    
    linhas = agrupar_em_blocos(results)
    blocos = montar_texto_blocos(linhas)

    #for bloco in blocos:
    #    print(f"{bloco}")
    return blocos

#Seleciona imagem chamando a função para tal
caminho = select_image()

if caminho:
    
    #Normaliza a imagem
    img = normalize_image(caminho)
    blocos = read_img(img)

    #Salva o texto em um arquivo .txt
    with open("final_txt.txt", "w", encoding="utf-8") as f:
        for bloco in blocos:
            f.write(bloco+"\n")
