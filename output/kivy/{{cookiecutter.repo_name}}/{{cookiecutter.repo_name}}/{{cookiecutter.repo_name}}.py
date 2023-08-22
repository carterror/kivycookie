import kivy

kivy.require('{{cookiecutter.kivy_version}}')

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty


class Controller(FloatLayout):
    '''Create a controller that receives a custom widget from the kv lang file.

    Add an action to be called from the kv lang file.
    '''
    label_wid = ObjectProperty()
    info = StringProperty()

    def do_action(self):
        self.label_wid.text = 'My label after button press'
        self.info = '{{cookiecutter.short_description}}'


class {{cookiecutter.app_class_name}}(App):

    def build(self):
        return Controller(info='{{cookiecutter.app_title}}')


if __name__ == '__main__':
    {{cookiecutter.app_class_name}}().run()
