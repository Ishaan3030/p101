import random

response = int('press y to roll again and n to exit:')

while response == "y":
    no = random.randint(1,6)

if response == "n":
    print(no)
print()