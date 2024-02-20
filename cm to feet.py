# CODE FOR CONVERTING CENTIMETER TO FEET
def cm_to_feet(cm):
    # 1 cm is approx 0.0328084 feet
    feet = cm * 0.0328084
    return feet
centimeters = float(input("Enter length in centimeters: "))
feet = cm_to_feet(centimeters)
print(f"{centimeters} centimeters is equal to {feet} feet.")


#SAME CODE WITH TKINTER 

import tkinter as tk

def cm_to_feet():
    try:
        centimeters = float(entry.get())
        feet = centimeters * 0.0328084
        result_label.config(text=f"{centimeters} centimeters is equal to {feet:.2f} feet.")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

window = tk.Tk()
window.title("Centimeter to Feet Converter")
label = tk.Label(window, text="Enter length in centimeters:")
label.pack(pady=10)
entry = tk.Entry(window)
entry.pack(pady=10)
convert_button = tk.Button(window, text="Convert", command=cm_to_feet)
convert_button.pack(pady=10)
result_label = tk.Label(window, text="")
result_label.pack(pady=10)
window.mainloop()
