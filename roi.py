def outer():        
     n = 5           
 
     def inner():     
         nonlocal n
         n += 1        
         print(n)
 
     return inner
fn = outer()   
fn()    
fn()    
fn() 


def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"функция {func.__name__} вызвана: {count} раз")
        return func(*args, **kwargs)
    return inner

@counter
def sum(a, b):
    return a + b
    
    # print(sum(1, 5))
    # print(sum(1, 8))
    # print(sum(1, 4))
    # print(sum(1, 7))

a = counter(sum)
print(a(7, 1481))
print(a(6, 1482))
print(a(5, 1483))
print(a(1, 1487))

@counter
def div(c, k, l):
    return c // k + l
div(9, 3, 1476)
