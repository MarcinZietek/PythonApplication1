file = open("multiple_lines.txt", "r", encoding = "utf-8")
lines = file.readlines()
file.close()

print(len(lines))