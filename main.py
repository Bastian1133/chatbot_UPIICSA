import numpy as np
from gemini_chat import GeminiChat
from documentos import Documentos

# Se inicializa la clase GeminiChat
GeminiChat = GeminiChat()
Documentos = Documentos()

df = Documentos.crear_dataframe()

print("¿En qué puedo ayudarte?")

while True:
    consulta = input("> ")
    print("")
    if consulta == "salir":
        print("¡Hasta luego!")
        break
    GeminiChat.consultar_llm(consulta)
    print("")
