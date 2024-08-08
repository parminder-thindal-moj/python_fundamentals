def make_averager():
    count = 0
    total = 0
    
    def averager(new_value):
        nonlocal count, total
        count += 1 # same as count = count + 1
        total += new_value
        return total / count
    
    return averager

avg = make_averager()

# This will error
avg(10)


