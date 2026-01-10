
print("KALKULATOR")
print("1 - dodawanie")
print("2 - odejmowanie")
print("3 - mnozenie")
print("4 - dzielenie")
while True:
    operation = input("Wybierz dzialanie (1-4)")
    a = float(input("Podaj pierwsza liczbe: "))
    b = float(input("Podaj druga liczbe: "))
  
    verification = input("Czy zatwierdzic? (t/n)")
    calculation = 0

    if verification == "t":
        print("Pierwsza liczba: ", a, "\n")
        print("Druga liczba: ", b, "\n")
        if operation == "1":
            calculation = a + b 
            print("Wynik: ", calculation)
        elif operation == "2":
            calculation = a - b
            print("Wynik: ", calculation)
        elif operation == "3":
            calculation = a * b
            print("Wynik: ", calculation)
        elif operation == "4":
            calculation = a / b
            print("Wynik: ", calculation)
        else:
            print("Anulowano!\n")
       
    nextData = input("Czy wykonac kolejne dzialanie? (t/n)")
    if nextData != "t":
        break







