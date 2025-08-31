import os
import json
import customtkinter as ctk
from dotenv import load_dotenv
from openai import OpenAI
import httpx, certifi
import speech_recognition as sr
import pyttsx3
from tkinter import filedialog


# carrega a chave da API
load_dotenv(dotenv_path=".env")
api_key = os.getenv("OPENAI_API_KEY")

# print message para verificar se a chave_api foi devidamente carregada.
print("API Key encontrada:", api_key[:8] + "..." if api_key else "NENHUMA")
client = OpenAI(api_key=api_key)

# cliente ignorando SSL (teste local)
httpx_client = httpx.Client(verify=False)  
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), http_client=httpx_client)

# histórico de conversa
messages = [{"role": "system", "content": "Você é um assistente útil."}]

# motor de voz (TTS)
engine = pyttsx3.init()

# ========= INTERFACE =========
ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("CHATBOT - API")
root.geometry("800x650")

try:
    montserrat_font = ctk.CTkFont(family="Montserrat", size=13)
except:
    montserrat_font = ctk.CTkFont(family="Arial", size=13)

try:
    root.iconbitmap("assets/favicon.ico")
except:
    pass

frame_chat = ctk.CTkFrame(root, corner_radius=10)
frame_chat.pack(fill="both", expand=True, padx=10, pady=10)

chat_box = ctk.CTkTextbox(frame_chat, wrap="word", width=760, height=450,
                          font=montserrat_font)
chat_box.pack(side="left", fill="both", expand=True)

scrollbar = ctk.CTkScrollbar(frame_chat, command=chat_box.yview)
scrollbar.pack(side="right", fill="y")
chat_box.configure(yscrollcommand=scrollbar.set)

entry = ctk.CTkEntry(root, width=550, placeholder_text="Digite sua mensagem...",
                     font=montserrat_font)
entry.pack(side="left", padx=10, pady=10)

model_var = ctk.StringVar(value="gpt-4o-mini")
model_menu = ctk.CTkOptionMenu(root, variable=model_var,
                               values=["gpt-4o-mini", "gpt-4o", "gpt-4.1"],
                               font=montserrat_font)
model_menu.pack(side="left", padx=5)

status_label = ctk.CTkLabel(root, text="✅ Conectado", text_color="green",
                            font=montserrat_font)
status_label.pack(pady=3)


# ========= FUNÇÕES =========
def send_message(event=None):
    user_input = entry.get()
    if not user_input.strip():
        return
    
    chat_box.insert("end", f"🧑 Você: {user_input}\n", "user")
    entry.delete(0, "end")

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model=model_var.get(),
            messages=messages
        )
        answer = response.choices[0].message.content
        messages.append({"role": "assistant", "content": answer})

        chat_box.insert("end", f"🤖 Chatbot: {answer}\n\n", "bot")
        chat_box.see("end")

        engine.say(answer)
        engine.runAndWait()

    except Exception as e:
        chat_box.insert("end", f"[ERRO] {e}\n\n")


def clear_chat(event=None):
    chat_box.delete("1.0", "end")
    global messages
    messages = [{"role": "system", "content": "Você é um assistente útil."}]


def export_chat():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Arquivo TXT", "*.txt"), ("Arquivo JSON", "*.json")])
    if not file_path:
        return
    
    if file_path.endswith(".json"):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(messages, f, indent=4, ensure_ascii=False)
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            for msg in messages:
                f.write(f"{msg['role']}: {msg['content']}\n")


def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.configure(text="🎤 Ouvindo...", text_color="orange")
        root.update()
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="pt-BR")
            entry.delete(0, "end")
            entry.insert(0, text)
            send_message()
        except sr.UnknownValueError:
            chat_box.insert("end", "❌ Não entendi o que foi dito.\n")
        except sr.RequestError as e:
            chat_box.insert("end", f"[ERRO microfone] {e}\n")
        finally:
            status_label.configure(text="✅ Conectado", text_color="green")


def toggle_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")


# ========= BOTÕES =========
frame_buttons = ctk.CTkFrame(root, fg_color="transparent")
frame_buttons.pack(pady=8)

send_btn = ctk.CTkButton(frame_buttons, text="Enviar", command=send_message,
                         width=100, corner_radius=15, font=montserrat_font)
send_btn.grid(row=0, column=0, padx=5)

clear_btn = ctk.CTkButton(frame_buttons, text="Limpar", command=clear_chat,
                          width=100, corner_radius=15, font=montserrat_font)
clear_btn.grid(row=0, column=1, padx=5)

export_btn = ctk.CTkButton(frame_buttons, text="Exportar", command=export_chat,
                           width=100, corner_radius=15, font=montserrat_font)
export_btn.grid(row=0, column=2, padx=5)

voice_btn = ctk.CTkButton(frame_buttons, text="🎤 Voz", command=voice_input,
                          width=100, corner_radius=15, font=montserrat_font)
voice_btn.grid(row=0, column=3, padx=5)

theme_btn = ctk.CTkButton(frame_buttons, text="🌙 Tema", command=toggle_theme,
                          width=100, corner_radius=15, font=montserrat_font)
theme_btn.grid(row=0, column=4, padx=5)


# ========= ESTILOS =========
chat_box.tag_config("user", foreground="#06b6d4")  
chat_box.tag_config("bot", foreground="#22c55e")   

# ========= ATALHOS =========
root.bind("<Return>", send_message)
root.bind("<Control-l>", clear_chat)

root.mainloop()