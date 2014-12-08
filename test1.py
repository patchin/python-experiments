import time

__author__ = 'patrickchin'

t0 = time.time()
count = 10**5
nums = []
for i in range(count):
    nums.append(i)
nums.reverse()
t1 = time.time()
total = t1 - t0
print("Code 1:")
print(total)

t0 = time.time()
nums = []
for i in range(count):
    nums.insert(0,i)
t1 = time.time()
total = t1 - t0
print("Code 2:")
print(total)

letters = "helloworld"
[x for x in letters]