from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/datos", methods=["POST"])
def recibir_datos():
    # Depuración: Ver los datos recibidos en crudo
    print("Contenido en bruto recibido:", request.data)
    print("Headers recibidos:", request.headers)

    # Intentar obtener JSON de la petición
    try:
        data = request.get_json(force=True)  # Forzamos JSON si no se detecta automáticamente
    except Exception as e:
        return f"Error al procesar JSON: {str(e)}", 400

    if not data:
        return "Error: No se enviaron datos JSON", 400

    # Extraemos los datos esperados
    nombre = data.get("nombre", "Desconocido")
    edad = data.get("edad", "No especificada")

    # Formateamos la respuesta
    respuesta = f"Datos recibidos\nNombre: {nombre}\nEdad: {edad}"
    
    return respuesta, 201, {"Content-Type": "text/plain; charset=utf-8"}

if __name__ == "__main__":
    app.run(debug=True)
