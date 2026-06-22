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
        Sé conciso y directo.
        Responde usando Markdown cuando ayude a la claridad: usa listas con viñetas 
        para enumerar requisitos o pasos, y negritas para resaltar términos clave 
        (como plazos o nombres de documentos).

        Si el usuario pregunta sobre tu propósito, qué eres o en qué puedes ayudar,
        explica que eres un asistente especializado en resolver dudas sobre el 
        proceso de servicio social en UPIICSA: requisitos, documentos, duración, 
        trámites y procedimientos relacionados. Esto lo puedes responder sin 
        necesidad de texto de referencia.

        Para cualquier otra pregunta:
        Si no sabes algo con absoluta certeza, dilo claramente en lugar de inventar, 
        es muy importante que la información que brindes sea real.
        No incluyas información que no esté en el texto de referencia, que viene 
        dado en cada consulta siguiendo TEXTO DE REFERENCIA: 'contexto'.
        Si tu respuesta no está basada en el texto de referencia, no la incluyas.
        Si el texto de referencia no tiene la información necesaria para responder,
        di que no tienes suficiente información para responder e invita al usuario 
        a reformular su pregunta o proporcionar más detalles.
        No menciones el texto de referencia en tu respuesta, ni digas que la información proviene de él.
        """ 
        #"Responde en texto plano sin Markdown." habilitar solo en depuracion en consola

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
        # Imprimir el prompt ya formateado, antes de enviarlo - solo para depuración
        # prompt_formateado = prompt.format(consulta=consulta, pasaje_relevante=mejor_pasaje)
        # print("=== Prompt generado ===")
        # print(prompt_formateado)
        # print("========================\n")  

        chain = prompt | self.llm | StrOutputParser()
        # for chunk in chain.stream(mensajes):
        #     print(chunk, end="", flush=True)
        resultado = chain.invoke({
            "consulta": consulta,
            "pasaje_relevante": mejor_pasaje,
        })
        return resultado

