import random

for i in range(10):
    s = random.sample(range(1, 21), 4)
    s.sort()
    print(s)
