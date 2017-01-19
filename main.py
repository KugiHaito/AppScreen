# Essential Packages
import os
import pymysql as mysql
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
        padding:10
        Label:
            text: 'Seja Bem Vindo'
            font_size: 50
            size_hint:(1, .4)
        TextInput:
            id:nick
            text:open('.saved/.name.txt','r').read()
            hint_text: 'Nickname'
            font_size:20
            write_tab:False
            size_hint:(1, .1)
            background_color:(0,0,0,0)
        TextInput:
            id:pswd
            text:open('.saved/.pass.txt','r').read()
            hint_text: 'Password'
            password:True
            font_size:20
            write_tab:False
            size_hint:(1, .1)
            background_color:(0,0,0,0)
        Label:
    BoxLayout:
        orientation:'horizontal'
        size_hint:(.05,1.2)
        padding:5
        CheckBox:
            id:check
            size_hint:(.1,1)
        Label:
            text:'Lembrar-me'
            size_hint:(0,1)
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
            on_press: root.log(nick.text, pswd.text, check.active)
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
            text:"Seja Bem Vindo!"
            font_size:120
        Button:
            text: 'Logout'
            size_hint:(1, .05)
            on_press: root.quit()
""")

# Definition General
try:
    os.mkdir(".saved/")
    _name = open(".saved/.name.txt", "w")
    _name.close()
    _pass = open(".saved/.pass.txt", "w")
    _pass.close()
    os.system("attrib +h .saved/")
except:
    pass

def addslashes(s):
    d = {'"':'\\"', "'":"\\'", "\0":"\\\0", "\\":"\\\\"}
    return ''.join(d.get(c, c) for c in s)

class Login(Screen):
    # Functions
    def pull():
        _name = open(".saved/.name.txt", "r")
        ni = _name.read()
        _name.close()
        _pass = open(".saved/.pass.txt", "r")
        p = _pass.read()
        _pass.close()
        return ni

    def log(args, n, p, c):
        if n == "Nickname.." or n == "":
            p = Popup(title='Login Error', content=Label(text="Digite seu apelido!", color=(1,0,0,1)),size_hint=(.6, .2))
            p.open()
        elif p == "Password.." or p == "":
            p = Popup(title='Login Error', content=Label(text="Digite sua senha!", color=(1,0,0,1)),size_hint=(.6, .2))
            p.open()
        else:
            name = addslashes(n)
            pswd = addslashes(p)
            sql = "select * from users where nickname ='"+name+"' and passwd='"+pswd+"'"
            enc = cur.execute(sql)
            if enc:
                if c:
                    try:
                        _name = open(".saved/.name.txt", "w")
                        _name.write(name)
                        _name.close()
                        _pass = open(".saved/.pass.txt", "w")
                        _pass.write(pswd)
                        _pass.close()
                        os.system("attrib +h .saved/")
                    except:
                        print("Error in saving..")
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
            # Tratando dados..
            name = addslashes(n)
            pswd = addslashes(p)
            sql = "select * from users where nickname = '"+name+"'"
            rows = cur.execute(sql)
            if rows > 0:
                p = Popup(title='Login Error', content=Label(text="Este apelido esta em uso!", color=(1,0,0,1)),size_hint=(.6, .2))
                p.open()
            else:
                sql = "insert into users (nickname, passwd, level, photo, online) values ('"+name+"', '"+pswd+"', 'Usuario', default, '0')"
                cur.execute(sql)
                con.commit()

class Home(Screen):
    def quit(arg):
        sm.current = 'main'

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
