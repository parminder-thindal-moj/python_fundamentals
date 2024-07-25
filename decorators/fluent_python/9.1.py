def deco(func):
    def inner():
        print("runner inner()")
    return inner

@deco
def target():
    print("running target")
    
target()
target

