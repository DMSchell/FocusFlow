from tkcalendar import Calendar

def instantiateWindow(window, tk):
    new_calendar = tk.Toplevel(window)
    cal = Calendar(new_calendar, selectmode="day", year=2025, month=1, day=11)
    cal.pack(pady=20)

    date_label = tk.Label(new_calendar, text=cal.get_date())
    date_label.pack()