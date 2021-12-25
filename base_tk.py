import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tela de exemplo")

#componentes:
lbl1 = tk.Label(window, text = "Primeira Tela em Tkinter")

#organiza os compontentes na tela :
lbl1.grid(column = 0, row = 0)
 
window.mainloop()