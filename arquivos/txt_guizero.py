from guizero import App, PushButton, Text

def get_file():
    file_name.value = app.select_file()

def process_file():
    with open(file_name.value) as f:
        value = f.read()
        conteudo_text.value = value



app = App()

file_name = Text(app)
PushButton(app, command=get_file, text="Selecionar Arquivo")
PushButton(app, command=process_file, text="Ler arquivo")
conteudo_text = Text(app)

app.display()
