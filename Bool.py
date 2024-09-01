x = bool("hello") 
print(x) 
 
x = bool([]) 
print(x) 
 
def sum(a, b): 
    print(a + b) 
sum(744, 744) 
 
m_list = 1 
 
if m_list: 
     print("вкантакте") 
 
list_1 = (1, 0, 0) 
 
print(any(list_1)) 
 
list_2 = [1, 2, 0] 
print(all(list_2)) 
 
x1 = 5 
 
while x1 > 0: 
    print(x1) 
    x1 -= 1 
 
# while 1: 
#    name = input("Введите вкантакте: ") 
     
#    if len(name) > 3: 
#        break 
   
#    x1 = 20 
#    while x1: 
#      print("*" * x1) 
#      x1 -= 1 
 
x2 = 1 
 
while x2: 
    print('*' * x2) 
    x2 += 2 
    if x2 > 20: 
 
        break 
 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
 
numbers2 = [] 
for i in numbers: 
    numbers2.append(i ** 2) 
 
print(numbers) 
print(numbers2) 
 
numbers2 = [x**2 for x in numbers] 
 
numbers2 = [x for x in numbers if x % 2 == 0] 
 
 
print(numbers2) 
 
#  numbers3 = [1, 3, 5, 7, 9] 
 
numbers3 = [x+1000 for x in numbers if x  % 2 == 1] 
 
print(numbers3) 
 
str_list = ['python', 'hi', 'hello', 'world', 'python', 'hi', 'hello', 'world'] 
 
numbers2 = [x.upper() + '!' for x in str_list if len(x) >= 3] 
 
print(numbers2) 
       
 
print(numbers2)
