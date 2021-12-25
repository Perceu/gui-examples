from guizero import App, TextBox, PushButton, info

def multiplicacao():
    val = float(num1.value)* float(num2.value)
    info("info", "a multiplicação resultou: {}".format(val))

app = App()

num1 = TextBox(app)
num2 = TextBox(app)

button = PushButton(app, text="Multiplicação", command=multiplicacao)

app.display()