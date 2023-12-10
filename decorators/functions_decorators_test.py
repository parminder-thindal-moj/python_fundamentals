def parent():
    print("Printing from the parent() function")

    # Inner Function
    def first_child():
        print("Printing from the first_child() function")

    # inner function
    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


first_child() # not defined, because it's an inner function
parent() # outer function


def parent(num):
    def first_child():
        return "Hi, I am Dunban"

    def second_child():
        return "My name is Fiora"

    if num == 1:
        return first_child
    else:
        return second_child

# first_child \ second_child are returning the functions - no parenthesis
# first_child() \ second_child() are calling the functions - parenthesis.
    
parent(1) # references the 1st inner function inside parent()
parent(2) # references the 2nd inner function inside parent()

first = parent(1) # returning a reference to the function without parenthesis
second = parent(2)

first()
second()



def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
say_whee()

from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)
say_whee()