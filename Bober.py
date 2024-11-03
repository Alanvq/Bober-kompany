nums = [0, 1000, 2430, 3312, 500, 5023,21321, 5321, 53023, 123021, 231333, 231]
print("Годовой доход ООО БОБЁР:")
print("Доход Компании:")
print(sum(nums))
print("Налог Компании:")
print(sum(nums)*0.08)

class Car:
    colors = ['black', 'violet']
    wheels_count = 4

bmw = Car()
audi = Car()

print(bmw.colors)
print(bmw.wheels_count)

bmw.colors = "white"
bmw.speed = 300

# bmw = Car()
# print(bmw)
# print(hex(id(bmw)))

# print(type(bmw))

print("class", Car.__dict__)
print("bmw", bmw.__dict__)
print("audi", audi.__dict__)
