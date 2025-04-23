# Part 1
d = {"name": "John", "age": 20}
print(d)

# Part 2
students = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(students)

# Part 3
print(students["Bob"])

# Part 4
import pandas as pd
df = pd.DataFrame(list(students.items()), columns=["Name", "Marks"])
print(df)

# Part 5
print(df.loc[0])
print(df.iloc[1])
