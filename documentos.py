from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter # Configuracion splitter
import pandas as pd
import textwrap

class Documentos:
    def __init__(self):

        info_1 = textwrap.dedent("""
            ¿Qué requiero para iniciar mi servicio social?
            - Ser alumno inscrito o egresado.
            - Constancia de créditos vigente que avale un mínimo del 70% de avance.
            - Constancia de servicio médico vigente (IMSS, ISSSTE o privado).
            - CURP, no mayor a un mes de expedición.
            - Contar con correo electrónico vigente (personal o institucional).
            IMPORTANTE: únicamente podrás realizarlo dentro del IPN.
        """).strip()

        doc_1 = Document(textwrap.dedent(info_1).strip(), metadata={"titulo": "Requisitos servicio social"})
        self.docs = [doc_1]


    def crear_dataframe(self):
        # Dividiendo los documentos en fragmentos más pequeños (chunks) para que el modelo pueda procesarlos mejor
        text_splitter = RecursiveCharacterTextSplitter(
                  chunk_size=80,
                  chunk_overlap=50, # Esto significa que cada fragmento tendrá un solapamiento de 100 caracteres con el siguiente fragmento para mantener el contexto.
                  separators=[
                    "\n\n",   # párrafos primero
                    "\n",     # luego líneas
                    ". ",     # luego oraciones
                    ", ",
                    " ",
                    ""
                ] 
        )

        splits = text_splitter.split_documents(self.docs)

        # Almacenando los chunks en un DataFrame
        chunks = []
        for split in splits:
            chunks.append(split.page_content)

        df = pd.DataFrame(chunks, columns = ['Text']) # Creamos un dataFrame con los textos
        return df
        