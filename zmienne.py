#!/usr/bin/env python

print(f"Hej {input('Podaj imie: ')}!")
wiek = float(input('Podaj wiek: '))

nowa_zmienna = 0

if wiek >= 18.0:
    print('Jesteś pełnoletni!')
    nowa_zmienna = 1
else:
    print('Jesteś niepełnoletni!')

print(wiek)

if round(wiek) == wiek:
    print("Podałeś liczbę całkowitą!")
else:
    print("Podałeś liczbę niecałkowitą!")

def nowy_feature():
    print("to jest nowy feature")
