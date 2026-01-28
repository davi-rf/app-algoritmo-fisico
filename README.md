<div align="center">
  <h1>APP Algoritmo Físico</h1>

<<<<<<< HEAD
  <img src="https://img.shields.io/badge/react_native-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB">
  <img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi">
</div>
=======
![React Native](https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Expo](https://img.shields.io/badge/Expo-000020?style=for-the-badge&logo=expo&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=000)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![OpenCV](https://img.shields.io/badge/OpenCV-27338E?style=for-the-badge&logo=opencv&logoColor=white)
![EasyOCR](https://img.shields.io/badge/EasyOCR-000000?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-7B2CBF?style=for-the-badge)
![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
>>>>>>> e2e3577aa9e3fe9eadd295f9d891b98636200582

<p align="right">
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
