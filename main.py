from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from cookiecutter.main import cookiecutter
import json
import os


class MenuScreen(GridLayout):

    def __init__(self, m, c, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.cols = 2
        self.m = m
        self.c = c

        print(os.listdir('./input'))

        for b in os.listdir('./input'):
            self.add_widget(Button(text=b, on_press=self.change))

    def change(self, instance):
        self.c = 'django'
        self.m.current = 'cookie'


class CookieScreen(GridLayout):
    asd = []

    def __index__(self):
        print('asdasdsad')

    def __init__(self, m, c, **kwargs):
        super(CookieScreen, self).__init__(**kwargs)
        self.cols = 2
        self.m = m

        with open(f'input/{c}/cookiecutter.json', 'r') as f:
            array = json.load(f)

        print(array)

        for j in array:

            self.asd.append([j, TextInput(multiline=False, text=array[j])])

            if not j.startswith('_'):
                self.add_widget(Label(text=j))
                self.add_widget(self.asd[-1][1])

        self.add_widget(Button(text='Back', on_press=self.change))
        btn = Button(text='Create', on_press=self.chose_letter)
        self.add_widget(btn)

    def change(self, instance):
        self.m.current = 'menu'

    def chose_letter(self, instance):
        r = {}

        for f in self.asd:
            r[f[0]] = f[1].text

        json_obj = json.dumps(r)

        with open('output/kivy/cookiecutter.json', 'w') as f:
            json.dump(json.loads(json_obj), f)

        cookiecutter('./output/kivy/', no_input=True, output_dir='./apps/')


class MyApp(App):
    cutter = 'kivy'

    def build(self):
        sm = ScreenManager()

        screen1 = Screen(name='cookie')
        screen1.add_widget(CookieScreen(sm, self.cutter))
        screen2 = Screen(name='menu')
        screen2.add_widget(MenuScreen(sm, self.cutter))

        sm.add_widget(screen1)
        sm.add_widget(screen2)

        return sm


if __name__ == '__main__':
    MyApp().run()
