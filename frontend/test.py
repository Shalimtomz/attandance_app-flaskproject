from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex


class CustomLoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(CustomLoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 20

        # Create and style TextInput fields with rounded box and sky blue color
        self.username_input = TextInput(hint_text='Username', background_color=get_color_from_hex('#87CEEB'),background_normal='', multiline=False, size_hint=(1, None), height=40,border_radius=[10, 10, 10, 10])
        self.email_input = TextInput(hint_text='Email', background_color=get_color_from_hex('#87CEEB'), background_normal='', multiline=False, size_hint=(1, None), height=40,border_radius=[10, 10, 10, 10])
        self.password_input = TextInput(hint_text='Password', background_color=get_color_from_hex('#87CEEB'), background_normal='', multiline=False, size_hint=(1, None), height=40,border_radius=[10, 10, 10, 10], password=True)

        # Create and style buttons
        self.login_button = Button(text='Login', background_color=get_color_from_hex('#4682B4'),size_hint=(1, None), height=40, border_radius=[10, 10, 10, 10])
        self.go_to_register_button = Button(text='Click here to Register',background_color=get_color_from_hex('#4682B4'),size_hint=(1, None), height=40, border_radius=[10, 10, 10, 10])

        # Bind button actions (you need to define these methods)
        self.login_button.bind(on_press=self.login_user)
        self.go_to_register_button.bind(on_press=self.go_to_register)

        # Add widgets to the layout
        self.add_widget(self.username_input)
        self.add_widget(self.email_input)
        self.add_widget(self.password_input)
        self.add_widget(self.login_button)
        self.add_widget(self.go_to_register_button)

    def login_user(self, instance):
        # Define the login action
        pass

    def go_to_register(self, instance):
        # Define the action to go to the registration screen
        pass


class TestApp(App):
    def build(self):
        return CustomLoginScreen()


if __name__ == '__main__':
    TestApp().run()
