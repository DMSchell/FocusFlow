#to make a new window, put this code in a python file

def instantiateWindow(window, tk):
    new_window = tk.Toplevel(window)

    
    #after this, build your window using the tkinter python library and whatever else you may need.
    #put your extension in the "extensions" file to have it work

    greeting = tk.Label(new_window, text="hello", font=("Arial", 16))
    greeting.pack()
    