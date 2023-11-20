def hello_decorator(func):
    print(f'Decorator Init :: Begins for {func.__name__}')

    def wrapper(*args, **kwargs):
        print(f'Decorator execution :: Begins for {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Decorator execution :: Ends for {func.__name__}')
        return result

    print(f'Decorator Init :: Ends for {func.__name__}')
    return wrapper


@hello_decorator
def add(a, b):
    return a + b


if __name__ == '__main__':
    output1 = add(2, 2)
    print('Result:: ', output1)

    output2 = add(4, 2)
    print('Result:: ', output2)
    