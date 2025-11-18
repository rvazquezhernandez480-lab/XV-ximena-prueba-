
from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)
DB = "familias.json" 

def load():
    with open(DB) as f:
        return json.load(f)

def save(data):
    with open(DB, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/qr/<token>")
def qr(token):
    data = load()
    if token not in data:
        return "QR inválido"
    if data[token]["usado"]:
        return "QR ya utilizado"

    info = data[token]
    info["usado"] = True
    save(data)

    # Llama a la plantilla HTML
    return render_template('template.html', familia=info['familia'], cantidad=info['cantidad'])

if __name__ == "__main__":
    app.run()