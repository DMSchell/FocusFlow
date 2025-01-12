from tkinter import filedialog, messagebox

def instantiateWindow(mainWindow, tk):
    note_window = tk.Toplevel(mainWindow)
    note_window.title("New Note")
    note_window.attributes("-topmost", True)
    
    text_box = tk.Text(note_window, height=10, width=40)
    text_box.pack(pady=20)

    save_button = tk.Button(note_window, text="Save", command=lambda: save_as_file(text_box, tk))
    save_button.pack(pady=5)

    open_note_button = tk.Button(note_window, text="Open", command=lambda: open_note(text_box, tk))
    open_note_button.pack(pady=5)

def save_as_file(text_box, tk):
    try:
        text_content = text_box.get("1.0", tk.END)

        file_name = "saved_note.txt"
        
        with open(file_name, "w") as file:
            file.write(text_content.strip())

        messagebox.showinfo("Success", f"Text has been successfully exported to {file_name}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def open_note(text_box, tk):
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    
    if file_path:
        if file_path.endswith('.txt'):
            write_note(file_path, text_box, tk)
        else:
            messagebox.showerror("Invalid File", "Please upload a text file (.txt).")

def write_note(file_path, text_box, tk):
    try:
        with open(file_path, 'r') as file:
            text_box.delete("1.0","end")
            text_box.insert(tk.END, file.read())
    
    except Exception as e:
        messagebox.showerror("Execution Error", f"Error executing the file: {e}")