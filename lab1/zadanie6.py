# Zad. 6:

# Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz
# średnie spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu
# paliwa oraz o szacowanych kosztach podróży (cena paliwa 6.5 zł/l).

# A) Zmodyfikuj skrypt tak, aby długość przejechanej drogi była generowana losowo
# (liczba całkowita z zakresu ), a użytkownik podawał aktualną cenę paliwa za litr.

# B) Zmodyfikuj zadania 6 tak, aby wyświetlanie wyników wykorzystywało f-string.

import random

odległość_km = random.randint(1,500)

while True:
    try:
        cena_paliwa_litr = float(input("Podaj cenę paliwa za litr(zł): "))
        if cena_paliwa_litr <= 0 or cena_paliwa_litr is None: raise ValueError
        break
    except ValueError:
        print("Cena paliwa jest niepoprawna, spróbuj jeszcze raz!")

while True:
    try:
        średnia_spalania = float(input("Podaj średnią spalania (w litrach na 100 km): "))
        break
    except ValueError:
        print("Średnia spalania jest niepoprawna, spróbuj jeszcze raz!")

print()
zużycie_paliwa = średnia_spalania / 100 * odległość_km
print(f"Przewidywane zużycie paliwa na {odległość_km}km, wynosi: {zużycie_paliwa:.2f}l.")
print(f"Przewidywana cena paliwa na całą podróż wynosi:{(zużycie_paliwa * cena_paliwa_litr):.2f}zł.")

