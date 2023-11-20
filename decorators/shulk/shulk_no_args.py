## Using decorators with 0 arguments

def shulk_says(func):
    '''Print a phrase that Shulk says'''
    
    def wrapper():
        print("Shulk:", end=' ')
        print(func())
    return wrapper
    
@shulk_says
def shulk_buster():
    msg = "Monado Buster!"
    return msg

shulk_buster()

@shulk_says
def shulk_eater():
    msg = "Monado Eater!"
    return msg
    
shulk_eater()