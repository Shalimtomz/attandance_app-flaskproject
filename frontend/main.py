from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.network.urlrequest import UrlRequest
from kivy.uix.popup import Popup
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)

        self.username_input = TextInput(hint_text='Username')
        self.email_input = TextInput(hint_text='Email')
        self.password_input = TextInput(hint_text='Password', password=True)
        self.register_button = Button(text='Register', on_press=self.register_user)
        self.go_to_login_button = Button(text='Click here to Login', on_press=self.go_to_login)
        layout.add_widget(Label(text='Register', font_size=24))
        layout.add_widget(self.username_input)
        layout.add_widget(self.email_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.register_button)
        layout.add_widget(self.go_to_login_button)
        self.add_widget(layout)

    def register_user(self, instance):
        username = self.username_input.text
        email = self.email_input.text
        password = self.password_input.text

        data = {'username': username, 'email': email, 'password': password}
        url = 'http://127.0.0.1:5000/register'

        req = UrlRequest(url, on_success=self.register_success, req_body=json.dumps(data),
                         req_headers={'Content-Type': 'application/json'})

    def register_success(self, req, result):
        print(result)
        self.manager.current = 'login'  # Transition to the LoginScreen
    def go_to_login(self, instance):
        self.manager.current = 'login'  # Transition to the LoginScreen

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)

        self.username_input = TextInput(hint_text='Username', border=[10, 10, 10, 10])
        self.email_input = TextInput(hint_text='Email', border=[10, 10, 10, 10])
        self.password_input = TextInput(hint_text='Password', password=True, border =[10, 10, 10, 10])
        self.login_button = Button(text='Login', on_press=self.login_user, border=[10, 10, 10, 10])
        self.go_to_register_button = Button(text='Click here to Register', on_press=self.go_to_register, border=[10, 10, 10, 10])


        layout.add_widget(Label(text='Login', font_size=24))
        layout.add_widget(self.username_input)
        layout.add_widget(self.email_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.login_button)
        layout.add_widget(self.go_to_register_button)

        self.add_widget(layout)

    def go_to_register(self, instance):
        self.manager.current = 'register'  # Transition to the RegisterScreen



    def login_user(self, instance):
        username = self.username_input.text
        email = self.email_input.text
        password = self.password_input.text

        data = {'username': username, 'email': email, 'password': password}
        url = 'http://127.0.0.1:5000/login'

        req = UrlRequest(url, on_success=self.login_success, req_body=json.dumps(data),
                         req_headers={'Content-Type': 'application/json'})

    def login_success(self, req, result):
        print(result)
        if result.get('message') == 'Login successful':
            self.manager.current = 'success'  # Transition to the SuccessScreen
        else:
            self.show_alert('Login Failed', 'Invalid credentials')

    def show_alert(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()
    def on_pre_enter(self, *args):
        # Reset the text inputs when returning to the LoginScreen
        self.username_input.text = ''
        self.email_input.text = ''
        self.password_input.text = ''


class SuccessScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)
        layout.add_widget(Label(text='Login Successful', font_size=24))
        self.logout_button = Button(text='Logout', pos=(50,-100),background_color='green',size=(5,10),on_press=self.go_to_login)
        layout.add_widget(self.logout_button)
        self.add_widget(layout)

    def go_to_login(self, instance):
        self.manager.current = 'login'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SuccessScreen(name='success'))
        return sm

    def on_start(self):


        self.root.current = 'login'  # Set the current screen to the LoginScreen


if __name__ == '__main__':
    MyApp().run()
