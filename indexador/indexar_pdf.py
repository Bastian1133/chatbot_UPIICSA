from extractor_pdf import Extractor
from pathlib import Path

ExtractorPDF = Extractor()

diccionario = ExtractorPDF.extraer_desde_carpeta(str(Path(__file__).parent.parent / "documentos"))

for nombre_pdf, texto in diccionario.items():
    print(f"""Nombre: {nombre_pdf}
    Contenido: {texto}""".strip())