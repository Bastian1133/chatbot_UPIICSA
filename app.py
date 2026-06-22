from fastapi import FastAPI
from pydantic import BaseModel
from gemini_chat import GeminiChat
from database.retriever import Retriever
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Chatbot Servicio Social UPIICSA",
    description="API para resolver dudas sobre el proceso de servicio social en la UPIICSA",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # para desarrollo; restringir en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

gemini_chat = GeminiChat()
retriever = Retriever()

class ConsultaRequest(BaseModel):
    pregunta: str

class ConsultaResponse(BaseModel):
    respuesta: str

@app.post("/consulta", response_model=ConsultaResponse)
def consultar(request: ConsultaRequest):
    contexto = retriever.obtener_contexto_concatenado(request.pregunta)
    texto_generado = gemini_chat.consultar_llm(request.pregunta, contexto)
    return ConsultaResponse(respuesta=texto_generado)