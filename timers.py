import time

# timer
def update_timer(label):
    if timer_running:
        global elapsed_time, start_time, resume_time
        elapsed_time = time.time() - start_time - resume_time
        mins, secs = divmod(elapsed_time, 60)
        millis = int((elapsed_time - int(elapsed_time)) * 1000)
        label.config(text=f"Timer: {int(mins):02}:{int(secs):02}:{millis:03d}")
        label.after(100, update_timer, label)


# fix start timer
def start_timer(label):
    global timer_running, resume_time
    timer_running = True
    resume_time = time.time() - start_time
    update_timer(label)

def stop_timer():
    global timer_running
    timer_running = False

def reset_timer(label):
    global start_time
    start_time = time.time()
    update_timer(label)

def instantiateWindow(mainWindow, tk):
    global elapsed_time, timer_running, start_time
    elapsed_time = 0
    timer_running = False
    start_time = time.time()
    
    timer_window = tk.Toplevel(mainWindow)
    timer_window.title("Timer")
    timer_window.attributes("-topmost", True)
    
    timer_label = tk.Label(timer_window, text="Timer: 00:00:000", font=("Arial", 16))
    timer_label.pack(pady=20)
    
    start_button = tk.Button(timer_window, text="Start", command=lambda: start_timer(timer_label))
    start_button.pack(side=tk.LEFT, padx=5)

    stop_button = tk.Button(timer_window, text="Stop", command=stop_timer)
    stop_button.pack(side=tk.LEFT, padx=5)

    reset_button = tk.Button(timer_window, text="Reset", command=lambda: reset_timer(timer_label))
    reset_button.pack(side=tk.LEFT, padx=5)
