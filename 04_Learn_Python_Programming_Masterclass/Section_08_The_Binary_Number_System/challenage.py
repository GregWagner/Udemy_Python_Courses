num = int(input('Enter a decimal number: '))

for power in [2 ** x for x in range(15)[::-1]]:
    printing = False
    bit = num // power
    if bit != 0 or power == 1:
        print(bit, end='')
    num %= power
print()
