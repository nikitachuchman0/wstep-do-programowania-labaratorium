# Zad. 5:
# Napisz skrypt, który pobiera długości boków prostokąta, a następnie oblicza jego pole i
# obwód oraz wyświetla wyniki na ekranie.

while True:
    try:
        bok_a = float(input("Podaj długość boku 'a':"))
        bok_b = float(input("Podaj długość boku 'b':"))
        break
    except ValueError:
        print("Jedna z wartości jest niepoprawna, spróbuj jeszcze raz!")

pole_prostokąta = bok_a * bok_b
obwód_prostokąta = 2 * (bok_a + bok_b)

print(f"Wartość pola prostokąta: {pole_prostokąta}\nWartość obwodu prostokąta: {obwód_prostokąta}")

# Wynik:
#
# Podaj długość boku 'a':12
# Podaj długość boku 'b':12
# Wartość pola prostokąta: 144.0
# Wartość obwodu prostokąta: 48.0
#
# Process finished with exit code 0
