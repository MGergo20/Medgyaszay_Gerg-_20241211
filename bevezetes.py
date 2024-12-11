def autokbekeres():
    nev:str=str(input("Autó neve: "))
    ev:int= int(input("Gyártási dátum: "))
    return nev, ev

def nev_ev(nev, ev):
    if ev == 2024:
        print(f"Ez az {nev} friss gyártás.")
    elif ev < 2000:
        print(f"Ez az {nev} öreg autó.")
    else:
        print(f"Ez az {nev} átlagos korú.")