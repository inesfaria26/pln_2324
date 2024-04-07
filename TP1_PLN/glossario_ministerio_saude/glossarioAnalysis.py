#!/usr/bin/env python3
import re
import json

ficheiro = open('glossario_ministerio_saude.xml','r',  encoding="utf-8")
texto = ficheiro.read()

#Limpeza de texto e marcação 
texto = re.sub(r'<page number="107" position="absolute" top="0" left="0" height="1263" width="892">\n[\d\D]+',r'',texto) # Remove parte final 
texto = re.sub(r'<page number="15" (.*\n*){11}', r'', texto) # Remover parte inicial
texto = re.sub(r"</?page.*>","", texto)  # Remover <page> e </page>
texto = re.sub (r"</?text.*?>", "", texto) # remover <text> e </text>
texto = re.sub(r"</?fontspec.*?>", "", texto) # Remover <fontspec> e </fontspec>
texto = re.sub(r'</?pdf2xml.*?>', r'', texto)
texto = re.sub(r'<image.+/>', r'',texto)
texto = re.sub(r"<[?]xml(.*)?>", "", texto) # Remover <xml> e </xml>
texto = re.sub(r"<[!]DOCTYPE(.*)?>","", texto) # Remover <DOCTYPE> e </DOCTYPE>
texto = re.sub(r"</?pdf(.*)?>", "", texto) # Remover <pdf> e </pdf>
texto = re.sub(r'<b>\d{2}[15|3|5|7|9]</b>\n<b>.*</b>\n', r'', texto) # Retirar número de páginas ímpares
texto = re.sub(r'<b>.*</b>\n<b>\d{2}[16|2|4|6|8]</b>\n', '', texto) # Retirar número de páginas pares

texto = re.sub(r"<text(.*)>\s*(\*)(.*)</text>", "", texto) # Remover frases inicializadas com *, ** e ***
texto = re.sub(r"\n(\s*)\n", "\n", texto) # Remover espaços 
texto = re.sub(r"[A-Z]\n\d{1,3}", "", texto) # Retira letras
texto = re.sub(r"\d{1,3}\n", "", texto) # Retira números
texto = re.sub(r"<b> </b>", "", texto) # Remove os <b> e </b>


texto = re.sub(r'<text .+?>',"",texto) # retira <text top="605" left="176" width="289" height="16" font="14"> de todo o texto
texto = re.sub(r'<position="absolute" top="0" left="0" height="918" width="663">[\d\D]+',r'',texto)
texto = re.sub(r'</text>', r'', texto) # Remove os </text>
texto = re.sub(r'</b>\n<b>','',texto) # Colocar os títulos todos na mesma linha
texto = re.sub(r'</i>\n<i>','',texto) # Colocar as categorias todas na mesma linha


texto = re.sub(r'<i>([^Categoria])(.*)</i>',r'\1\2', texto)
texto = re.sub(r"<i>Categoria:?\s?</i>\n(.*)\n(.*)\s\n\s", r"<i>Categoria: \1\2</i>\n", texto)
texto = re.sub(r"<i>Categoria:?\s?</i>\n(.*)\n", r"<i>Categoria: \1</i>\n", texto)
texto = re.sub(r"em </i>\nSaúde", r" em Saúde</i>\n", texto)
texto = re.sub(r"</i>\n", r"</i>\n@", texto)
texto = re.sub(r"\n<b>", r"@\n<b>", texto)
texto = re.sub(r"\\n", "", texto)
texto = re.sub(r"\\n@", "", texto)



file = open('glossario_atualizado.xml', 'w',encoding = 'utf-8')
file.write(texto)
file.close



#Extração de Informação

dicionario = {}
#ver termos que n tem descrições

all_titles = re.findall(r'<b>(.+)</b>',texto) # Extrai o título
all_descriptions = re.findall(r'@([^@<]+)@', texto) # Extrai tudo o que está a frente do arroba
all_categories = re.findall(r'<i>.+\n.+',texto) # Extrai Categoria: categoria

titulos = []
descricoes = []
categorias = []

for titulo in all_titles:
    titulos.append(titulo)

for categoria in all_categories:
    categorias.append(categoria)

for descricao in all_descriptions:
    descricoes.append(descricao)
#print(titulos)
#print(descricoes)
""""
lista_dicionarios = []

# Verificar se as listas têm o mesmo tamanho
if len(titulos) == len(descricoes) == len(categorias):
    for i in range(len(titulos)):
        dicionario = {
            'titulo': titulos[i],
            'categoria': categorias[i],
            'descricao': descricoes[i]
        }
        lista_dicionarios.append(dicionario)
else:
    print("As listas não têm o mesmo tamanho!")

# Visualizando a lista de dicionários
for item in lista_dicionarios:
    print(item)
"""

# Verificar o comprimento das listas e usando o menor comprimento para iterar
lista = []
comprimento_minimo = min(len(titulos), len(descricoes), len(categorias))

for i in range(comprimento_minimo):
    tuplo = (titulos[i], categorias[i] if i < len(categorias) else None, descricoes[i])
    lista.append(tuplo)

output = open("glossario.json", "w", encoding="utf-8")
json.dump(lista, output, ensure_ascii=False, indent=4)

output.close()

ficheiro.close()