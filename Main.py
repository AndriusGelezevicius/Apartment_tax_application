import tkinter as tk
from tkinter import font, ttk
from tax_window import newTax

def history_tax():
    print("history_tax")

# Main window
root = tk.Tk()
root.title("Apartment tax application")
root.geometry("300x500")

image = tk.PhotoImage(file="C:/Users/PC/Desktop/Python/pythonProject/Apartment tax application/Images/taxes.png")

image_label = tk.Label(root, image=image)
image_label.pack(pady=30)

custom_font = font.Font(size=12, weight="bold")
label = tk.Label(root, text="Apartment tax application", font=custom_font)
label.pack(pady=10)

button_width = 20
new_tax_button = ttk.Button(root, text="New tax", command=lambda: newTax(root), width=button_width)
new_tax_button.pack(pady=20)

history_tax_button = ttk.Button(root, text="Previous taxes", command=history_tax, width=button_width)
history_tax_button.pack(pady=20)

developer_label = tk.Label(root, text="Developed by Andrius Geleževičius")
developer_label.pack(side="bottom", pady=10, anchor="s")



root.mainloop()