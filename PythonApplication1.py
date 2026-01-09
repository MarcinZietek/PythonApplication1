sum = 0

file1 = open("numbers.txt", "r", encoding = "utf-8")
file2 = open("pusty_numbers.txt", "w", encoding = "utf-8")

for line in file1:
    file2.write(line)   
    print("Liczby", line)
  
file1.close()
file2.close()

print("Plik skopiowany")

