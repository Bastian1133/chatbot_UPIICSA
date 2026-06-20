from pathlib import Path
import sys

# Para que Python encuentre embedder.py en la carpeta raíz
sys.path.append(str(Path(__file__).parent.parent))

from embedder import Embedder
from .supabase_client import get_supabase_client

class Retriever:
    
    def __init__(self):
        self.supabase = get_supabase_client()
        self.embedder = Embedder()
    
    def obtener_contexto(self, consulta: str) -> list:
        vector_consulta = self.embedder.vectorizar_consulta(consulta)
        
        response = self.supabase.rpc("buscar_chunks", {
            "query_embedding": vector_consulta
        }).execute()
        
        return response.data
    
    def obtener_contexto_concatenado(self, consulta: str) -> str:
        resultados = self.obtener_contexto(consulta)
        
        if not resultados:
            return ""
        
        for r in resultados:
            print(f"  Similitud: {r['similitud']:.3f} — Hijo: {r['texto_embedding']}")
        
        contextos = [r["contexto_completo"] for r in resultados]
        return "\n\n---\n\n".join(contextos)