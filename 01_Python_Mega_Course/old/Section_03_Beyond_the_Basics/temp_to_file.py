temperatures = [10, -20, -289, 100]

def c_to_f(c):
    if c < -274.15:
        return "The temperature doesn't make sense!"
    f = c * 9/5 + 32
    return f

with open("temps.txt", "w") as temp_file:
    for t in temperatures:
        f = c_to_f(t)
        if type(f) == float:
            temp_file.write(str(f) + '\n')
