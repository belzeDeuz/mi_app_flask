from flask import Flask, request, jsonify

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
        return jsonify({"error": "No se enviaron datos JSON"}), 400

    # Puedes procesar los datos aquí
    respuesta = {
        "datos": data
    }
    return jsonify(respuesta), 201

if __name__ == "__main__":
    # Para desarrollo local, se activa el modo debug
    app.run(debug=True)
