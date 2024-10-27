from collections import deque

 # Стек - LIRFO последний зашел, первый вышел
 # Очень - LIRFO первый зашел, первый вышел

d = deque()
d.append(1)
d.append(2)
d.appendleft(0)
d.appendleft(-1)
print(d)
  
print(d.pop())
print(d.pop())
print(d)

d.extend([8, 8, 8])
d.extendleft([1, 1, 1])

print(d)

d.clear()
print(d)
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)

print(f"Стек после добавления элементов - {stack}")

print(f"удаляем элемент - {stack.pop}")

print(stack)

def validate(s):
    # Создаем словарь на основе deque() для эффективности
    stack = deque()
    # Coздаем словарь ключ значение с скобками для отслеживания правильности
    br = {")": "(", "]": "[", "}": "{"}
    # перебираем каждую скобку из "s"
    for char in s:
        # создаем цикл для проверки
        if char in br.values():
            # добавляем в стэк в конец
            stack.append(char)
            # если скобка являеться закрывающей
        elif char in br.keys():
            # если стак пустой или скобка не правильная по отношению к последней в стеке
            if not stack or stack.pop() != br[char]:
                return False

    # Если стек пустой после проверки возвращаем True   
    return not stack

print(validate("({[]})"))
print(validate("({[})"))
