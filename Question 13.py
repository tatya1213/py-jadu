import numpy as np

# Part 1: Create 1D, 2D numpy array and check its dimensions and type
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(f"1D Array: {array_1d}")
print(f"2D Array: {array_2d}")

print(f"1D Array Dimensions: {array_1d.ndim}, Type: {type(array_1d)}")
print(f"2D Array Dimensions: {array_2d.ndim}, Type: {type(array_2d)}")

# Part 2: Array indexing and slicing
print(f"Element at index 2 in 1D Array: {array_1d[2]}")
print(f"Sliced 1D Array (from index 1 to 4): {array_1d[1:4]}")
print(f"Sliced 2D Array (first row): {array_2d[0, :]}")
print(f"Sliced 2D Array (first column): {array_2d[:, 0]}")

# Part 3: Array addition, multiplication, and subtraction
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

add_result = array_a + array_b
mul_result = array_a * array_b
sub_result = array_a - array_b

print(f"Addition: {add_result}")
print(f"Multiplication: {mul_result}")
print(f"Subtraction: {sub_result}")

# Part 4: Get minimum, maximum value in the numpy array
min_val = np.min(array_2d)
max_val = np.max(array_2d)

print(f"Minimum Value in 2D Array: {min_val}")
print(f"Maximum Value in 2D Array: {max_val}")

# Part 5: Get sum of values and sort the array
sum_values = np.sum(array_1d)
sorted_array = np.sort(array_1d)

print(f"Sum of Values in 1D Array: {sum_values}")
print(f"Sorted Array: {sorted_array}")

# Part 6: Perform horizontal and vertical stacking
array_c = np.array([7, 8, 9])
h_stack = np.hstack((array_a, array_c))
v_stack = np.vstack((array_a, array_b))

print(f"Horizontal Stacking: {h_stack}")
print(f"Vertical Stacking: \n{v_stack}")
