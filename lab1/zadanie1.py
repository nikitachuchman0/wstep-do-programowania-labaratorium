# A) Sprawdź w interpreterze typ wyników określonych działań - type( x ) i wyjaśnij, co
# oznaczają poszczególne operatory?

# 1.
1 + 2
# <class 'int'>; dodawanie

# 2.
1 + 4.5
# <class 'float'>; dodawanie

# 3.
3 / 2
# <class 'float'>; dzielenie zmiennoprzecinkowe

# 4.
4 / 2
# <class 'float'>; dzielenie zmiennoprzecinkowe

# 5.
3 // 2
# <class 'int'>; dzielenie całkowite

# 6.
-3 // 2
# <class 'int'>; dzielenie całkowite

# 7.
11 % 2
# <class 'int'>; reszta z dzielenia

# 8.
2 ** 10
# <class 'int'>; potęgowanie

# 9.
8 ** (1/3)
# <class 'float'>; potęgowanie z dzieleniem zmiennoprzecinkowym

# B) Sprawdź i wyjaśnij działanie następujących instrukcji:

# 1.
int(3.0)
# konwersja liczby typu float na typ int. Odrzuca część ułamkową.

# 2.
float(3)
# konwersja liczby typu int na typ float. Dodaje część ułamkową.

# 3.
float("3")
# konwersja ciągu znaków typu str na typ float. Dodaje część ułamkową.

# 4.
str(12.4)
# konwersja liczby typu float na typ str. Liczba jest interpretowana jako ciąg znaków.
# 5.
bool(0)
# konwersja liczby typu int na typ bool. Liczba jest interpretowana jako wartość logiczna.

# We wszystkich przykładach jest używana konwersja typów