import json

with open('/Users/inesfaria/Desktop/TP2_PLN/concatenado_2.json', 'r', encoding='utf-8') as file:
    ministerio_saude = json.load(file)

with open('/Users/inesfaria/Desktop/TP2_PLN/JSON/acronyms_and_descriptions.json', 'r', encoding='utf-8') as file:
    acronimos = json.load(file)

categoria_medicamentos = "<i>Categoria: Medicamentos, Vacinas e Insumos</i>"
dados_atualizados = []

for termo, categoria, descricao in ministerio_saude:
    if categoria == categoria_medicamentos:
        # Adicionar o termo original
        dados_atualizados.append([termo, categoria, descricao]) 

        # Verificar se o termo é um acrónimo conhecido
        for sigla, descricao_acronimo in acronimos.items():
            if sigla == termo:
                dados_atualizados.append([sigla + ' - ' + termo, categoria_medicamentos, descricao_acronimo])

ministerio_saude.sort(key=lambda x: x[0])

with open('resultado_concatenado.json', 'w', encoding='utf-8') as file:
    json.dump(ministerio_saude, file, ensure_ascii=False, indent=4)

print("Dados concatenados, ordenados e guardados em 'resultado_concatenado.json'")