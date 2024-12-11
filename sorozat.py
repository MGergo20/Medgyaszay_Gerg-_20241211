import random

szam_lista = []
index = 0
while index < 5:
    vszam = random.randint(1,90)
    szam_lista.append(vszam)
    index += 1

def masodik_feladat():
    print("II/A, B, C: ")
    index = 0
    while index < len(szam_lista):
        if index < 4:
            print(f"\t{szam_lista[index]}",end=";")
        else:
            print(f"{szam_lista[index]}",end="")
        index += 1

def egyjegyuek_szama():
    print("\nII/D,E")
    index = 0
    eredmeny = 0
    while index < len(szam_lista):
        if szam_lista[index] < 10:
            eredmeny += 1
        index += 1
    return eredmeny

           
def fajlba_kiir():
    f = open("szamok.txt","w",encoding="utf-8")
    f.write("II/F\n")
    f.write(f"\t Egyjegyűek szama: {egyjegyuek_szama()} ")
    f.close()

def konzolra_kiir():
    print("\n II/E,F:\n\t",egyjegyuek_szama()) 