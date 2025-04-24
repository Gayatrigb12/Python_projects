# Install necessary modules if not already installed
# pip install tk
# pip install googletrans==4.0.0-rc1

# Import GUI toolkit modules
from tkinter import *              # Import all basic tkinter components
from tkinter import ttk            # Import themed widgets (like Combobox)
from googletrans import Translator, LANGUAGES  # Import translation tools and language mappings

# Function to handle translation
def translate_text():
    src_lang = combo_from.get()                 # Get source language from dropdown
    dest_lang = combo_to.get()                 # Get target language from dropdown
    input_text = text_input.get("1.0", END).strip()  # Get user input text (from line 1 to end)

    if input_text:  # If input is not empty
        translator = Translator()              # Create translator object
        translated = translator.translate(
            text=input_text, src=src_lang, dest=dest_lang
        )                                      # Translate the input text
        text_output.delete("1.0", END)         # Clear previous output (if any)
        text_output.insert(END, translated.text)  # Display translated result

# --- GUI SETUP BELOW ---

# Create the main application window
root = Tk()                          # Initialize Tkinter root window
root.title("Translator")            # Set the window title
root.geometry("700x500")            # Set the window size
root.config(bg='black')             # Set background color to black

# Create a heading label
lab_text = Label(
    root, text="Translator", font=("Times New Roman", 30, "bold"),
    bg="black", fg="white"
)
lab_text.pack(pady=20)              # Pack the label with vertical padding

# Frame for language dropdowns
frame = Frame(root, bg="black")     # Create a frame to organize dropdowns
frame.pack(pady=10)                 # Pack the frame with some padding

# Dropdown to select source language
combo_from = ttk.Combobox(
    frame, values=list(LANGUAGES.keys()), width=20, font=("Arial", 12)
)
combo_from.set("en")                # Set default source language to English
combo_from.grid(row=0, column=0, padx=10)  # Place in grid

# Dropdown to select destination language
combo_to = ttk.Combobox(
    frame, values=list(LANGUAGES.keys()), width=20, font=("Arial", 12)
)
combo_to.set("hi")                  # Set default destination language to Hindi
combo_to.grid(row=0, column=1, padx=10)  # Place in grid

# Text box for user to enter input text
text_input = Text(
    root, height=7, width=60, font=("Arial", 14), wrap=WORD, bd=2
)
text_input.pack(pady=10)            # Pack the input text box with padding

# Button to trigger translation
btn_translate = Button(
    root, text="Translate", font=("Arial", 14),
    bg="green", fg="white", command=translate_text
)
btn_translate.pack(pady=10)         # Pack the button with padding

# Text box to show the translated result
text_output = Text(
    root, height=7, width=60, font=("Arial", 14), wrap=WORD, bd=2
)
text_output.pack(pady=10)           # Pack the output text box with padding

# Start the Tkinter GUI loop
root.mainloop()
