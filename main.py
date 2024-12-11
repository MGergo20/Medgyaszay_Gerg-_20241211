import bevezetes, sorozat, autom, auto

nev, ev= bevezetes.autokbekeres()
bevezetes.nev_ev(nev, ev)

sorozat.masodik_feladat()
eredmeny=sorozat.egyjegyuek_szama()
print()
print(f"\t Egyjegyűek szama: {eredmeny} ")
sorozat.fajlba_kiir()


autok = autom.beolvas("auto.txt")
print("III/Flotta:")
print(f"Autók száma: {autom.flotta(autok)}.")

legfiatalabb_auto = autom.legfiatalabb(autok)
print("III/Legfiatalabb:")
print(f"A legfiatalabb autó: {legfiatalabb_auto.nev} ({legfiatalabb_auto.gyartasi_ev}).")

atlag_kor = autom.atlagos_kor(autok)
print("III/Átlag kor:")
print(f"Az autók átlagos kora: {atlag_kor:.2f} év.")

