import random
lists = []
print("Rolling the dice...")
for i in range(2):
    lists.append(random.randint(1, 6))
for i in range(1, 3):
    print("Die {}:".format(i), lists[i - 1])

print("Total Value:", sum(lists))
