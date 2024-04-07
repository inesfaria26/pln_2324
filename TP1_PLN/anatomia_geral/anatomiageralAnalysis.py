import re
import json

file = open("anatomia_geral.xml", "r", encoding="utf-8")
text = file.read()

def clean(text):
    text = re.sub(r"\s+", " ", text)   # substitui todos os espaços e \n por apenas 1 espaço
    return text.strip() # Remove o \n no início e fim da frase


#limpeza ficheiro xml
text = re.sub(r"</?page.*>","", text)  # Remover <page> e </page>
text = re.sub(r"</?image.*?>", "", text) # Remover <image> e </image>
text = re.sub(r"<[!]DOCTYPE(.*)?>","", text) # Remover <DOCTYPE> e </DOCTYPE>
text = re.sub(r"</?pdf(.*)?>", "", text) # Remover <pdf> e </pdf>
text = re.sub(r"</?fontspec.*?>", "", text) # Remover <fontspec> e </fontspec>
text = re.sub(r"<[?]xml(.*)?>", "", text) # Remover <xml> e </xml>
text = re.sub(r"<i><b>(.*)</b></i>", "", text) # Remover <i><b> e </b></i>
text = re.sub(r"</?text.*?>", "", text) # Remover <text> e </text>

text = re.sub(r"[0-9]+", "", text) # Remove dígitos numéricos 
text = re.sub(r"\s[A-Z](<|,|\n)", "", text) # Remove espaços seguidos de letra maiúscula seguida por < ou \n 
text = re.sub(r"<i><b>(.*)</b></i>", "", text) # Remove texto entre <i><b> e </b></i>
text = re.sub(r"<i>", "<b>", text) # Substitui ocorrências <i> por <b>
text = re.sub(r"</i>", "</b>", text) # Substitui ocorrências </i> por </b>
text = re.sub(r"(\n)+", "", text) # emove todas as ocorrências de uma ou mais quebras de linha \n
text = re.sub(r"</b>(\s)+<b>", "</b><b>", text) # Substitui </b> seguido de um ou mais espaços e <b> por </b><b>
text = re.sub(r"</b><b>", "\n<b>", text) # Substitui </b><b> por uma quebra de linha \n seguida de <b>.
text = re.sub(r"<b>", "@<b>", text) # Adiciona @ antes de cada ocorrência de <b>.
text = re.sub(r"\[\[(.*)\]\]",r"\1", text) # Remove os delimitadores [[ e ]] , mantendo o conteúdo 
text = re.sub(r'</b>\s*(@)?</b>', '', text) # Remove </b> seguido opcionalmente de @ e novamente </b>

text = re.sub(r"-</b></text>\n<text(.*)><b>", "", text) # Juntar expressões que estão separadas pelas regras de translineação
text = re.sub(r"\n(\s*)\n", "\n", text) # Remover espaços
text = re.sub(r"<text(.*)>\s*(\*)(.*)</text>", "", text) # Remover frases inicializadas com *, ** e ***


#print (text) 

# Pesquisar a expressão
list = re.findall(r"<b>\s(.*?)\.</b>(.*?)\s+@", text)
nova_lista = [(designacao, re.sub(r"@<b>|</b>"," ", descricao)) for designacao, descricao in list] #remover @<b> de alguns termos que causava erro

# Conversão 
new_list = []
for designacao, descricao in nova_lista:
    new_designacao = designacao.lower()
    new_descricao = clean(descricao)
    new_list.append([new_designacao, new_descricao])

list = new_list

'''
if list:
    print("A lista contém elementos.")
else:
    print("A lista está vazia.")
'''

dicionario = dict(list)

output = open("anatomiageral.json", "w", encoding="utf-8")
json.dump(dicionario, output, ensure_ascii=False, indent=4)

output.close()

file.close()