# Part 1
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Part 2
marks = int(input("Enter your marks: "))
if marks >= 75:
    print("DISTINCTION")
elif marks >= 60:
    print("FIRST CLASS")
elif marks >= 50:
    print("SECOND CLASS")
elif marks >= 35:
    print("PASSED")
else:
    print("FAILED")
