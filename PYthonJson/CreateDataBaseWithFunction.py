import json
#Mesed DB.Jsondaki data base-i Python File-da yigmaq Funksiyali varianti
data={}#data adinda bos dict yaradiriq
data["users"]=[]#bu bos dict-e users adinda key elave edirik,ve value-si ise list olmalidi,bos list aciriq
"""#Bu hisseler tekrarlanir deye funksiyaya sala bilerik
Innerdict={}#Bununda qabaginda dict olmalidi,Innnerdict adinda bos dict aciriq
Innerdict["id"]=18#Acilmis dict-e id elave edirik
Innerdict["name"]="Ayxan"#Acilmis dict-e name elave edirik
Innerdict["surname"]="Yaqubov"#Acilmis dict-e surname elave edirik
#data["users"].append(Innerdict)#List oldugu ucun append elemek mumkundur

Innerdict1={}
Innerdict1["id"]=21
Innerdict1["name"]="Ferid"
Innerdict1["surname"]="Memmedov"""
def CreateDict(_id,_name,_surname):
    Innerdict = {}
    Innerdict["id"] = _id
    Innerdict["name"] = _name
    Innerdict["surname"] = _surname
    return Innerdict
"""#Bularda tekrarlanir deye istifadeciden input alaraq doldura bilerik data base-i
data["users"].append(CreateDict(18,"Ayxan","Yaqubov"))
data["users"].append(CreateDict(21,"Ferid","Memmedov"))"""
def GetData(say):
     id=int(input("ID-nizi daxil edin:"))
     name=input("Adinizi daxil edin:")
     surname=input("Soyadinii daxil edin:")
     data['users'].append(CreateDict(id,name,surname))

for say in range(5):
    say+=1
    print(f"---->>>Add new user {say}")
    GetData(say)
with open("Db.Json.","w") as ElaqeQur:
    json.dump(data,ElaqeQur)

GetData(5)


print(data)