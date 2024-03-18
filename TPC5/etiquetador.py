import json
import re
from deep_translator import GoogleTranslator

# Load the medical terms and their definitions from the 'conceitos.json' file
file_conceitos = open("conceitos.json")
texto = file_conceitos.read()
conceitos = json.loads(texto)
conceitos_min = {chave.lower(): conceitos[chave] for chave in conceitos}

# List of words that should not be translated or included in the tooltips
blacklist = ["e", "de", "para", "pelo", "os", "são", "este", "tipo"]

# Function to translate a word from Portuguese to English using the 'deep_translator' library
translated = GoogleTranslator(source='pt', target='en')
print(translated)

def translate_word(word):
    return translated.translate(word)

# Function to add tooltips with descriptions and translations for the medical terms in the text
def etiquetador(matched):
    palavra = matched[0]
    original = palavra
    palavra = palavra.lower()
    if palavra in conceitos_min and palavra not in blacklist:
        descricao = conceitos_min[palavra]
        descricao = re.sub(r"<br>\s*",r"", descricao)
        translated = translate_word(palavra)
        return f'<a title="{descricao} - {translated}">{original}</a>'
    else:
        return original

# Replace newline characters with <br> tags and form feed characters with <hr> tags
texto_processado = re.sub(r'\n', '<br>', texto)
texto_processado = re.sub(r'\f', '<hr>', texto_processado)
texto_processado = re.sub(r'\b(\w+)\b', etiquetador, texto_processado)

# Write the processed text to an HTML file named 'livro.html'
file_livro = open("livro.html","w")
file_livro.write(texto)
file_livro.close()

