#https://github.com/Stina0081
import tkinter as tk
from tkinter import messagebox

def calculate_print_price():
    try:
        print_time = float(print_time_entry.get())
        filament_weight = float(filament_weight_entry.get())
        filament_price_per_kg = float(filament_price_entry.get())

        filament_weight_grams = filament_weight * 1000

        filament_cost = (filament_weight_grams / 1000) * (filament_price_per_kg / 1000)

        print_time_cost = print_time / 60

        total_cost = filament_cost + print_time_cost

        messagebox.showinfo("Total Cost", f"The total cost is €{total_cost:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

window = tk.Tk()
window.title("3D Print Cost Calculator")

print_time_label = tk.Label(window, text="Print Time (minutes):")
print_time_entry = tk.Entry(window)

filament_weight_label = tk.Label(window, text="Filament Weight (kilograms):")
filament_weight_entry = tk.Entry(window)

filament_price_label = tk.Label(window, text="Filament Price per kg (€):")
filament_price_entry = tk.Entry(window)

calculate_button = tk.Button(window, text="Calculate", command=calculate_print_price)

print_time_label.grid(row=0, column=0, padx=5, pady=5)
print_time_entry.grid(row=0, column=1, padx=5, pady=5)

filament_weight_label.grid(row=1, column=0, padx=5, pady=5)
filament_weight_entry.grid(row=1, column=1, padx=5, pady=5)

filament_price_label.grid(row=2, column=0, padx=5, pady=5)
filament_price_entry.grid(row=2, column=1, padx=5, pady=5)

calculate_button.grid(row=3, columnspan=2, padx=5, pady=10)

window.mainloop()
