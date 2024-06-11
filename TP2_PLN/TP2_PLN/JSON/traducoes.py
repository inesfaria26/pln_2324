import json
from deep_translator import GoogleTranslator

translated_alemao = GoogleTranslator(source='pt', target='de')
translated_italiano = GoogleTranslator(source='pt', target='it')
translated_ingles = GoogleTranslator(source='pt', target='en')
translated_espanhol = GoogleTranslator(source='pt', target='es')

with open('/Users/inesfaria/Desktop/TP2_PLN/TP2_PLN/resultado_concatenado.json', 'r') as f:
    resultado = json.load(f)

new_resultado = []

for designacao, descricao in resultado:
    descricao_nova = descricao.copy()
    if 'alemao' not in descricao_nova:
        alemao_termo = translated_alemao.translate(designacao)
        new_resultado.append(alemao_termo)
    if 'ingles' not in descricao_nova:
        ingles_termo = translated_ingles.translate(designacao)
        new_resultado.append(ingles_termo)
    if 'espanhol' not in descricao_nova:
        espanhol_termo = translated_espanhol.translate(designacao)
        new_resultado.append(espanhol_termo)
    if 'italiano' not in descricao_nova:
        italiano_termo = translated_italiano.translate(designacao)
        new_resultado.append(italiano_termo)

with open('resultado_traduzido.json', 'w') as f:
    json.dump(new_resultado, f, indent=4, ensure_ascii=False)