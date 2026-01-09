sum = 0

file = open("numbers.txt", "r", encoding = "utf-8")

for numbers in file:
    print("Liczby", numbers)
    number = int(numbers)
    sum += number
    
  
file.close()

print("Suma z liczb w pliku wynosi = " ,sum)

