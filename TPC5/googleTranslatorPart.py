import json
import re
from deep_translator import GoogleTranslator


translated = GoogleTranslator(source='pt', target='en')
file_in = open('conceitos.json', 'r', encoding='utf-8')
dic = json.load(file_in)


new_dic = {}
for designation, description in dic.items():
    en_translate = translated.translate(designation)
    print(en_translate)
    new_dic[designation] = {
                        "des": description,
                        "en": en_translate
                        }

file_out = open('result_ficheiro.json', 'w')
json.dump(new_dic, file_out, ensure_ascii=False, indent=4)

file_in.close()
file_out.close()