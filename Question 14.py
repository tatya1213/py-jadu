import pandas as pd

# Part 1: Create a dictionary with roll number, name of student, and attendance
data = {
    "Roll Number": ["RN1", "RN2", "RN3", "RN4", "RN5"],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Attendance": [85, 90, 88, 92, 95]
}

# Part 2: Convert the dictionary into a DataFrame, with index as RN1, RN2, RN3, RN4, RN5
df = pd.DataFrame(data)
df.set_index("Roll Number", inplace=True)
print("DataFrame with Roll Number as Index:")
print(df)

# Part 3: Use .loc function to extract one or more specified rows
# Extract one row (for example, RN3)
print("\nExtracted Row for RN3:")
print(df.loc["RN3"])

# Extract multiple rows (for example, RN1, RN2, RN4)
print("\nExtracted Rows for RN1, RN2, RN4:")
print(df.loc[["RN1", "RN2", "RN4"]])

# Part 4: Read a CSV file and perform few operations
# Assuming the CSV file 'students.csv' has the columns: Roll Number, Name, and Attendance
# You can replace the file name with the actual file path
csv_file_path = "students.csv"
csv_df = pd.read_csv(csv_file_path)

# Display the first 5 rows of the DataFrame
print("\nFirst 5 rows of CSV file:")
print(csv_df.head())

# Perform an operation: Get students with attendance greater than 90
high_attendance = csv_df[csv_df["Attendance"] > 90]
print("\nStudents with attendance greater than 90:")
print(high_attendance)
