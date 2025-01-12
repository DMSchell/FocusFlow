import google.generativeai as genai

genai.configure(api_key="AIzaSyDS4U4obx8bERL6yGU2Uc2eWdqghNpkn9c")
model = genai.GenerativeModel("gemini-1.5-flash")

def instantiateWindow(mainWindow, tk):
    note_window = tk.Toplevel(mainWindow)
    note_window.title("Gemini")
    note_window.attributes("-topmost", True)
    
    text_box = tk.Text(note_window, height=10, width=40)
    text_box.pack(pady=20)

    save_button = tk.Button(note_window, text="Generate response", command=lambda: getResponse(text_box.get("1.0", tk.END), response_box, tk))
    save_button.pack(pady=5)

    response_box = tk.Text(note_window, height=10, width=40)
    response_box.pack(pady=20)

def getResponse(input, response_box, tk):
    response = model.generate_content(input)
    response_box.delete("1.0","end")
    response_box.insert(tk.END, response.text)
