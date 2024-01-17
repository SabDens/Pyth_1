import random

# print(random.random())
# print(random.randint(1,100))
# print(random.choice("123123123"))
# print(random.randrange(0,100,3))
# rand = random.randint(0,5)
# chisl = int(input(":"))
# while chisl != rand:
#     chisl = int(input(":"))

start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))
number = int(input("Введіть число: "))

for i in range(start, end + 1):
    if i == number:
        print(f"!{i}!", end=' ')
    else:
        print(i, end=' ')