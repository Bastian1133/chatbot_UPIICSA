from pathlib import Path
import sys

# Para que Python encuentre embedder.py en la carpeta raíz
sys.path.append(str(Path(__file__).parent.parent))

from chunker import Chunker
from extractor_pdf import Extractor
from embedder import Embedder
from database.insertar_supabase import InsersorSupabase

# 1. Extraer texto de PDFs
ExtractorPDF = Extractor()
diccionario = ExtractorPDF.extraer_desde_carpeta(str(Path(__file__).parent.parent / "documentos"))

# 2. Generar chunks padre-hijo
chunker = Chunker()
bloques = chunker.generar_desde_diccionario(diccionario)

# 3. Vectorizar todos los hijos en un solo lote
print("\nVectorizando chunks hijos...")
embedder = Embedder()
textos_hijos = [
    hijo["texto_embedding"]
    for bloque in bloques
    for hijo in bloque["hijos"]
]
embeddings = embedder.vectorizar_lote(textos_hijos)
print(f"  {len(embeddings)} embeddings generados")

# 4. Insertar en Supabase
print("\nInsertando en Supabase...")
insersor = InsersorSupabase()
insersor.insertar_bloques(bloques, embeddings)

print("\n=== Indexación completada ===")