def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n.
       https://docs.python.org/3/tutorial/controlflow.html#defining-functions"""
       
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(fib2(1000000))