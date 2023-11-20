
def colourful_pen(func):
    def wrapper(radius, color):
        print("Using", color, "pen!")
        func(radius)
    return wrapper

@colourful_pen
def draw_circle(radius):
    print("Drawing a circle with radius", radius)

draw_circle(5, "red")
