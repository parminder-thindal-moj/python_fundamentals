import pandas as pd
from pathlib import Path

import tracemalloc
import os


def measure_memory_usage(func):
   """Decorator to record memory usage."""

   def wrapper(self, *args, **kwargs):
       tracemalloc.start()

       # Call the original function
       result = func(self, *args, **kwargs)

       current, peak = tracemalloc.get_traced_memory()

       tracemalloc.stop()

       print(f"Memory usage of {func.__name__}:")
       print(f"Current memory usage is {current}KB; Peak was {peak}KB")
       
       my_dict = {"result": result,
                  "current": current,
                  "peak": peak}
       
       # Return the result and memory usage
       return my_dict

   return wrapper

def set_memory_attributes(func):
   """Decorator to set memory attributes."""

   def wrapper(self, *args, **kwargs):
       result, current, peak = func(self, *args, **kwargs)

       self.current_memory = current
       self.peak_memory = peak

       return result

   return wrapper


class Memory_usage:
   def __init__(self):
       self.current_memory = None
       self.peak_memory = None

   @measure_memory_usage
   def say_hello(self):
       msg = "hello"
       return msg
   
   def set_current_memory(self, num):
       self.current_memory = num
   
   def set_peak_memory(self, num):
       self.peak_memory = num