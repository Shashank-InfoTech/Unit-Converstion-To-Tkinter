# CODE FOR CONVERTING SQFT TO ACERS

def sqft_to_acres(sqft):
    acres = sqft / 43560
    return acres
sqft_value = 80000 
acres_result = sqft_to_acres(sqft_value)
print(f"{sqft_value} square feet is equal to {acres_result:.6f} acres.")

#SAME CODE WITH TKINTER 

import tkinter as tk

def sqft_to_acres_gui():
    try:
        sqft_value = float(entry_sqft.get())
        acres_result = sqft_value / 43560
        result_label.config(text=f"{sqft_value} sqft is equal to {acres_result:.6f} acres.")
    except ValueError:
        result_label.config(text="Please enter a valid numeric value.")
window = tk.Tk()
window.title("Square Feet to Acres Converter")
label_sqft = tk.Label(window, text="Enter Square Feet:")
label_sqft.pack(pady=10)
entry_sqft = tk.Entry(window)
entry_sqft.pack(pady=10)
convert_button = tk.Button(window, text="Convert", command=sqft_to_acres_gui)
convert_button.pack(pady=10)
result_label = tk.Label(window, text="")
result_label.pack(pady=10)
window.mainloop()

