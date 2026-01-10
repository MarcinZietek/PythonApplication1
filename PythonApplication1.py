
file1 = open("dane_uzytkownika.txt", "w", encoding = "utf-8")

while True:
    name = input("Podaj imie: ")
    surname = input("Podaj nazwisko: ")
    age = input("Podaj wiek: ")

    print("Wprowadzone dane: ",name,surname,age)

    verification = input("Czy zatwierdzic? (t/n)")

    if verification == "t":
        file1.write("Imie: " + name + "\n")
        file1.write("Nazwisko: " + surname + "\n")
        file1.write("Wiek: " + age + "\n")
        print("Dane zostaly zapisane do pliku\n")
    else:
        print("Anulowano!\n")

    nextData = input("Czy dodac kolejnego uzytkownika? (t/n)")
    if nextData != "t":
        break

file1.close()






