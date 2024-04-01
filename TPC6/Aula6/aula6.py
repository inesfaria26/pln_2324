import json

with open("conceitos.json", encoding="iso-8859-1") as file:
    conceitos = json.load(file)

with open("termos_traduzidos.txt", encoding="utf-8") as file_trad:
    trad_dict = {}
    for line in file_trad:
        if "@" in line:
            pt, en = line.strip().split("@")
            trad_dict[pt.strip()] = en.strip()
        else:
            # Handle lines without "@" separator, if needed
            pass

res = {}
for conceito in conceitos:
    if conceito in trad_dict:
        tmp = {
            "desc": conceitos[conceito],
            "en": trad_dict[conceito]
        }
        res[conceito] = tmp
    else:
        tmp = {
            "desc": conceitos[conceito],
            "en": "sem tradução"
        }
        res[conceito] = tmp

file_out= open("conceitos.json","w")
json.dump(res,file_out, ensure_ascii=False, indent=4)
