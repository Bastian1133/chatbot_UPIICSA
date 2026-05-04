import os
# Configuracion LLM - Gemini
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.output_parsers import StrOutputParser

from langchain_core.messages import SystemMessage, HumanMessage

class GeminiChat:
    def __init__(self):
        GEMINI_API_KEY = "AIzaSyARZsER14stTHweYD4ynlRPSRBeNEGeKFs"
        os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.1-flash-lite-preview",
            temperature=0.2, # Ajusta la temperatura para controlar la creatividad de las respuestas
            max_tokens=2048 # Ajusta el número máximo de tokens en la respuesta
        )
        self.system_prompt = """
        Eres un asistente virtual de UPIICSA especializado en servicio social.
        Responde en texto plano sin Markdown.
        Sé conciso y directo.
        Si no sabes algo, dilo claramente en lugar de inventar.
        """ 

    def consultar_llm(self, consulta):
        mensajes = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=consulta)
        ]
        chain = self.llm | StrOutputParser()
        
        for chunk in chain.stream(mensajes):
            print(chunk, end="", flush=True)
        print("")  # salto de línea al terminar

