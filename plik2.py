def kalkulator(a, b, operacja):
    if operacja == "+":
        return a + b
    elif operacja == "-":
        return a - b
    elif operacja == "*":
        return a * b
    elif operacja == "/":
        return a / b if b != 0 else "Nie można dzielić przez zero!"
    else:
        return "Nieznana operacja!"

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
operacja = input("Wybierz operację (+, -, *, /): ")

wynik = kalkulator(a, b, operacja)
print(f"Wynik: {wynik}")

