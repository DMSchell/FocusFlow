import os
import tkinter as tk
from tkinter import filedialog, messagebox

file_path = "";

def findFileToUpload(uploadLabel, window, tk):
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Python files", "*.py"), ("All files", "*.*")])
    
    if file_path:
        if file_path.endswith('.py'):
            uploadLabel.config(text=f"Python file uploaded: {file_path}")
            execute_python_file(file_path, window, tk)
        else:
            messagebox.showerror("Invalid File", "Please upload a Python file (.py).")
    else:
        uploadLabel.config(text="No file selected")

def execute_python_file(file_path, window, tk):
    try:
        with open(file_path, 'r') as file:
            code = file.read()

        local_namespace = {}

        exec(code, {}, local_namespace)

        if 'instantiateWindow' in local_namespace:
            param1 = window
            param2 = tk
            makewindow_func = local_namespace['instantiateWindow']
            makewindow_func(param1, param2)
        else:
            messagebox.showerror("Function Not Found", "'instantiateWindow' function not found in the uploaded file.")
    
    except Exception as e:
        messagebox.showerror("Execution Error", f"Error executing the file: {e}")

def readThroughFolder(folder_path):
    # Get a list of all files in the folder
    files_in_folder = os.listdir(folder_path)
    
    # Filter for Python files only
    python_files = [f for f in files_in_folder if f.endswith('.py')]
    
    # Read the contents of each Python file
    contents = {}
    for python_file in python_files:
        file_path = os.path.join(folder_path, python_file)
        with open(file_path, 'r') as file:
            content = file.read()
            contents[python_file] = content
            
    return contents

def checkForExtensions(frame, window, path):
    if path:
        contents = readThroughFolder(path)
        for file, content in contents.items():
            makeButton(window, path, file, frame)

def makeButton(window, path, file, frame):
    tk.Button(frame, text=file, command=lambda: execute_python_file(path+"/"+file, window, tk)).pack(side=tk.LEFT, padx=5)