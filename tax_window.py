import tkinter as tk

class newTax:
    def __init__(self, master):
        self.master = master
        self.new_tax_window = tk.Toplevel(master)  # Create Toplevel window linked to master
        self.new_tax_window.title("new Tax")
        self.new_tax_window.geometry("700x700")

        self.create_widgets()

    def create_widgets(self):

        label = tk.Label(self.new_tax_window, text="This is a new window")
        label.pack(pady=20)