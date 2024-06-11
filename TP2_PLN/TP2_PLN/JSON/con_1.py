
import locale
import json
#from collections import OrderedDict

locale.setlocale(locale.LC_ALL, 'pt_PT.UTF-8')


def carregar_json(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        return json.load(file)

def guardar_json(dados, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

def combinar_valores(valor1, valor2):
    if isinstance(valor1, list):
        if isinstance(valor2, list):
            return valor1 + valor2
        else:
            return valor1 + [valor2]
    else:
        if isinstance(valor2, list):
            return [valor1] + valor2
        else:
            return [valor1, valor2]        

def concatenar_json(caminho_arquivo1, caminho_arquivo2, caminho_saida):
    dados1 = carregar_json(caminho_arquivo1)
    dados2 = carregar_json(caminho_arquivo2)
    dados_concatenados = dados1.copy()
    
    for chave, valor in dados2.items():
        if chave in dados_concatenados:
            dados_concatenados[chave] = combinar_valores(dados_concatenados[chave], valor)
        else:
            dados_concatenados[chave] = valor
            
    #dados_ordenados = OrderedDict(sorted(dados_concatenados.items()))
    dados_ordenados = dict(sorted(dados_concatenados.items(), key=lambda item: locale.strxfrm(item[0])))
    
    guardar_json(dados_ordenados, caminho_saida)

caminho_arquivo1 = '/Users/inesfaria/Desktop/TP2_PLN/JSON/glossariosaude.json'
caminho_arquivo2 = '/Users/inesfaria/Desktop/TP2_PLN/JSON/cruzverde.json'
caminho_saida = 'concatenado_1.json'

concatenar_json(caminho_arquivo1, caminho_arquivo2, caminho_saida)