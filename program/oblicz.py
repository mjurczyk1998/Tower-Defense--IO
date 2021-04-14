#!/usr/bin/python3

# autor: Maciej Jurczyk
import pathlib
import time
import sys
import os

err_log = open("out/err_info_oblicz.txt", "a")
wyjscie = open("out/wyjscie.txt", "w")
try:
    dane = open("in/dane.txt", "r")
except FileExistsError as err:
    print("Plik dane.txt nie istnieje.")
    err_log.write(str(err) + "\n")
max_n = 50000
max_m = 1000000
towers = []
test = True
r = 0

try:
    print("  Zczytywanie pliku...")
    time.sleep(0.75)
    text = (dane.readline()).split()
    n = int(text[0])  # liczba miast
    m = int(text[1])  # liczba dróg w państwie
    k = int(text[2])  # maksymalna liczba strażnic
    c = 0
    edges = [0] * (max_m+1)
    already_safed = [0] * max_m
    neighbour = [0] * max_m
    neighbour2 = [0] * max_m

    # zczytywanie danych i tworzenie tablic
    for i in range(m):
        tekst = dane.readline()
        if tekst == "":
            print("\nBlad danych! Nie mozna wykonac obliczen.")
            wyjscie.write("\nBlad danych! Nie mozna wykonac obliczen.")
            err_log.write("Blad danych! Nie mozna wykonac obliczen.\n")
            sys.exit()
        text = tekst.split()
        c += 1
        neighbour[c] = int(text[1])
        neighbour2[c] = edges[int(text[0])]
        edges[int(text[0])] = c
        c += 1
        neighbour[c] = int(text[0])
        neighbour2[c] = edges[int(text[1])]
        edges[int(text[1])] = c

    # główny algorytm rozmieszczania strażnic
    print("  Obliczam...")
    time.sleep(0.5)
    for i in range(1, n+1):
        if not already_safed[i]:
            r += 1
            towers.append(i)
            j = edges[i]
            while not j == 0:
                already_safed[neighbour[j]] = True
                k = edges[neighbour[j]]
                while not k == 0:
                    already_safed[neighbour[k]] = True
                    k = neighbour2[k]
                j = neighbour2[j]

    print("  Wynik:")
    print("  " + str(r), end="\n  ")
    wyjscie.write(str(r) + "\n")

    for i in range(r):
        wyjscie.write(str(towers[i]) + " ")
        print(str(towers[i]), end=" ")
    print()

except Exception as err:
    print("Blad krytyczny. Program przerwany. Po więcej informacji zerknij do err_info_oblicz.txt.")
    err_log.write(str(err) + "\n")
err_log.close()
wyjscie.close()
dane.close()


# ====================================== RAPORT ==============================================
print("  Tworze raport...")
time.sleep(0.75)

raport = open('out/raport.html', 'w')
wyjscie = open("out/wyjscie.txt", "r")
err_log = open('out/err_info_oblicz.txt', 'r')
dane = open("in/dane.txt", "r")
try:
    err_log_wejscie = open('out/err_info_dane_wejscie.txt', 'r')
except FileExistsError as err:
    print("Plik err_info_dane_wejscie.txt nie istnieje.")
    err_log.write(str(err) + "\n")
    raport.close()
    wyjscie.close()
    err_log.close()
    sys.exit()

raport.write("<!DOCTYPE html>\n<html>\n<head>\n<title>\nRaport dzialania programu\n</title>\n</head>\n"
             "<body>\n<h1 style=\"color: SlateBlue;\">Raport</h1>\n")
raport.write("<h3>Wyniki:</h3>\n")
a = "Dla danych wejsciowych:".ljust(30) + "poprawnym wynikiem jest:\n\n"
raport.write("<pre>" + a)
i = 0
for line in dane:
    i += 1
    a = line.ljust(30)
    if i == 1 or i == 2:
        a += wyjscie.readline()
    a = a.replace("\n", "")
    raport.write(a+"\n")
raport.write("\n\n</pre>")

raport.write("<h3>Bledy napotkane przy pracy, od ostatniego pelnego uruchomienia programu :</h3>\n<p>\n")
for line in err_log_wejscie:
    raport.write(line + "\n<br>")
raport.write("</p>\n<p>\n")
for line in err_log:
    raport.write(line + "\n<br> ")
raport.write("</p>\n\n\n")

raport.write("</body>\n</html>")
raport.close()
dane.close()
wyjscie.close()

print("  Otwieram raport.")
time.sleep(0.5)
os.system("out\\raport.html")
