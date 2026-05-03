"""from google import genai

cliente = genai.Client(api_key="AIzaSyARZsER14stTHweYD4ynlRPSRBeNEGeKFs")

chat = cliente.chats.create(model="gemini-3.1-flash-lite-preview")

print("¿En qué puedo ayudarte?")
while True:
    consulta = input("> ")
    print("")
    if consulta == "salir":
        break
    respuesta = chat.send_message_stream(consulta)
    for stream in respuesta:
        print(stream.text)

print("¡Hasta luego!")

"""

import numpy as np
import pandas as pd
from gemini_chat import GeminiChat

# Configuracion splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Se inicializa la clase GeminiChat
GeminiChat = GeminiChat()

print("¿En qué puedo ayudarte?")
consulta = input("> ")
print("")

print(GeminiChat.consultar_llm(consulta))
