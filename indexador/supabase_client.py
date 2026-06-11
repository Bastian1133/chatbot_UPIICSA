import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv("../keys.env") # Carga las variables de entorno desde el archivo keys.env

def get_supabase_client():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    
    if not url or not key:
        raise ValueError("Faltan las credenciales de Supabase en el archivo keys.env")
    
    return create_client(url, key)