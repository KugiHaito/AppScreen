# Essential Packages
import MySQLdb as mysql
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
# Interface Packages
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
# Information Definitions

con = mysql.connect(db="talkchat", user="root", passwd="youcode", host="127.0.0.1")
cur = con.cursor()

# Secondary Code
Builder.load_string("""
<Login>:
    BoxLayout:
        orientation:'vertical'
        Label:
            text: 'Seja Bem Vindo'
            font_size: 40
            size_hint:(1, .4)
        TextInput:
            id:nick
            hint_text: 'Nickname'
            font_size:20
            write_tab:False
            size_hint:(1, .1)
            background_color:(0,0,0,0)
        TextInput:
            id:pswd
            hint_text: 'Password'
            password:True
            font_size:20
            write_tab:False
            size_hint:(1, .1)
            background_color:(0,0,0,0)
        Label:
    BoxLayout:
        orientation:'horizontal'
        size_hint: (1,.1)
        Button:
            id: entry
            text: 'Entrar'
            size_hint: (1,.7)
            border: (2,5,2,5)
            #background_down:'img/btn.png'
            background_normal:'img/btn.png'
            on_press: root.log(nick.text, pswd.text)
        Button:
            text: 'Cadastrar-se'
            size_hint: (1,.7)
            border: (2,5,2,5)
            #background_down:'img/btn.png'
            background_normal:'img/btn.png'
            on_press: root.reg(nick.text, pswd.text)

<Home>:
    BoxLayout:
        orientation:'vertical'
        Label:
            text: 'Seja Bem Vindo!'
            font_size:120
        Button:
            text: 'Logout'
            size_hint:(1,.05)
            on_press: root.manager.current = 'main'
""")

class Login(Screen):
    # Functions
    def log(args, n, p):
        if n == "Nickname.." or n == "":
            p = Popup(title='Login Error', content=Label(text="Digite seu apelido!", color=(1,0,0,1)),size_hint=(.6, .2))
            p.open()
        elif p == "Password.." or p == "":
            p = Popup(title='Login Error', content=Label(text="Digite sua senha!", color=(1,0,0,1)),size_hint=(.6, .2))
            p.open()
        else:
            sql = "select * from users where nickname ='"+n+"' and passwd='"+p+"'"
            enc = cur.execute(sql)
            if enc:
                sm.current = 'space'
                Window.size=(1366, 768)
            else:
                p = Popup(title='Login Error', content=Label(text="Usuario "+n+" nao encontrado!"),size_hint=(.6, .2))
                p.open()

    def reg(args, n, p):
        if n == "Nickname.." or n == "":
            p = Popup(title='Login Error', content=Label(text="Digite seu apelido!", color=(1,0,0,1)),size_hint=(.6, .2))
            p.open()
        elif p == "Password.." or p == "":
            p = Popup(title='Login Error', content=Label(text="Digite sua senha!", color=(1,0,0,1)),size_hint=(.6, .2))
            p.open()
        else:
            sql = "select * from users where nickname = '"+n+"'"
            rows = cur.execute(sql)
        if rows > 0:
            p = Popup(title='Login Error', content=Label(text="Este apelido esta em uso!", color=(1,0,0,1)),size_hint=(.6, .2))
            p.open()
        else:
            sql = "insert into users (nickname, passwd, level, photo, online) values ('"+n+"', '"+p+"', 'Usuario', default, '0')"
            cur.execute(sql)
            con.commit()

class Home(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(Login(name='main'))
sm.add_widget(Home(name='space'))

class AppLogin(App):
    def build(self):
        self.icon = 'img/icon.png'
        # Window Settings
        Window.fullscreen = False
        Window.size = (620, 580)
        Window.clearcolor = (.6, .6, .6, .4)
        return sm

if __name__ == '__main__':
    AppLogin().run()
