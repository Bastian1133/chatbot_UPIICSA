from gemini_chat import GeminiChat
from documentos import Documentos
from embedding import calcular_embeddings
from embedding import encontrar_mejor_pasaje

# Se inicializa la clase GeminiChat
GeminiChat = GeminiChat()
Documentos = Documentos()

df = Documentos.crear_dataframe()
calcular_embeddings(df)

print("¿En qué puedo ayudarte?")

while True:
    consulta = input("> ")
    print("")
    mejor_pasaje = encontrar_mejor_pasaje(consulta, df)
    if consulta == "salir":
        print("¡Hasta luego!")
        break
    GeminiChat.consultar_llm(consulta, mejor_pasaje)
    print("")
