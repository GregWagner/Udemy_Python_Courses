text = input("Enter some text: ")

vowels = frozenset("aeiou")
print(sorted(set(text) - vowels))
