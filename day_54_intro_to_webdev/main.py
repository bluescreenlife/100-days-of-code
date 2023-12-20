'''Function timer using decorator functions.'''
import time

def speed_calc_decorator(function_to_time):
    def wrapper_function():
        start_time = time.time()
        function_to_time()
        end_time = time.time()
        print(f"{function_to_time.__name__} completed in {end_time - start_time} seconds.")
    return wrapper_function

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i

@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()
slow_function()