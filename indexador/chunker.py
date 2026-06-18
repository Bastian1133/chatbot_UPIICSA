import textwrap

class Chunker:
    
    def __init__(self, chunk_size_maximo=500):
        self.chunk_size_maximo = chunk_size_maximo
    
    def _dividir_texto(self, texto: str) -> list:
        fragmentos = []
        
        # Primero separar por párrafos (doble salto de línea)
        bloques = texto.split("\n\n")
        
        for bloque in bloques:
            # Dentro de cada párrafo, separar por línea
            lineas = bloque.split("\n")
            for linea in lineas:
                linea = linea.strip()
                if not linea:
                    continue
                # Solo si una línea supera el límite, partir por oración
                if len(linea) > self.chunk_size_maximo:
                    partes = linea.split(". ")
                    for parte in partes:
                        parte = parte.strip()
                        if parte:
                            fragmentos.append(parte)
                else:
                    fragmentos.append(linea)
        
        return fragmentos
    
    def generar_chunks(self, texto: str, titulo: str, fuente: str) -> dict:
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
                "texto_embedding": f"{titulo}: {fragmento}"
            })
        
        return {
            "padre": padre,
            "hijos": hijos
        }
    
    def generar_desde_diccionario(self, diccionario: dict) -> list:
        resultado = []
        for nombre_pdf, texto in diccionario.items():
            titulo = nombre_pdf.replace(".pdf", "").replace("_", " ").title()
            print(f"Chunkeando: {nombre_pdf} — título: '{titulo}'")
            chunks = self.generar_chunks(texto, titulo, nombre_pdf)
            resultado.append(chunks)
            print(f"  Padre: 1 bloque")
            print(f"  Hijos: {len(chunks['hijos'])} fragmentos")
        return resultado