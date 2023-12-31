parrot: str = "Norwegian Blue"
print(parrot)
print(parrot[0])
print(parrot[3])

# index from the end
print(parrot[-1])

# slice
print(parrot[0: 6])
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:-2])
print(parrot[0:6:2])

number: str = "9,233,372,036,854,775,807"
print(number[1::4])         #,,,,,,

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])        # 123456789

string1: str = "he's "
string2: str = "probably "
print(string1 + string2)    # he's probably

print("Hello" * 5)

today: str = "friday"
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in "fjord")
