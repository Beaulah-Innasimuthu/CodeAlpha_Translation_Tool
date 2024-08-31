import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator

# Function to translate text
def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    target_language = lang_var.get()
    
    if not text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return
    
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_language)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {e}")

# List of languages (You can add more languages)
LANGUAGES = {
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese (Simplified)": "zh-cn",
    "Japanese": "ja",
    "Hindi": "hi",
    "English": "en",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Russian": "ru",
    "Tamil": "ta",        
    "Telugu": "te",       
    "Marathi": "mr",      
    "Bengali": "bn",      
}

# Create the main window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("400x300")

# Input text box
input_label = tk.Label(root, text="Enter text to translate:")
input_label.pack(pady=5)
input_text = tk.Text(root, height=5, width=50)
input_text.pack(pady=5)

# Language selection
lang_label = tk.Label(root, text="Select target language:")
lang_label.pack(pady=5)
lang_var = tk.StringVar(value="es")
lang_menu = ttk.Combobox(root, textvariable=lang_var, values=list(LANGUAGES.keys()))
lang_menu.pack(pady=5)

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Output text box
output_label = tk.Label(root, text="Translated text:")
output_label.pack(pady=5)
output_text = tk.Text(root, height=5, width=50)
output_text.pack(pady=5)

# Run the GUI event loop
root.mainloop()
