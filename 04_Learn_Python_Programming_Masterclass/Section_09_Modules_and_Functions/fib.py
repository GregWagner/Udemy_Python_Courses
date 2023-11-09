def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fast_fib(n):
    if n < 2:
        return n
    n_minus1 = 1
    n_minus2 = 0
    for f in range(1, n):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
    return result

for i in range(36):
    print(i, fast_fib(i))
