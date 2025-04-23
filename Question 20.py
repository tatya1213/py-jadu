import tkinter as tk

# Function to display the greeting message
def greet():
    name = name_entry.get()  # Get the name entered by the user
    greeting_label.config(text=f"Hello, {name}!")  # Update the label to show the greeting

# Create the main window
root = tk.Tk()
root.title("Greeting Application")

# Create and pack the label for instructions
instruction_label = tk.Label(root, text="Enter your name:")
instruction_label.pack(pady=10)

# Create and pack the entry widget for input
name_entry = tk.Entry(root)
name_entry.pack(pady=10)

# Create and pack the button to trigger the greeting
greet_button = tk.Button(root, text="Greet", command=greet)
greet_button.pack(pady=10)

# Create and pack the label to show the greeting message
greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=10)

# Run the application
root.mainloop()
