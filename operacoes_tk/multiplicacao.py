import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tela de exemplo")

#funções 
def multiplicacao():
    multiplicacao = float(ent1.get())/float(ent2.get())
    messagebox.showinfo('Resultado', "A multiplicação deu: {}".format(multiplicacao))

#componentes:
lbl1 = tk.Label(window, text = "Numero 1: ")
lbl2 = tk.Label(window, text = "Numero 2: ")
ent1 = tk.Entry(window)
ent2 = tk.Entry(window)
btn = tk.Button(window, text = "multiplicar", command = multiplicacao)

#organiza os compontentes na tela :
lbl1.grid(column = 0, row = 0)
lbl2.grid(column = 0, row = 1)

ent1.grid(column = 1, row = 0)
ent2.grid(column = 1, row = 1)

btn.grid(column = 0, row = 2)

 
window.mainloop()