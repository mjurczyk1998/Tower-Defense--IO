#!/usr/bin/python3

import os
import pathlib

file = open("in/dane.txt", "w")
err_log = open("out/err_info_dane_wejscie.txt", "w")

print("  Bledne wprowadzenie danych skutkuje niemozliwoscia wykonania obliczen!")
print("  Podaj najpierw 3 liczby: lb miast, drog i straznic, a nastepnie polacznienia miedzy miastami.\n"
      "  Liczby przedzielaj spacjami:")
print()
try:
    while True:
        nmk = input("  ")
        txt = nmk.replace(" ", "")
        tab = nmk.split()
        m = tab[1]
        if txt.isnumeric() and len(txt) >= 3 and len(tab) == 3:  # czy podano dokładnie 3 liczby, z dowolną ilością spacji
            break
        print("Blad wprowadzanych danych. Wprowadz trzy liczby ponownie.")
        err_log.write(nmk + " -> Zly typ wprowadzanych danych lub ich niewlasciwa ilosc.\n")
    file.write(nmk + "\n")
    for i in range(int(m)):
        while True:
            line = input("  ")
            tkst = line.replace(" ", "")
            tabl = line.split()
            if tkst.isnumeric() and len(tkst) >= 2 and len(tabl) == 2:  # czy podano dokładnie 2 liczby, z dowolną ilością spacji
                file.write(line + "\n")
                break
            print("Blad wprowadzanych danych. Wprowadz dwie liczby ponownie.")
            err_log.write(line + " -> Zly typ wprowadzanych danych lub ich niewlasciwa ilosc.\n")
except Exception as err:
    print("Blad krytyczny. Program przerwany. Po więcej informacji zerknij do err_info_dane_wejscie.txt.")
    err_log.write(err + "\n")

f = open("out/err_info_oblicz.txt", "w")
f.close()
file.close()
err_log.close()
os.system('py oblicz.py')
