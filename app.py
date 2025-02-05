from flask import Flask, request, render_template

app = Flask(__name__)

# Página principal con HTML
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Página para recibir datos con un formulario
@app.route("/datos", methods=["GET", "POST"])
def recibir_datos():
    if request.method == "POST":
        nombre = request.form.get("nombre", "Desconocido")
        edad = request.form.get("edad", "No especificada")
        return render_template("resultado.html", nombre=nombre, edad=edad)
    
    return render_template("formulario.html")

if __name__ == "__main__":
    app.run(debug=True)
