import random


def greed():
    print("What is your name?")
    greed = input('> ')
    return greed


lists = []
greed = greed()
print("Hello, " + greed + "!")
print("Rolling the dice...")
for i in range(2):
    lists.append(random.randint(1, 6))
for i in range(1, 3):
    print("Die {}:".format(i), lists[i - 1])

print("Total Value:", sum(lists))

