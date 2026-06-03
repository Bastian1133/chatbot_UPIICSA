from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter # Configuracion splitter
import pandas as pd

class Documentos:
    def __init__(self):
        info_1 = """¿Qué requiero para iniciar mi servicio social? 

        - Ser alumno inscrito o egresado
        - Constancia de créditos vigente que avale un mínimo del 70% de avance. En caso de ser egresado, deberás contar con constancia del 100% de créditos cursados, carta de pasante o boleta certificada (vigencia no mayor a 3 meses)
        - Constancia de servicio médico vigente (IMSS, ISSSTE o privado) con el que cuentes. Egresados con el 100% de créditos cursados, no es necesaria esta constancia.
        - CURP, no mayor a un mes de expedición.
        - Contar con correo electrónico vigente (personal o institucional).

        IMPORTANTE: únicamente podrás realizarlo dentro del IPN, así como en dependencias y empresas que se encuentren registradas en el SISS (Sistema Institucional de Servicio Social).
        """

        doc_1 =  Document(info_1)
        self.docs =  [doc_1]


    def crear_dataframe(self):
        # Dividiendo los documentos en fragmentos más pequeños (chunks) para que el modelo pueda procesarlos mejor
        text_splitter = RecursiveCharacterTextSplitter(
                  chunk_size=450,
                  chunk_overlap=50
        )

        splits = text_splitter.split_documents(self.docs)

        # Almacenando los chunks en un DataFrame
        chunks = []
        for split in splits:
            chunks.append(split.page_content)

        df = pd.DataFrame(chunks, columns = ['Text']) # Creamos un dataFrame con los textos
        return df
        