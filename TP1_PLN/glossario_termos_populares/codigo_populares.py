import re
import json

ficheirotxt = open("Glossario_de_termos_Medicos_Tecnicos_Populares.xml", encoding="utf-8")
text = ficheirotxt.read()

text = re.sub(r"</?fontspec.*?>", "", text) 
text = re.sub(r"</?page.*>", "", text)
text = re.sub(r"</?text.*?>", "", text) 


text = re.sub(r"<b>[A-Z]</b>", "", text) #termos que correspondem a apenas uma maiuscula sao eliminados, especie de blacklist
#maiusculas apenas aparecem nesses casos especificos

text = re.sub (r"<i>", "", text)
text = re.sub (r"</i>", "", text)
termos = re.findall(r"<b>(.*)</b>", text) #recolha dos termos


text2 = re.sub(r"<b>(.*)</b>", "", text) #remocão dos termos na variavel text2
text2= re.sub(r"\n+", "", text2) #remoção dos paragrafos
text2 = re.sub(r"\s,", "", text2) #remover espaços seguidos de virgula, presente apos o (pop)



text2 = re.sub(r"\(pop\)", "@@", text2) #substituir o (pop) por @@ para marcação
#text2 = re.sub(r"@@  @@", "@@" , text2)


resultado=open("glossario_termos_populares.txt", "w", encoding='UTF-8')
resultado.write(text2)
resultado.close()


designacoes1 = re.findall(r"@(?:\s|,|X)(.*?)@", text2)  #encontra todas as que começam em 
#@ seguido por um espaço em branco, vírgula ou "X", e terminam com "@".
# As partes entre "@" e "@" são capturadas pelo grupo (.*?) e retornadas como uma lista.
#(?: ) identifica o conteudo como necessario mas nao o captura
designacoes2= re.findall(r"(^.*?)@", text2) #encontra o que começa no início de uma linha e termina com @

designacoes= designacoes2 + designacoes1  #conjunto total de designacoes

'''termos2=[]
designacoes2=[]

for termo in termos:
    termos2.append(termo)

for designacao in designacoes:
    designacoes2.append(designacao)'''

lista_de_listas = [[x, y] for x, y in zip(termos, designacoes)]

dicti={}
dicti = dict(lista_de_listas)

output = open ("json_termos_populares.json", "w", encoding="utf-8")
json.dump(dicti, output, ensure_ascii=False, indent=4)
output.close()

