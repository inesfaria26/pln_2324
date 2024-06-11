from bs4 import BeautifulSoup
import requests
import json
import string

def extrair_termos(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao acessar a URL {url}: {e}")
        return {}

    html = result.text
    soup = BeautifulSoup(html, 'html.parser')
    dicionario_termos = {}

    # Encontrar todas as divs que contêm as siglas e descrições
    sections = soup.find_all("div", class_="cms-editor")
    for section in sections:
        letras = section.find_all("div")
        for i in range(0, len(letras) - 1, 2):
            termo = letras[i].find("span").get_text(strip=True)
            # Verificar se a próxima div contém uma descrição
            descricao_div = letras[i + 1]
            descricao_span = descricao_div.find("span")
            descricao = descricao_span.get_text(strip=True) if descricao_span else ""
            dicionario_termos[termo] = descricao
    return dicionario_termos

def processar_glossario(base_url, letras):
    res = {}
    for letra in letras:
        url = f"{base_url}#{letra}"
        print(f"Processando URL: {url}")
        termos = extrair_termos(url)
        res.update(termos)
    return res

def limpar_dados(dados):
    return {sigla: descricao for sigla, descricao in dados.items() if descricao != "Topo" and sigla not in string.ascii_uppercase}

def limpar_dados2(dados):
    return {sigla: descricao for sigla, descricao in dados.items() if descricao not in dados or dados[descricao] == sigla}

"""
def corrigir_correspondencia(dados):
    correspondencia_corrigida = {}
    for sigla, descricao in dados.items():
        if descricao in dados and dados[descricao] == sigla:
            correspondencia_corrigida[sigla] = descricao
        else:
            correspondencia_corrigida[sigla] = descricao
    return correspondencia_corrigida
"""

base_url = "https://www.infarmed.pt/web/infarmed/glossario"
letras = list(string.ascii_uppercase)
resultado = processar_glossario(base_url, letras)
resultado_limpo = limpar_dados(resultado)
res = limpar_dados2(resultado_limpo)
#resultado_corrigido = corrigir_correspondencia(res)

with open("acronyms_and_descriptions.json", "w", encoding="utf-8") as f_out:
    json.dump(res, f_out, indent=4, ensure_ascii=False)
