from google import genai

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