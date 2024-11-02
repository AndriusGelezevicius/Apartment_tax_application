import tkinter as tk
from tkinter import font, ttk



# Main window
root = tk.Tk()
root.title("Apartment tax application")
root.geometry("300x500")

custom_font = font.Font(size=12, weight="bold")
label = tk.Label(root, text="Apartment tax application", font=custom_font)
label.pack(pady=30)

new_tax_button = ttk.Button(root, text="New tax", command="new_tax")
new_tax_button.pack(pady=20)

history_tax_button = ttk.Button(root, text="Previous taxes", command="history_tax")
history_tax_button.pack(pady=20)




root.mainloop()