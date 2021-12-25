from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class Screen(GridLayout):

    def __init__(self) -> None:
        super().__init__()
        self.add_widget(Label(text = 'Tela Base'))

class MyApp(App):

    def build(self):
        return Screen()


if __name__ == '__main__':
    MyApp().run()