def cache_decorator(function):
    mem_cache = {}
    
    def cached_fucntion(argument):
        if argument in mem_cache:
            return mem_cache[argument]
        else:
            mem_cache[argument] = function(argument)
            return mem_cache[argument]
    
    return cached_fucntion
@cache_decorator
def fib(n):
     if n == 0:
        return 1
     if n == 1:
        return 1
     return fib(n-1) + fib(n-2)
from my_python_functions.fib_functions.my_function import fib