import tkinter as tk
from tkinter import ttk

nombre_input = ''

# def submit_function():
#     print(nombre_input)

def invok_ui(submit_function):
    window = tk.Tk()
    window.title('Reconocimiento facial')

    label = ttk.Label(window, text ='Nombre')
    entry = ttk.Entry(window, textvariable = nombre_input)
    button = ttk.Button(window, text = 'submit', command = lambda : submit_function(entry.get()))

    label.pack(side = tk.TOP, fill = tk.BOTH)
    entry.pack(side = tk.TOP, fill = tk.BOTH)
    button.pack(side = tk.TOP, fill = tk.BOTH)  

    window.mainloop()