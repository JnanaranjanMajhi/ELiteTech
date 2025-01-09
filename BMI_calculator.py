import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    # Calculate BMI (BMI = weight (kg) / height (m)^2)
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    # Interpret the BMI result based on standard BMI categories
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def on_calculate_click():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Please enter valid positive values for weight and height.")
            return
        bmi = calculate_bmi(weight, height)
        interpretation = interpret_bmi(bmi)
        result_label.config(text=f"Your BMI is: {bmi:.2f}\nInterpretation: {interpretation}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numerical values for weight and height.")

def on_clear_click():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create widgets
weight_label = tk.Label(root, text="Enter your weight in kilograms:")
weight_entry = tk.Entry(root)
height_label = tk.Label(root, text="Enter your height in meters:")
height_entry = tk.Entry(root)
calculate_button = tk.Button(root, text="Calculate BMI", command=on_calculate_click)
clear_button = tk.Button(root, text="Clear", command=on_clear_click)
result_label = tk.Label(root, text="", font=("Helvetica", 14))

# Layout the widgets
weight_label.grid(row=0, column=0, padx=10, pady=5)
weight_entry.grid(row=0, column=1, padx=10, pady=5)
height_label.grid(row=1, column=0, padx=10, pady=5)
height_entry.grid(row=1, column=1, padx=10, pady=5)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)
clear_button.grid(row=3, column=0, columnspan=2, pady=10)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
