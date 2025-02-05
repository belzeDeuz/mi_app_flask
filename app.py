from flask import Flask, request

app = Flask(__name__)

# Endpoint GET
@app.route("/", methods=["GET"])
def home():
    return "¡Hola, mundo! Bienvenido a mi app en Heroku."

# Endpoint POST
@app.route("/datos", methods=["POST"])
def recibir_datos():
    # Se espera recibir datos en formato JSON
    data = request.get_json()
    if not data:
        return "Error: No se enviaron datos JSON", 400

    # Extraemos los datos esperados
    nombre = data.get("nombre", "Desconocido")
    edad = data.get("edad", "No especificada")
    
    # Formateamos la respuesta de la forma solicitada
    respuesta = f"Datos recibidos\nNombre: {nombre}\nEdad: {edad}"
    
    # Retornamos la respuesta como texto plano
    return respuesta, 201, {"Content-Type": "text/plain; charset=utf-8"}

if __name__ == "__main__":
    # Para desarrollo local, se activa el modo debug
    app.run(debug=True)
