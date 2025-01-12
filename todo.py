def instantiateWindow(window, tk):
    todo_window = tk.Toplevel(window)

    todoLabel = tk.Label(todo_window, text="TODO", font=("Arial", 16))
    todoLabel.pack()
    todoName = tk.Text(todo_window, height=2, width=60)
    todoName.pack()

    # items in todo
    frame = tk.Frame(todo_window)
    frame.pack(pady=20)

    AddNewItemButton = tk.Button(todo_window, text="Add New Item", command=lambda: AddNewItem(frame))
    AddNewItemButton.pack()
    AddNewItem(frame, tk)

def AddNewItem(frame, tk):
    Item = tk.Text(frame, height=2, width=45)
    Item.pack()
    Done = tk.Button(frame, text="done???", command=lambda: Finish(Done))
    Done.pack()

def Finish(DoneButton):
    if (DoneButton.cget("text") == "done???"):
        DoneButton.config(text = "done!!!")
    else:
        DoneButton.config(text = "done???")