import requests
from bs4 import BeautifulSoup
import json
import re

def extrair_termos(url):
    result = requests.get(url)
    html = result.text
    soup = BeautifulSoup(html, 'html.parser')

    # Encontre todos os divs com a classe 'kt-tab-inner-content-inner'
    termos_divs = soup.find_all("div", class_="kt-tab-inner-content-inner")
    dicionario_termos = {}

    for termo_div in termos_divs:
        # Extraia todos os <p> tags dentro do div
        ps = termo_div.find_all("p")

        # Itere através dos <p> tags e encontre os termos e suas descrições
        for i in range(len(ps)):
            strong_tag = ps[i].find("strong")
            if strong_tag:
                termo = strong_tag.text.strip()
                # Verifique se há uma descrição disponível
                descricao = ps[i + 1].get_text(separator=" ", strip=True) if i + 1 < len(ps) else ""
                descricao = re.sub(r"[NBSP]|[ZWSP]", " ", descricao)
                dicionario_termos[termo] = descricao

    return dicionario_termos


url = "https://www.mdsaude.com/glossario/"
res = extrair_termos(url)

# Salvar o resultado em um arquivo JSON
with open("glossariosaude.json", "w", encoding='utf-8') as f_out:
    json.dump(res, f_out, indent=4, ensure_ascii=False)

print("Extração concluída e dados salvos em glossariosaude.json")
