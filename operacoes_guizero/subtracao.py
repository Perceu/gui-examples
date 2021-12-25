from guizero import App, TextBox, PushButton, info

def subtracao():
    val = float(num1.value)- float(num2.value)
    info("info", "a subtração resultou: {}".format(val))

app = App()

num1 = TextBox(app)
num2 = TextBox(app)

button = PushButton(app, text="Subtração", command=subtracao)

app.display()