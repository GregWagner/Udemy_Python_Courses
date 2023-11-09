file = open("fruits.txt")
fruits = file.read()
file.close()

for fruit in fruits.splitlines():
    print(len(fruit))
