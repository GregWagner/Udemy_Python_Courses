def celsius_to_fahrenheit(temp):
    return temp * 9/5 + 32

temperatures = [10, -20, 100]
for temp in temperatures:
    print(celsius_to_fahrenheit(temp))
