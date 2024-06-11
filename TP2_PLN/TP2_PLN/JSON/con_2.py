import json

with open('/Users/inesfaria/Desktop/TP2_PLN/JSON/glossario_ministerio_saude.json', 'r', encoding='utf-8') as file:
    ministerio_saude = json.load(file)

with open('/Users/inesfaria/Desktop/TP2_PLN/concatenado_1.json', 'r', encoding='utf-8') as file:
    termos_medicos = json.load(file)

categoria_doencas = "<i>Categoria: Doenças</i>"
termos_medicos_lista = [[termo, categoria_doencas, descricao] for termo, descricao in termos_medicos.items()]


ministerio_saude.extend(termos_medicos_lista)
ministerio_saude.sort(key=lambda x: x[0])

with open('concatenado_2.json', 'w', encoding='utf-8') as file:
    json.dump(ministerio_saude, file, ensure_ascii=False, indent=4)

print("Dados concatenados e guardados em 'concatenado_2.json'")
