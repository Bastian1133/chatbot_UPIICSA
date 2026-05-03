import os
# Configuracion LLM - Gemini
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.output_parsers import StrOutputParser

class GeminiChat:
    def __init__(self):
        GEMINI_API_KEY = "AIzaSyARZsER14stTHweYD4ynlRPSRBeNEGeKFs"
        os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

        self.llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")

    def consultar_llm(self, consulta):
        chain = self.llm | StrOutputParser()
        respuesta = chain.invoke(consulta)
        return respuesta

