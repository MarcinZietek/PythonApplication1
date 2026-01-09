file1 = open("raw.txt", "r", encoding = "utf-8")
file2 = open("new_raw.txt", "w", encoding = "utf-8")

for line in file1:  
    print("Plik z pustymi liniami", line)
    if line.strip():
       file2.write(line)

file1.close()
file2.close()
print("Usunieto puste linie w pliku")

file2 = open("new_raw.txt", "r", encoding = "utf-8")
for line1 in file2:
    print("Plik bez pustych linii ", line1)  

file2.close()




