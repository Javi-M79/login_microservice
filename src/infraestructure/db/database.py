import os
import psycopg2
from dotenv import load_dotenv


# Carga las variables de entorno del archivo .env
load_dotenv()


def create_connection():
    # Recogemos las variables de entorno de la conexion del archivo .env
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")

    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Conexion realizada con exito")
        return connection
    except Exception as e:
        print("Error al conectar a la base de datos")
