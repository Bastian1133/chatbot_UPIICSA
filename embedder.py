import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv("keys.env") # Carga las variables de entorno desde el archivo keys.env

class Embedder:
    
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Falta GEMINI_API_KEY en el archivo keys.env")
        
        self.modelo = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-2",
            google_api_key=api_key,
            output_dimensionality=768
        )
    
    def vectorizar_consulta(self, texto: str) -> list:
        # Formato de tarea para búsquedas (asimétrico)
        texto_formateado = f"task: search result | query: {texto}"
        return self.modelo.embed_query(texto_formateado)
    
    def vectorizar_lote(self, textos: list, batch_size: int = 20) -> list:
        embeddings = []
        total = len(textos)
        for i in range(0, total, batch_size):
            lote = textos[i:i + batch_size]
            # Formato de tarea para documentos (asimétrico)
            lote_formateado = [f"title: none | text: {t}" for t in lote]
            resultados = [self.modelo.embed_query(t) for t in lote_formateado]
            embeddings.extend(resultados)
            print(f"  Vectorizados {min(i + batch_size, total)}/{total}...")
        return embeddings