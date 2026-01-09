
list = ["W", "czasie", "suszy", "szosa", "sucha"]
file = open("lista_slow.txt", "w", encoding = "utf-8")

for word in list:
    file.write(word + "\n")
    print(word)
file.close()

print("Slowa zostaly zapisane")

