list_of_numbers = [1, 2, 3, 4, 5, 6, 7]
list_iterator = iter(list_of_numbers)

for i in range(len(list_of_numbers)):
    print(next(list_iterator))
