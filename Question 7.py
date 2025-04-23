# Part 1
s1 = {1, 2, 3}
print(s1)

# Part 2
s2 = {1, 2, 3}
s2.add(4)
print(s2)

# Part 3
s3 = {1, 2, 3, 4, 4, 5, 5}
print(s3)
print(type(s3))

# Part 4
s3.update(["apple", "banana"])
print(s3)

# Part 5
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
