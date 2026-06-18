from chunker import Chunker
from extractor_pdf import Extractor
from pathlib import Path

ExtractorPDF = Extractor()

diccionario = ExtractorPDF.extraer_desde_carpeta(str(Path(__file__).parent.parent / "documentos"))

chunker = Chunker()
chunks = chunker.generar_desde_diccionario(diccionario)

for bloque in chunks:
    print(f"\nPADRE: {bloque['padre']['fuente']}")
    print(f"Contexto: {bloque['padre']['contexto_completo']}")
    for i, hijo in enumerate(bloque['hijos']):
        print(f"  Hijo {i+1}: {hijo['texto_embedding']}")