import requests
from bs4 import BeautifulSoup
import json

url = "https://www.poste.dz/customer/bureaux_postaux"
response = requests.get(url)
if response.status_code != 200:
    print("erreur non fetch!!!!!!.")
    exit()
soup = BeautifulSoup(response.text, 'html.parser')
select_tag = soup.find('select', {"id": ""}) 
if not select_tag:
    print("non trouvé le tag select *-*.")
    exit()

options = select_tag.find_all('option')
data = []
for option in options:
    value = option.get('value').strip()
    name = option.text.strip()
    if value:
        data.append({"id": value, "name": name})
with open("wilayas.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Les données ont été extraites avec succès et sauvegardées dans 'wilayas.json ** merci d'utiliser les codes de Oualid Hamri")
