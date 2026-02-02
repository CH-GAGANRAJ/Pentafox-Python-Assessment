import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        end=time.time()

        print(f'Function {func.__name__} took {end-start_time:.4f}')
        return res
    return wrapper
@time_it
def add_numbers(a, b):
    time.sleep(1) # Simulate a short delay
    return a + b
print(add_numbers(5,10))
