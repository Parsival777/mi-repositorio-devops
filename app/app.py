from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Despliegue exitoso! Pipeline CI/CD ejecutándose correctamente.'

if __name__ == '__main__':
    # El puerto 5000 es el estándar para Flask
    app.run(debug=True, host='0.0.0.0', port=5000)