import textwrap
import re

class Chunker:
    
    def __init__(self, chunk_size_maximo=500):
        self.chunk_size_maximo = chunk_size_maximo
    
    def _dividir_texto(self, texto: str) -> list:
        fragmentos = []
    
        # Separar por párrafos (doble salto de línea)
        bloques = texto.split("\n\n")
        
        for bloque in bloques:
            lineas = [l.strip() for l in bloque.split("\n") if l.strip()]
            if not lineas:
                continue
            
            # Fusionar la primera línea (encabezado/título) con la segunda,
            # para que no quede como chunk aislado y genérico
            if len(lineas) > 1:
                lineas[1] = f"{lineas[0]} {lineas[1]}"
                lineas = lineas[1:]
            
            for linea in lineas:
                oraciones = re.split(r'(?<=[.!])\s+', linea)
                for oracion in oraciones:
                    oracion = oracion.strip()
                    if oracion:
                        fragmentos.append(oracion)
        
        return fragmentos
    
    def generar_chunks(self, texto: str, fuente: str) -> dict:
        texto_limpio = textwrap.dedent(texto).strip()
        
        # Chunk padre: el bloque completo
        padre = {
            "contexto_completo": texto_limpio,
            "fuente": fuente
        }
        
        # Chunks hijos: cada línea/párrafo enriquecido con el título
        fragmentos = self._dividir_texto(texto_limpio)
        hijos = []
        for fragmento in fragmentos:
            hijos.append({
                "texto_embedding": fragmento,
            })
        
        return {
            "padre": padre,
            "hijos": hijos
        }
    
    def generar_desde_diccionario(self, diccionario: dict) -> list:
        resultado = []
        for nombre_pdf, texto in diccionario.items():
            print(f"Chunkeando: {nombre_pdf}")
            chunks = self.generar_chunks(texto, nombre_pdf)
            resultado.append(chunks)
            print(f"  Padre: 1 bloque")
            print(f"  Hijos: {len(chunks['hijos'])} fragmentos")
        return resultado