import re

file = open('dicionario_medico.txt')
text = file.read()

text = re.sub(r'\n\n\f(.+\n\n)', r'\n\1', text)
text = re.sub(r'\n\n\f((?:.+))\n[A-ZÁÀÂÃÉÍÓÕÚ]', r'\n\n\1', text) # mantém apenas o conteúdo capturado pelo grupo de captura
text = re.sub(r'\n\n\f', r'\n', text)
text = re.sub(r'\f','',text)
captureWords = re.sub(r'\n\n(.+)', r"\n\n@\1", text)
captureDescription = re.sub(r'\n([^@\n].+)', r'\n€\1', captureWords)
newDescription = re.sub(r'(@.+)\n\n@(.+)', r'\1\n€\2', captureDescription) # separa linhas marcadas com "@" das marcadas com "€"
removeLines = re.sub(r'(€.+)(?:\n€(.+))+', r'\1\2', newDescription) # adiciona um "€" na frente de cada linha que não começa com "@"
remove = re.sub(r'[@€]', r'', removeLines) # remove todos os caracteres de quebra de página

newEntries = re.findall(r"\n\n(.+)\n(.+)", remove)

file.close()

html = open('dicionario_medico.html','w', encoding='utf-8')
head = '''
<html>
<head> 
<meta charset='utf-8'/>
<title> Dicionário Médico </title>
</head> 
<body style = "background-color:lightgreen;">
<h1 style = "text-align:center; color:darkgreen;"> <br> Dicionário Médico </h1>

'''
entries=list(newEntries)
entries.insert(0,("Designação", "Descrição"))

# Create the HTML table

table = '<table style="border: 1px solid black; border-collapse: collapse; table-layout: auto;">\n'
for i, row in enumerate(entries):
    table += '<tr style="border: 1px solid black; border-collapse: collapse;">'
    for j, item in enumerate(row):
        if i == 0: 
            table += '<th style="font-weight:bold;border-right: 1px solid black;">{}</th>'.format(item)
        else:
            table += '<td style="border-right: 1px solid black;">{}</td>'.format(item)
    table += "</tr>\n"
table += "</table>"

footer = '''

</body>
</html>
'''

html.write(head+table+footer)

html.close()