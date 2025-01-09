import datetime
import os
import uuid
from peewee import *

# Conexion a la base de datos
db = PostgresqlDatabase(
    os.getenv("DB_NAME"),
    user=os.getenv("DB_USER,"),
    password=os.getenv("DB_PASSWORD,"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT"))
)


# definicion de la clase user como modelo
class User(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4())  # Id Unico
    username = CharField(max_length=200, unique=True)
    password = CharField(max_length=200)
    person_id = CharField(max_length=39, unique=True)
    activated = BooleanField(default=False)
    create_date = DateField(default=datetime.now)
    update_date = DateField(default=datetime.now)

class Meta:
    database = db


db.connect()

db.close()