import os
import customtkinter as ctk
from dotenv import load_dotenv
from openai import OpenAI
import httpx, certifi 

# carrega a chave da API
load_dotenv(dotenv_path=".env")
api_key = os.getenv("OPENAI_API_KEY")

# print message para verificar se a chave_api foi devidamente carregada.
print("API Key encontrada:", api_key[:8] + "..." if api_key else "NENHUMA")
client = OpenAI(api_key=api_key)

# cliente ignorando SSL (teste local)
httpx_client = httpx.Client(verify=False)  
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), http_client=httpx_client)

# configura a janela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Chatbot - ChatGPT")
root.geometry("600x500")

# caixa de texto para conversa
chat_box = ctk.CTkTextbox(root, width=580, height=350, wrap="word")
chat_box.pack(pady=10)

# placeholder de entrada
entry = ctk.CTkEntry(root, width=480, placeholder_text="Digite sua mensagem...")
entry.pack(side="left", padx=10, pady=10)

def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    
    # pergunta do user
    chat_box.insert("end", f"Você: {user_input}\n")
    entry.delete(0, "end")

    # resposta da API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}]
    )

    answer = response.choices[0].message.content
    chat_box.insert("end", f"Chatbot: {answer}\n\n")
    chat_box.see("end")

# botão de enviar
send_btn = ctk.CTkButton(root, text="Enviar", command=send_message)
send_btn.pack(side="right", padx=10, pady=10)

root.mainloop()
