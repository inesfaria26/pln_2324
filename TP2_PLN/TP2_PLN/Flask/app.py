from flask import Flask, request, render_template, redirect, url_for
import json

app = Flask(__name__)

def ler_conceitos():
    with open('/Users/inesfaria/Desktop/TP2/TP2_PLN/JSON/result.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def escrever_conceitos(conceitos):
    with open("/Users/inesfaria/Desktop/TP2/TP2_PLN/JSON/result.json", 'w', encoding='utf-8') as f:
        json.dump(conceitos, f, ensure_ascii=False, indent=4)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contactos")
def contactos():
    return render_template("contactos.html")

@app.route("/sobrenos")
def sobrenos():
    return render_template("sobrenos.html")

@app.route("/conceitos", methods=["GET", "POST"])
def gerenciar_conceitos():
    if request.method == "GET":
        termo_pesquisado = request.args.get("termo")
        conceitos = ler_conceitos()

        if termo_pesquisado:
            conceitos_pesquisados = {termo: info for termo, info in conceitos.items() if termo_pesquisado.lower() in termo.lower()}
            return render_template("conceitos.html", conceitos=conceitos, conceitos_pesquisados=conceitos_pesquisados, termo_pesquisado=termo_pesquisado)
        
        return render_template("conceitos.html", conceitos=conceitos)

    elif request.method == "POST":
        titulo = request.form["titulo"]
        categoria = request.form["categoria"]
        descricao = request.form["descricao"]

        novos_conceitos = ler_conceitos()
        novos_conceitos[titulo] = {"categoria": categoria, "definicao": descricao}
        escrever_conceitos(novos_conceitos)

        return redirect(url_for("gerenciar_conceitos"))

if __name__ == "__main__":
    app.run(debug=True)
