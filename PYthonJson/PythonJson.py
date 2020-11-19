import json
with open("DB.Json.py", "r") as Fayl_ileElaqe:#Yaradilan fayli conn kimi aciriq
    data = json.load(Fayl_ileElaqe)#
print(data)
for item in data["users"]:
    #print(f"{item['name']} | {item['surname']} | {item['id']}")
    if item['id']== 21:#yasi 21 olan userin adini deyis
        item['name']="Ayxan"
        item['surname']="Yaqubov"
print(data)
with open("DB.Json.py", "w") as Fayl_ileElaqe:
    json.dump(data,Fayl_ileElaqe)

