file = open("numbers.txt", "w")
numbers = [1, 2, 3]
for num in numbers:
    file.write(str(num) + '\n')
file.close()
