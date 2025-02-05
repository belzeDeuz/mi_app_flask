from flask import Flask, request, render_template

app = Flask(__name__)

# Página principal con HTML
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Página para mostrar y recibir datos
@app.route("/datos", methods=["GET", "POST"])
def recibir_datos():
    if request.method == "POST":
        # Intentar obtener JSON o datos de formulario
        try:
            data = request.get_json(force=True, silent=True)  # Si no se detecta JSON, no lanza error
        except Exception as e:
            return f"Error al procesar JSON: {str(e)}", 400

        if not data:
            nombre = request.form.get("nombre", "Desconocido")
            edad = request.form.get("edad", "No especificada")
        else:
            nombre = data.get("nombre", "Desconocido")
            edad = data.get("edad", "No especificada")

        return render_template("resultado.html", nombre=nombre, edad=edad)

    return render_template("formulario.html")

if __name__ == "__main__":
    app.run(debug=True)
