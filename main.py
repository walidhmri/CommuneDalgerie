import requests
from bs4 import BeautifulSoup
import json

url = "https://www.poste.dz/customer/bureaux_postaux?wilaya="

with open('wilayas.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

wilaya = [item['id'] for item in data]

for i in range(len(wilaya)):
    response = requests.get(url + str(wilaya[i]))
    
    if response.status_code != 200:
        print("erreur tant l'exctaction.")
        continue
    
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    
    if not table:
        print(f"Tableau non trouvé {wilaya[i]}. pass;ent...")
        continue
    
    rows = table.find_all('tr')
    data = []
    
    for row in rows[1:]:
        cells = row.find_all('td')
        if len(cells) < 3:
            continue
        postal_entry = {
            "wilaya" : str(wilaya[i]),
            "nom": cells[0].text.strip(),
            "code_postal": cells[1].text.strip(),
            "nom_exact": cells[2].text.strip(),
        }
        data.append(postal_entry)
    
    filename = f"{wilaya[i]}.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    print(f"Les données ont été extraites avec succès et sauvegardées dans {filename} merci d'utiliser les codes de walidhmri")
