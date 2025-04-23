# Part 1
t1 = (1, 1, 1)
t2 = (1, "apple", 3.14)
print(type(t1))
print(type(t2))

# Part 2
t = (10, 20, 30, 40, 50)
print(t[1])
print(t[-1])
print(t[1:4])

# Part 3
t3 = (1, 2, 3)
try:
    t3[0] = 10
except TypeError as e:
    print(e)

# Part 4
t4 = (4, 7, 1, 9)
print(len(t4))
print(min(t4))
print(max(t4))

# Part 5
l = [10, 20, 30]
t5 = tuple(l)
print(type(t5))
