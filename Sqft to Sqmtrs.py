# CODE FOR CONVERTING SQFT TO SQMTRS

def sqft_to_sqm(sqft):
    sqm = sqft * 0.092903
    return sqm
sqft_value = 100  
sqm_result = sqft_to_sqm(sqft_value)
print(f"{sqft_value} square feet is equal to {sqm_result:.2f} square meters.")

#SAME CODE WITH TKINTER 

import tkinter as tk

def sqft_to_sqm_gui():
    try:
        sqft_value = float(entry_sqft.get())
        sqm_result = sqft_value * 0.092903
        result_label.config(text=f"{sqft_value} sqft is equal to {sqm_result:.2f} sqm.")
    except ValueError:
        result_label.config(text="Please enter a valid numeric value.")
window = tk.Tk()
window.title("Square Feet to Square Meters Converter")
label_sqft = tk.Label(window, text="Enter Square Feet:")
label_sqft.pack(pady=10)
entry_sqft = tk.Entry(window)
entry_sqft.pack(pady=10)
convert_button = tk.Button(window, text="Convert", command=sqft_to_sqm_gui)
convert_button.pack(pady=10)
result_label = tk.Label(window, text="")
result_label.pack(pady=10)
window.mainloop()

