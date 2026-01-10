text = input ("Podaj tekst: ")

vowel = "aeiouyAEIOUY"
vowelCounter = 0
consonantCounter = 0

for letter in text:
    if letter.isalpha():
        if letter in vowel:
            vowelCounter += 1
        else:
            consonantCounter += 1

print("Lczba samoglosek: ", vowelCounter,"\n")
print("Lczba spolglosek: ", consonantCounter,"\n")

