from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder="static")

# Ruta explícita para servir archivos estáticos si Heroku no los detecta
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
