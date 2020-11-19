f=open("data.txt", "r")
#print(f.read())#Acdigimiz fayli oxumaq ucun istifade olunur.
#print(f.read(2))#Fayldaki textin daxil etdiyimiz sayda characterini oxuyur.
#print(f.readline())#Acdigimiz faylin bir setrini oxuyur,nece defe cagirsaq o qeder setr oxuyacaq
"""for x in f:
    print(x)#Dovr vasitesile butun fayli oxumaq"""
"""print(f.readline())
f.close()

f=open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()#Faylin acilmasi,melumatin daxil edilmesi,fayldan cixmaq
#Open and Read the file after appending
f=open("demofile.txt","r")#Acilmis fayli oxumaq
print(f.read())
f=open("Myfile.txt","x")
print(f.read())#Bu adda fayl olmadigi ucun error verecek"""
"""f=open("Myfile.txt","w")
print(f.read())"""
"""import os
os.remove("Myfile.txt")#Daxil edilen addaki fayli silir"""
"""import os
if os.path.exists("demofile.txt"):#Bu adda faylin olub olmamasini yoxluyur
    os.remove("demofile.txt")#bu adda fayl varsa onu silir
    print("demofile.txt adinda fayl silindi")
else:
    print("Bu adda fayl movcud deyildir")#Bu adda fayl yoxdusa User bunu bildirir"""
"""import os
os.rmdir("data.txt")#bu adda fayli silir."""