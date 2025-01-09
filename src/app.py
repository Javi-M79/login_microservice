from flask import Flask
from infraestructure.db.database import create_connection
from flask import Flask

from infraestructure.db.database import create_connection

app = Flask(__name__)

# Creamos la conexion. Traemos el metodo desde infraestructure/database_config
conection = create_connection()


# Ruta de prueba
# Decorador
@app.route("/")
def home():
    return f"Bienvenido a Katalyst Control Suit"


if __name__ == '__main__':
    app.run(debug=True)
