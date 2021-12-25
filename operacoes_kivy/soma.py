from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class SomaScreen(GridLayout):

    def __init__(self) -> None:
        super().__init__()
        self.cols=2
        self.numero_1 = TextInput()
        self.numero_1.focus = True
        self.numero_2 = TextInput()
        self.add_widget(Label(text = 'numero 1'))
        self.add_widget(self.numero_1)
        self.add_widget(Label(text = 'numero 2'))
        self.add_widget(self.numero_2)
        self.btn_somar = Button(text="somar")
        self.btn_somar.bind(on_press=self.somar)
        self.add_widget(self.btn_somar)

    def somar(self, btn):
        if self.numero_1.text != '' and self.numero_2.text != '':
            soma = float(self.numero_1.text) + float(self.numero_2.text)
            popup = Popup(
                title="resultado",
                content=Label(text='a soma foi: {}'.format(soma)),
                size=(50, 50),
            )
            popup.open()


class MyApp(App):

    def build(self):

        return SomaScreen()


if __name__ == '__main__':
    MyApp().run()