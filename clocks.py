import time

# clock
def update_time(label):
    current_time = time.strftime("%H:%M:%S")
    label.config(text=f"{current_time}")
    label.after(100, update_time, label)

def instantiateWindow(mainWindow, tk):
    time_window = tk.Toplevel(mainWindow)
    time_window.title("Current Time")
    time_window.attributes("-topmost", True)
    
    time_label = tk.Label(time_window, text="", font=("Arial", 16))
    time_label.pack(pady=20)

    update_time(time_label)