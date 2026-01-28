<h1 align='center'>APP Algoritmo Físico</h1>

<p align='center'>
  <img src='https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB'>
  <img src='https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=000'>
  <img src='https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white'>
</p>

<p align='right'>
Aplicativo que escaneia pseudocódigos em blocos (algoritmos físicos) a partir de imagens e retorna o código equivalente em <b>Python</b> junto com a <b>saída da execução</b>.
</p>

## Funcionalidades

- Captura de imagem pela câmera ou galeria
- Reconhecimento de texto (OCR)
- Interpretação do pseudocódigo usando IA
- Conversão automática para Python
- Execução do código gerado
- Retorno do código e da solução

## Estrutura do Projeto

### Front-end

- React Native
- Expo
- JavaScript

Responsável pela interface, captura/seleção da imagem e envio ao back-end.

### Back-end

- Python
- EasyOCR
- OpenCV
- Ollama

Fluxo:

1. Recebe a imagem do front-end
2. Extrai o texto via OCR
3. Converte o pseudocódigo em Python usando IA
4. Executa o código gerado
5. Retorna:
   - Código Python
   - Resultado da execução
