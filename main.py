from tkinter import *


# ---------- LETTERS, SYMBOLS, AND PUNCTUATION ----------
morse_alphabet = {
    'A': '.- ',
    'B': '-.. ',
    'C': '-.-. ',
    'D': '-.. ',
    'E': '. ',
    'F': '..-. ',
    'G': '--. ',
    'H': '.... ',
    'I': '.. ',
    'J': '.--- ',
    'K': '-.- ',
    'L': '.-.. ',
    'M': '-- ',
    'N': '-. ',
    'O': '--- ',
    'P': '.--. ',
    'Q': '--.- ',
    'R': '.-. ',
    'S': '... ',
    'T': '- ',
    'U': '..- ',
    'V': '...- ',
    'W': '.-- ',
    'X': '-..- ',
    'Y': '-.-- ',
    'Z': '--.. ',
}

morse_numbers = {
    '0': '----- ',
    '1': '.---- ',
    '2': '..--- ',
    '3': '...-- ',
    '4': '....- ',
    '5': '..... ',
    '6': '-.... ',
    '7': '--... ',
    '8': '---.. ',
    '9': '----. ',
}

morse_punctuation = {
    '.': '.-.-.- ',
    ',': '--..-- ',
    '?': '..--.. ',
    "'": '.----. ',
    '!': '-.-.-- ',
    '/': '-..-. ',
    '(': '-.--. ',
    ')': '-.--.- ',
    '&': '.-... ',
    ':': '---... ',
    ';': '-.-.-. ',
    '=': '-...- ',
    '+': '.-.-. ',
    '-': '-....- ',
    '_': '..--.- ',
    '"': '.-..-. ',
    '$': '...-..- ',
    '@': '.--.-. ',
    ' ': '/ '
}


# ---------- ERROR POPUP ----------
def popup():
    error_popup = Toplevel(window)
    error_popup.title('Error')
    error_popup.minsize(width=100, height=100)
    error_popup.config(padx=10, pady=10)

    error_text = Label(error_popup,
                       text='There was an Error With Your Text Input. \n Please Try Again.',)
    error_text.grid(row=0, column=0, pady=20)

    close_button = Button(error_popup, text='close', command=error_popup.destroy, width=10, relief='groove')
    close_button.grid(row=2, column=0, sticky='e')


# ---------- TRANSLATOR ----------
def translate_text():
    # CONVERTER
    user_input = input_text.get('1.0', END).strip().upper()
    output = []
    for char in user_input:
        if char in morse_alphabet:
            code_letter = morse_alphabet[char]
            output.append(code_letter)
        elif char in morse_numbers:
            code_letter = morse_numbers[char]
            output.append(code_letter)
        elif char in morse_punctuation:
            code_letter = morse_punctuation[char]
            output.append(code_letter)
        else:
            return popup()

    translated_text = ''.join(output)

    output_text.delete('1.0', END)
    output_text.insert(END, translated_text)


# ---------- GUI ----------

# window
window = Tk()
window.title('Text to Morse Code Converter')
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# labels
title = Label(text='Best Text to Morse Code Converter', font=('ThaleahFat', 20))
title.grid(row=0, column=0, pady=(0, 20))

input_title = Label(text='Enter Text:', font=('ThaleahFat', 20))
input_title.grid(row=1, column=0, sticky='w', padx=(50, 0))

output_title = Label(text="Here's Your Morse Code!:", font=('ThaleahFat', 20))
output_title.grid(row=4, column=0, sticky='w', padx=(50, 0))

# Entry
input_text = Text(window, height=10, width=40)
input_text.grid(row=2, column=0)

output_text = Text(window, height=10, width=40)
output_text.grid(row=5, column=0)

# Button
button = Button(window,
                text='Enter',
                command=translate_text,
                font=('ThaleahFat', 20),
                width=20,
                )
button.grid(row=3, column=0, pady=10)

window.mainloop()
