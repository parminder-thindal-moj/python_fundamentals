def factorial(n):
    """returns n!"""

    return 1 if n < 2 else n * factorial(n - 1)


factorial(42)

factorial.__doc__

type(factorial)

help(factorial)


fact = factorial

fact(5)

map(fact, range(10))
map(factorial, range(10))

list(map(fact, range(10)))
list(map(factorial, range(10)))

map.__doc__

help(map)
