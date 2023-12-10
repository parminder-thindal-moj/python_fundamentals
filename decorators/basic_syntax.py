def my_function():
    print("I am a function")


# Assign the function to the variable without (). We dont want to execute this function
description = my_function

# Accessing the function from the variable I assigned it to.
print(description())


def outer_function():
    """Assign a task to Student"""

    task = "Read Python Book chapter 3"

    def inner_function():
        print(task)

    # Executing the inner function
    return inner_function()


homework = outer_function()

# note inner function not available outside of the inner function
inner_function()


def msg_shulk():
    msg = "This is the power of the Monado!"
    print(msg)


msg_shulk()


def friendly_reminder(func):
    """Reminder for husband"""

    func()
    print("Don't forget to bring your wallet!")


def action():
    print("I am going to to the store to buy you something nice")


# calling the friend_reminder function with the action function used as an argument
friendly_reminder(action)


def print_shulk_msg(func):
    print("Shulk:", end=" ")
    func()


def msg():
    print("Monado Buster!")


print_shulk_msg(msg)
