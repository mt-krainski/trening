#!/usr/bin/env python

print(f"Hej {input('Podaj imie: ')}!")
wiek = float(input('Podaj wiek: '))

print(wiek)

if round(wiek) == wiek:
    print("Podałeś liczbę całkowitą!")
else:
    print("Podałeś liczbę niecałkowitą!")

def nowy_feature():
    print("to jest nowy feature")


def kolejna_modyfikacja():
    print ('to jest jeszcze jedna modyfikacja')