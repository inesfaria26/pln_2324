import json
import pprint

with open('resultado_concatenado.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

result = {}

for entry in data:
    termo = entry[0]

    categoria = ""
    definicao = ""

    try:
        categoria = entry[1].split('Categoria: ')[1].split('</i>')[0].strip()
    except IndexError:
        print(f"Erro ao processar a categoria do termo: {termo}")

    if len(entry) > 2:
        definicao = entry[2]
        if isinstance(definicao, list):
            definicao = ' '.join(definicao)
        elif not isinstance(definicao, str):
            definicao = str(definicao)
        definicao = definicao.replace('\n', ' ')
    else:
        print(f"Erro ao processar a definição do termo: {termo}")

    result[termo] = {
        "categoria": categoria,
        "definicao": definicao
    }

pprint.pprint(result)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)
