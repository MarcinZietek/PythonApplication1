
file1 = open("dane_uzytkownika.txt", "w", encoding = "utf-8")

while True:
    name = input("Podaj imie: ")
    surname = input("Podaj nazwisko: ")
    age = input("Podaj wiek: ")

    print("Wprowadzone dane: ",name,surname,age)

    verification = input("Czy zatwierdzic? (t/n)")

    if verification == "t":
        print("Imie: " + name + "\n")
        print("Nazwisko: " + surname + "\n")
        print("Wiek: " + age + "\n")
    else:
        print("Anulowano!\n")

    nextData = input("Czy zakonczyc wyswietlanie danych uzytkownika? (t/n)")
    if nextData != "n":
        break







