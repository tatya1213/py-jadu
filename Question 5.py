# Lists
same = [1, 2, 3]
diff = [1, "hello", 3.5]
print(type(same), type(diff))
# Indexing
print(same[0])
# Negative Indexing
print(diff[-1])
# Slicing
print(diff[0:2])
# List operations
lst = [1, 2]
lst.append(3)
lst.extend([4, 5])
lst.sort()
lst.pop()
lst.remove(2)
print(lst)
# Mutable
lst[0] = 99
print(lst)
