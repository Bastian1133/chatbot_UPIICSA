import numpy as np
# Usamos el modelo de embeddings de Google Generative AI para generar los vectores de los documentos y las preguntas.
from langchain_google_genai import GoogleGenerativeAIEmbeddings
embeddings_model = GoogleGenerativeAIEmbeddings(
  model="gemini-embedding-2",
  google_api_key="AIzaSyARZsER14stTHweYD4ynlRPSRBeNEGeKFs"
)

def embeddings_fn(text):
  """
  Crea los embeddings dado un texto
  """
  return embeddings_model.embed_query(text)

def calcular_embeddings(df):
  # Calculamos los embeddings para cada texto de nuestro DataFrame
    df['Embeddings'] = df['Text'].apply(embeddings_fn)

def encontrar_mejor_pasaje(consulta, df):
  # Calcula las distancias entre la consulta y cada documento en el marco de datos utilizando el producto punto.
  query_embedding = embeddings_model.embed_query(consulta)
  dot_products = np.dot(np.stack(df['Embeddings']), query_embedding)

  # Obtiene la ID del que más se parece
  idx = np.argmax(dot_products)

  return df.iloc[idx]['Text'] # Devuelve el texto del índice con el valor máximo.
