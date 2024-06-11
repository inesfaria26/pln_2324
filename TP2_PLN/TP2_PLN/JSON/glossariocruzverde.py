import re
import string
import requests
from bs4 import BeautifulSoup
import json

def extrair_doencas(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        html_content = result.text
    except requests.RequestException as e:
        print(f"Erro ao acessar a URL {url}: {e}")
        return {}

    soup = BeautifulSoup(html_content, 'html.parser')
    divs = soup.find_all("div", class_="row m0 glossaryText")
    dicionario_doencas = {}

    for div in divs:
        titles = div.find_all("div", class_="row m0 titleRow text-left")
        descriptions = [div.find_all("p")[i] for i in range(len(titles)) if i % 2 == 0]
        descriptions = [desc for desc in descriptions if desc.text.strip()]


        for title, desc in zip(titles, descriptions):
            designacao = title.h2.text.strip()
            descricao = desc.text.strip()
            if designacao not in dicionario_doencas:
                dicionario_doencas[designacao] = descricao

    return dicionario_doencas

url_base = "https://www.cruzverde.pt/apoio-cliente/glossario-saude"
urls = [url_base + "/" + c for c in list(string.ascii_uppercase)]

res = {}
for url in urls:
    print(f"Processando URL: {url}")
    dicti = extrair_doencas(url)
    res.update(dicti)

with open("cruzverde.json", "w", encoding="utf-8") as f_out:
    json.dump(res, f_out, indent=4, ensure_ascii=False)


