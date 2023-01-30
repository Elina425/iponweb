import time
add = lambda n:n+15

#print(add(3))

#task2
fib = lambda n:n if n<=1 else fib(n-1) + fib(n-2)
#print(fib(4))

#task3
rearrange = lambda list:list[::-1]
#print(rearrange([1,45,34,5]))

#task4
def print_time(func):
    def wrapper(*arg, **kwarg):
        start = time.time()
        result = func(*arg, **kwarg)
        end = time.time()
        print(f"{end - start} seconds")
        return result
    return wrapper

@print_time
def get_function(a,b,c):
    time.sleep(3)

#get_function(c=9,a=3, b=5)

def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1
x = count_up(3)
# print(next(x))
# print(next(x))
# print(next(x))

def even_numbers(n):
    i=0
    while True:
        if i%2 ==0:
            yield i
        i+=1
even = even_numbers(10)
# print(next(even))
# print(next(even))
# print(next(even))
def even_numbers(n):
    i=0
    while True:
        if i%2 ==0:
            yield i
        i+=1
even = even_numbers(10)
print(next(even))
print(next(even))
print(next(even))
print(next(even))
print(next(even))
print(next(even))
print(next(even))







