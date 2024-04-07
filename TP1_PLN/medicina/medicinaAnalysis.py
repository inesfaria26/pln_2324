#!/usr/bin/env python3
import re
import json
ficheiro = open('medicina.xml','r')
texto =ficheiro.read()

#Limpar o texto
texto = re.sub(r'^[\d\D]+<text\stop="128"\sleft="121"\swidth="3"\sheight="14"\sfont="17">\s</text>',r'',texto)  # Remover parte inicial
texto = re.sub(r'<page number="544" position="absolute" top="0" left="0" height="918" width="663">\n[\d\D]+',r'',texto) # Remover parte final 
texto = re.sub(r"</?page.*>","", texto)  # Remover <page> e </page>
texto = re.sub (r"</?text.*?>", "", texto) # remover <text> e </text>
texto = re.sub(r"</?fontspec.*?>", "", texto) # Remover <fontspec> e </fontspec>
texto = re.sub(r'</?pdf2xml.*?>', r'', texto)
texto = re.sub(r"<[?]xml(.*)?>", "", texto) # Remover <xml> e </xml>
texto = re.sub(r"<[!]DOCTYPE(.*)?>","", texto) # Remover <DOCTYPE> e </DOCTYPE>
texto = re.sub(r"</?pdf(.*)?>", "", texto) # Remover <pdf> e </pdf>
texto = re.sub(r"\n(\s*)\n", "", texto) # Remover espaços
texto = re.sub(r'[ ]{2,}', r'', texto) # Remover espaços nos meios das palavras
texto = re.sub(r'V\nocabulario\n\d+',r'',texto) # Apagar informações sobre o cabeçalho
texto = re.sub(r'<text[^>]*><b>[A-Z]</b>\s*</text>\n', '', texto) # Remover letras isoladas s/ espaços


texto = re.sub(r"</b>+", r"</b>\n", texto) # Colocar as categorias em linhas diferentes
texto = re.sub(r'<b></b>', r'', texto)
texto = re.sub(r'<b> </b>', r'', texto)
texto = re.sub(r'<i> </i>', r'', texto)


#Marcação do texto
texto = re.sub(r'(SIN\.-)', r'\n\1@', texto) #Sinónimos
texto = re.sub(r'(VAR\.-)', r'\n\1§', texto) #Variantes
texto = re.sub(r'(Nota\.-)',r'\n\1£',texto) #Notas


#Traduções
texto = re.sub(r'(\bes\b)', r'\n\1#', texto) #Espanhol
texto = re.sub(r'(\ben\b)', r'\n\1$', texto) #Inglês
texto = re.sub(r'(\bla\b)', r'\n\1%', texto) #Latim
texto = re.sub(r'(\bpt\b)', r'\n\1&', texto) #Português



file = open('med_atualizado.xml', 'w',encoding = 'utf-8')
file.write(texto)
file.close

#Extração de informação relativa ao vocabulário, nomeadamente as traduções

portugues = []
espanhol = []
ingles = []
latim = []
portugues = []

all_ES = re.findall(r'\#\s*<i>(\w+)</i>', texto)
for palavra in all_ES:
    espanhol.append(palavra)

all_IN = re.findall(r'\$\s*<i>(\w+)</i>', texto)
for palavra in all_IN:
    ingles.append(palavra)

all_LA = re.findall(r'\%\s*<i>(\w+)</i>', texto)
for palavra in all_LA:
    latim.append(palavra)

all_PT = re.findall(r'\&\s*<i>(\w+)</i>', texto)
for palavra in all_PT:
    portugues.append(palavra)

print(portugues)


dicE = {'Termos': espanhol}
dicI = {'Termos': ingles}
dicL = {'Termos':  latim}
dicP = {'Termos': portugues}

dicionario = {}
dicionario['Espanhol'] = dicE
dicionario['Inglês'] = dicI
dicionario['Latim'] = dicL
dicionario['Português'] = dicP

output = open("medicina.json", "w", encoding="utf-8")
json.dump(dicionario, output, ensure_ascii=False, indent=4)

output.close()

ficheiro.close()