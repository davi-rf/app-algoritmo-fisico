# APP Algoritmo Físico

![React Native](https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Expo](https://img.shields.io/badge/Expo-000020?style=for-the-badge&logo=expo&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=000)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-27338E?style=for-the-badge&logo=opencv&logoColor=white)
![EasyOCR](https://img.shields.io/badge/EasyOCR-000000?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-7B2CBF?style=for-the-badge)
![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Aplicativo que escaneia pseudocódigos em blocos (algoritmos físicos) a partir de imagens e retorna o **código equivalente em Python** junto com a **solução (saída da execução)**.

## Funcionalidades

- Captura de imagem pela câmera ou galeria
- Reconhecimento de texto (OCR)
- Interpretação do pseudocódigo usando IA
- Conversão automática para Python
- Execução do código gerado
- Retorno do código e da solução

## Estrutura do Projeto

### Front-end

- **React Native**
- **Expo**
- **JavaScript**

Interface onde o usuário seleciona ou captura a imagem (Android/iOS) e envia para o back-end.

### Back-end

- **Python**
- **EasyOCR**
- **OpenCV**
- **Ollama**

Fluxo do back-end:

1. Recebe a imagem do front-end
2. Extrai o texto usando OCR
3. Usa o **Ollama** para transformar o texto reconhecido em código Python
4. Executa o código
5. Retorna:
   - Código Python gerado
   - Solução (resultado da execução)
