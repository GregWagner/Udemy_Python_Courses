def fact_iter(n):
    """Calculate n! iteratively"""
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result

def fact(n):
    """Calculate n! recursively"""
    if n <= 1:
        return 1
    return n * fact(n - 1)

for i in range(130):
    print(i, fact(i))
