from dotenv import load_dotenv
import os
# Configuracion LLM - Gemini
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

class GeminiChat:
    def __init__(self):
        load_dotenv("keys.env") # Carga las variables de entorno desde el archivo keys.env

        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") # Obtiene la clave de API de Gemini desde las variables de entorno
        
        if not GEMINI_API_KEY:
            raise ValueError("Falta la API key de Gemini en el archivo keys.env")

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.1-flash-lite-preview",
            temperature=0.2, # Ajusta la temperatura para controlar la creatividad de las respuestas
            max_tokens=2048 # Ajusta el número máximo de tokens en la respuesta
        )
        self.system_prompt = """
        Eres un asistente virtual de UPIICSA especializado en servicio social.
        Responde en texto plano sin Markdown.
        Sé conciso y directo.
        Si no sabes algo con absoluta certeza, dilo claramente en lugar de inventar, es muy importante que la información que brindes sea real.
        No incluyas información que no esté en el texto de referencia, que viene dado en cada consulta siguiendo TEXTO DE REFERENCIA: 'contexto'
        Si tu respuesta no esta basada en el texto de referencia, no la incluyas. 
        Si el texto de referencia no tiene la información necesaria para responder, di que no tienes suficiente información para responder e invita al usuario a reformular su pregunta o proporcionar más detalles.
        """ 

    def consultar_llm(self, consulta, mejor_pasaje):
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", """
            
            PREGUNTA: '{consulta}'
            TEXTO DE REFERENCIA: '{pasaje_relevante}'

            RESPUESTA:
            """
            ),
        ])
        chain = prompt | self.llm | StrOutputParser()
        
        # for chunk in chain.stream(mensajes):
        #     print(chunk, end="", flush=True)
        resultado = chain.invoke({
            "consulta": consulta,
            "pasaje_relevante": mejor_pasaje,
        })
        print(resultado)
        print("")  # salto de línea al terminar

