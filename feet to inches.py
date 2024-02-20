# CODE FOR CONVERTING FEET TO INCHES

def feet_to_inches(feet):
    inches = feet * 12
    return inches
feet_value = 5  
inches_result = feet_to_inches(feet_value)
print(f"{feet_value} feet is equal to {inches_result} inches.")

#SAME CODE WITH TKINTER 

import tkinter as tk

def feet_to_inches():
    try:
        feet_value = float(entry_feet.get())
        inches_result = feet_value * 12
        result_label.config(text=f"{feet_value} feet is equal to {inches_result} inches.")
    except ValueError:
        result_label.config(text="Please enter a valid numeric value.")

window = tk.Tk()
window.title("Feet to Inches Converter")
label_feet = tk.Label(window, text="Enter Feet:")
label_feet.pack(pady=10)
entry_feet = tk.Entry(window)
entry_feet.pack(pady=10)
convert_button = tk.Button(window, text="Convert", command=feet_to_inches)
convert_button.pack(pady=10)
result_label = tk.Label(window, text="")
result_label.pack(pady=10)
window.mainloop()

