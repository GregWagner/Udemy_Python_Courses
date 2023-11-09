parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]
parrot_list.append("A Norwegian Blue")

for state in parrot_list:
    print(f"This parrot is {state}")

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd

numbers_in_order = sorted(numbers)
print(numbers_in_order)

print(numbers)
print(numbers.sort())
print(numbers)

another_even = even
another_even.sort(reverse=True)
print(another_even)
print(even)
