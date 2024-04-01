from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

with open('conceitos.json', encoding='utf-8') as file:
    conceitos = json.load(file)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/conceitos")
def listar_conceitos():
    return render_template("conceitos.html", conceitos=conceitos)

@app.route("/conceitos/<designacao>")
def consultar_conceitos(designacao):
    desig = conceitos[designacao]
    desig_pt = desig["desc"]
    desig_en = desig["en"]
    desig_fr = desig.get("fr") 
    desig_es = desig.get("es")
    desig_de = desig.get("de")
    
    return render_template("descricao.html",desig_pt = desig_pt, desig_en = desig_en, desig_es = desig_es, desig_de = desig_de, desig_fr = desig_fr, designacao = designacao)  


@app.route("/conceitos/<conceito>")
def detalhes_conceito(conceito):
    if conceito in conceitos:
        return render_template("designacoes.html", conceito=conceitos[conceito])


app.run(host="localhost", port=4002, debug=True)