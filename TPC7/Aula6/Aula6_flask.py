from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

with open('Aula6/conceitos.json', encoding='utf-8') as file:
    conceitos = json.load(file)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/conceitos")
def listar_conceitos():
    return render_template("conceitos.html", conceitos=conceitos)

@app.route("/conceitos/<designacao>") #não dá
def consultar_conceitos(designacao):
    if designacao in conceitos:
        desig = conceitos[designacao]
        desig_pt = desig["desc"]
        desig_en = desig["en"]
        desig_fr = desig.get("fr") 
        desig_es = desig.get("es")
        desig_de = desig.get("de")
    
        return render_template("descricao.html",desig_pt = desig_pt, desig_en = desig_en, desig_es = desig_es, desig_de = desig_de, desig_fr = desig_fr, designacao = designacao)  
        
    else:
        return render_template('erro.html', erro='Conceito não existe na nossa base de dados. ')


@app.route("/conceitos/<conceito>")
def detalhes_conceito(conceito):
    if conceito in conceitos:
        return render_template("designacoes.html", conceito=conceitos[conceito])

@app.route("/conceitos", methods=["POST"])
def adicionar_conceitos():
    designacao = request.form.get("designacao")
    descricao = request.form.get("descricao")
    traducao = request.form.get("en")

    conceitos[designacao] = {
        "desc": descricao,
        "en": traducao
    }
    return render_template("conceitos.html", conceitos=conceitos)

@app.route("/conceitos/<designacao>", methods =["DELETE"])
def delete_conceitos(designacao):
    del conceitos[designacao]
    return render_template("designacoes.html", conceitos=conceitos)


app.run(host="localhost", port=4002, debug=True)
