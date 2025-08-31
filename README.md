# 🤖 Chatbot com Python + ChatGPT API + Interface Gráfica

Este projeto é um **Chatbot Inteligente** desenvolvido em **Python**, utilizando a **API do ChatGPT (OpenAI)** e interface gráfica moderna com **CustomTkinter**.  
A aplicação permite conversar em tempo real com a IA, alternar entre modelos, exportar conversas (.TXT ou .JSON), usar entrada de voz e até alternar entre **modo claro/escuro**.

---

## 🚀 Funcionalidades

- **Histórico de conversa** mantido durante a sessão
- **Interface gráfica moderna** com [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- **Modo claro/escuro dinâmico**
- **Entrada de voz** via `SpeechRecognition` + microfone
- **Respostas em voz (TTS)** com `pyttsx3`
- **Exportar conversas** para `.txt` ou `.json`
- **Seleção de modelo** (`gpt-4o-mini`, `gpt-4o`, `gpt-4.1`)
- **Atalhos de teclado**:  
  - **Enter** → enviar mensagem  
  - **Ctrl + L** → limpar conversa

---

## 📸 Demonstração
### Dark

<img width="1363" height="719" alt="image" src="https://github.com/user-attachments/assets/e4056b9e-ee25-4c11-b5b7-9d8cb7c30977" />

### White

<img width="1363" height="709" alt="image" src="https://github.com/user-attachments/assets/e27bc4b1-2458-46f7-ade5-7c35dfc64c7e" />

### Detalhes (MENU)

<img width="1356" height="134" alt="image" src="https://github.com/user-attachments/assets/a1cd2fd9-cab4-43ff-b85a-be4d034d8410" />

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.12+](https://www.python.org/)
- [OpenAI API](https://platform.openai.com/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [gTTS](https://pypi.org/project/gTTS/)
- [httpx](https://www.python-httpx.org/)
- [certifi](https://pypi.org/project/certifi/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/chatbot-chatgpt.git
cd chatbot-chatgpt
```

### 2. Crie e ATIVE um ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # Linux/Mac
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure sua chave da API
Crie um arquivo `.env` na raiz do projeto:
```ini
OPENAI_API_KEY=sk-proj-sua_chave_aqui
```
🔑 Importante: você precisa ter créditos ativos ou billing configurado em sua conta OpenAI.
Mais informações: Gerenciar API Keys
```
https://platform.openai.com/api-keys?utm_source=chatgpt.com
```

## ▶️ Execução
```bash
python main.py
```

## 📂 Estrutura do Projeto
```bash
CHATBOT-API/
│── main.py              # Código principal do chatbot
│── requirements.txt     # Dependências do projeto
│── assets/
    └── favicon.ico     # Ícone da janela
```

## 👤 Autor
Desenvolvido por [Christian Mendes]
- **LinkedIn:** https://www.linkedin.com/in/christian-mendes-b0073118b/

