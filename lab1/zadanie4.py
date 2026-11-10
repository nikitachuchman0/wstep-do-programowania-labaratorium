# Zad. 4:

# Do zmiennej Cena przypisz cenę produktu równą 39.99 PLN oraz do zmiennej Rabat
# przypisz wartość 0.2 (rabat 20%). Następnie policz cenę tego produktu po zastosowaniu
# podanego rabatu. Wynik wydrukuj do konsoli. Zwróć uwagę na odpowiednie
# formatowanie tekstu w funkcji print() tak, aby końcowa cena produktu została
# wyświetlona tylko do drugiego miejsca po przecinku.

cena = 39.99
rabat = 0.2

wynik = cena * (1 - rabat)
print(f"Cena po rabacie: {wynik:.2f}PLN.")

# Resultat:
# Cena po rabacie: 31.99PLN.
#
# Process finished with exit code 0
