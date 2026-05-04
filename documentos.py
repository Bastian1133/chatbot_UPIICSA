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

        info_2 = """Indicaciones sobre la prestación de Prácticas Profesionales

        1.- Solo se podrán registrar los alumnos que tengan el 50% y el 99.99% de créditos y que se encuentren inscritos en el periodo. La presente situación es debido a que únicamente los alumnos que se encuentran inscritos son derechohabientes al seguro facultativo del IMSS.

        2.- Podrán registrar Prácticas Profesionales los egresados que cuenten con seguro vigente (IMSS, ISSSTE, IMSS BIENESTAR, PRIVADO) recuerda que como egresado puedes realizar hasta 8 horas como máximo diarias, de lunes a viernes.

        3.- El lugar donde se pretenda realizar las estancias o prácticas profesionales, puede ser en dependencias públicas o en empresas privadas (si es empresa privada, deberá contar con registro en la página de SISA-SIBOLTRA).

        4.- Las estancias o prácticas profesionales deberán realizarse de forma presencial

        5.- Los registros se llevarán de la siguiente forma:

        a.- El prestador deberá enviar los siguientes documentos en formato PDF y archivos separados al correo practicas_upiicsa@ipn.mx con el asunto: INICIO PRÁCTICAS PROFESIONALES.

            Constancia de créditos o estudios (la podrás descargar directamente de tu SAES)

            Cédula de registro descarga aquí

            Constancia de vigencia de derechos al IMSS, ISSSTE, IMSS BIENESTRAR, PRIVADO, vigente (en caso de no entregarlo se considerará invalido).

            Impresión de captura de pantalla del registro de la empresa en la plataforma SISAE-SIBOLTRA (dicha captura la debe proporcionar la empresa). NOTA: El registro lo deberá realizar la empresa.

            Impresión de captura de pantalla del registro en la plataforma SISAE-SIBOLTRA del alumno.

            Copia de horario de clases del periodo inscrito (sólo alumnos) recuerda que si eres alumno inscrito solo puedes realizar 4 horas diarias de lunes a viernes.

            El área de prácticas profesionales les enviará vía correo electrónico, carta de presentación y ustedes deberán de enviarnos la carta de aceptación por parte de la empresa sobre el mismo hilo de mensajes, esto para llevar un seguimiento a su trámite.

            Deberás cubrir mínimo 150hrs.

        6.- Las Prácticas Profesionales no acepta horas retroactivas, todo el tramite deberá de ser con fechas actuales al inicio de las mismas.

        7.- Al termino de las Prácticas Profesionales deberán de enviar al correo electrónico practicas_upiicsa@ipn.mx con el asunto TÉRMINO DE PRÁCTICAS PROFESIONALES en formato PDF y en archivos separados la documentación de termino:

            Carta de término consulta ejemplo aquí
            Reportes mensuales descarga aquí
            Informe final consulta ejemplo aquí

        8.- Después de 3 meses sin actividad en tu trámite, tu proceso será CANCELADO.

        9.- No se puede realizar prácticas o estancias en la institución donde hubo una cancelación anterior.

        10.- La empresa deberá de contar con su propia hoja membretada y sello oficial.

        11.- Las firmas como los sellos deben ser autógrafos.
        """

        doc_1 =  Document(info_1)
        doc_2 =  Document(info_2)
        self.docs =  [doc_1, doc_2]


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
        