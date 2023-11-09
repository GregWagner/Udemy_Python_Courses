age = 24
print("My age is " + str(age) + " years")

# Replacement field
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, 
    "January", "March", "May", "July", "August", "October", "Decemer"))

print("""January: {2}
Feburary: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: 
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

# Depriciated
print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))
print("PI is approximentaly %12.5f" % (22 / 7))

for i in range(1, 12):
    print("# %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))
# above with non-depricated
for i in range(1, 12):
    print("# {0:2} squared is {1:<4} and cubes is {2:<4}".format(i, i ** 2, i **
        3))
