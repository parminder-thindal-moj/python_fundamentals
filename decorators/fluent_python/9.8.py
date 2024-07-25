def make_averager():
    series = []
    
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    
    return averager

avg = make_averager()

avg(10)
avg(11)
avg(15)

# A closer is a function that retains the bindings of the free variables, that
# exists when the functio nsi define, so that they can be used later when
# the function is invokved and the defining scope is no longer available.

# inspecting the function created by make_averager
avg.__code__.co_varnames

avg.__code__.co_freevars

avg.__closure__

avg.__closure__[0].cell_contents