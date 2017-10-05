#!/usr/bin/env python

print(f"Hej {input('Podaj imie: ')}!")
wiek = float(input('Podaj wiek: '))

if wiek >= 18.0:
    print('Jesteś pełnoletni!')
else:
    print('Jesteś niepełnoletni!')

print(wiek)

if round(wiek) == wiek:
    print("Podałeś liczbę całkowitą!")
else:
    print("Podałeś liczbę niecałkowitą!")
