import numpy as np
import matplotlib.pyplot as plt

# Part 1: Import matplotlib and numpy libraries
# (Already done with import statements above)

# Part 2: Import pyplot library from matplotlib
# (Already done with the import statement: `import matplotlib.pyplot as plt`)

# Part 3: Plot sine and cosine waveforms in the same plot. Add labels and title.
x = np.linspace(0, 2 * np.pi, 1000)  # Generate 1000 points between 0 and 2*pi
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label='Sine Wave', color='blue')
plt.plot(x, y_cos, label='Cosine Wave', color='red')

plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Sine and Cosine Waveforms')
plt.legend()  # Show the legend to distinguish sine and cosine waves
plt.grid(True)
plt.show()

# Part 4: Define two lists for bar plot, pie chart, and histogram
langs = ['C', 'C++', 'Java', 'Python', 'Oracle']
students = [23, 17, 35, 29, 12]

# Bar Plot
plt.bar(langs, students, color='skyblue')
plt.xlabel('Programming Languages')
plt.ylabel('Number of Students')
plt.title('Students per Programming Language')
plt.show()

# Pie Chart
plt.pie(students, labels=langs, autopct='%1.1f%%', colors=['blue', 'green', 'red', 'orange', 'purple'])
plt.title('Students Distribution by Language')
plt.show()

# Histogram
# Generating some data based on the students list for a histogram
# This is just an example, as we are not directly plotting the `students` list as histogram data
np.random.seed(0)
data = np.random.choice(students, size=100, replace=True)

plt.hist(data, bins=10, color='lightcoral', edgecolor='black')
plt.title('Histogram of Students Data')
plt.xlabel('Number of Students')
plt.ylabel('Frequency')
plt.show()
