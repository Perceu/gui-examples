from guizero import App, TextBox, PushButton, info

def divisao():
    val = float(num1.value)/ float(num2.value)
    info("info", "a divisão resultou: {}".format(val))

app = App()

num1 = TextBox(app)
num2 = TextBox(app)

button = PushButton(app, text="Dividir", command=divisao)

app.display()