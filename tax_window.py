import tkinter as tk
from datetime import date, datetime
from tkinter import font, ttk
from tkcalendar import Calendar
class newTax:
    def __init__(self, master):
        self.master = master
        self.new_tax_window = tk.Toplevel(master)  # Create Toplevel window linked to master
        self.new_tax_window.title("new Tax")
        self.new_tax_window.geometry("700x700")

        self.new_tax_window.bind("<Button-1>", self.close_calendar_if_open)
        self.create_widgets()
        self.calendar = None


    def show_today_date(self):
        today_date = datetime.today().strftime("%m/%d/%y")
        self.show_date_button.config(text=today_date)

    def open_calendar(self):
        self.calendar = Calendar(self.new_tax_window, selectmode="day", year=date.today().year, month=date.today().month, day=date.today().day)
        self.calendar.pack(pady=20)

        # Bind the selection event to update the date immediately
        self.calendar.bind("<<CalendarSelected>>", self.update_date)

    def update_date(self, event):
        # Get the selected date from the calendar
        selected_date = self.calendar.get_date()
        # Update the button text to the selected date
        self.show_date_button.config(text=selected_date)
    def close_calendar_if_open(self, event):
        # Destroy the calendar if it exists when clicking outside
        if self.calendar is not None:
            self.calendar.destroy()
            self.calendar = None  # Reset the calendar reference
    def create_widgets(self):

        custom_font = font.Font(size=12, weight="bold")
        label = tk.Label(self.new_tax_window, text="New tax application", font=custom_font)
        label.pack(pady=(20,10))

        date_frame = tk.Frame(self.new_tax_window)
        date_frame.pack(anchor="w", padx=20, pady=10)
        label_date = tk.Label(date_frame, text="Date: ")
        label_date.pack(side="left", padx=(0, 10))


        self.show_date_button = ttk.Button(date_frame, text="", command=self.open_calendar)
        self.show_date_button.pack(pady=10)
        self.show_today_date()
