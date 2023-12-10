## Using decorators with1 argument


def shulk_says(func):
    """Print a msg that Shulk says"""

    def wrapper(msg):
        print("Shulk:", end=" ")
        func(msg)

    return wrapper


@shulk_says
def print_msg(msg):
    print(msg)


msg_1 = "Monado Buster!"
msg_2 = "I'm really feeling it!"
msg_3 = "This is the power of the Monado!"
msg_4 = "You're not invincible... Monado Enchant!"

print_msg(msg_1)
print_msg(msg_2)
print_msg(msg_3)
print_msg(msg_4)
