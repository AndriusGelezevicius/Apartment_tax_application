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
        self.calendar = None # Kalendoriaus instancijos saugojimui


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
        if self.calendar:
            # Get calendar coords
            x1 = self.calendar.winfo_rootx()
            y1 = self.calendar.winfo_rooty()
            x2 = x1 + self.calendar.winfo_width()
            y2 = y1 + self.calendar.winfo_height()

            # PCheck if we push mouse button outside the calendar
            if not (x1 <= event.x_root <= x2 and y1 <= event.y_root <= y2):
                self.calendar.pack_forget()  # hide calendar
                self.calendar = None
                self.new_tax_window.unbind("<Button-1>")  # turn off mouse's button
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
