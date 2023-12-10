# Structure for adding arguments to decorators


def my_decorator_func(func):
    def wrapper_func(*args, **kwargs):
        # Do something before the function.
        func(*args, **kwargs)
        # Do something after the function.

    return wrapper_func


@my_decorator_func
def my_func(my_arg):
    """Example docstring for function"""

    pass


# decorators hide the function they are decorating.
print(my_func.__name__)
print(my_func.__doc__)

# Use functools wraps, which willl update the decorator with the decorator function attributes

from functools import wraps


def my_decorator_func(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper_func


@my_decorator_func
def my_func(my_args):
    """Example docstring for function"""
    pass


# decorators hide the function they are decorating.
print(my_func.__name__)
print(my_func.__doc__)
