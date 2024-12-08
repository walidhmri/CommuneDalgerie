import json
import os

with open('wilayas.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

json_files = [item['id'] for item in data]

combined_data = []

for file_name in json_files:
    file_name= f"{file_name}.json"
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
            combined_data.extend(data)
    else:
        print(f"File {"{file_name}.json"}  existe pas****.")

with open('allcomune.json', 'w', encoding='utf-8') as f:
    json.dump(combined_data, f, ensure_ascii=False, indent=4)

print("JSON fichiers ont étaient combinez a 'allcomune.json' merci d'utiliser les code de walidhmri *_*")
