from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.app import App
import time
# Connect in LocalHost
import MySQLdb as mysql

con = mysql.connect(db="talkchat", user="root", passwd="youcode", host="127.0.0.1")
cur = con.cursor()

class Home(BoxLayout):
    """docstring for Talkchat ."""
    def build(self, arg):
        self.welcome = Label(text="Ola! Seja Bem Vindo!")
        self.add_widget(self.welcome)



class Login(App):
  def build(self):
      self.icon = 'icon.png'
      # Window Settings
      Window.clearcolor = (.6, .6, .6, .3)
      # Layout
      page = FloatLayout()
      layout = BoxLayout(orientation='vertical')
      self.hi = Label(text='Seja Bem Vindo!', size_hint=(1, .7), font_size=40)
      self.nick = TextInput(text='Nickname..',size_hint=(1, .1), background_color=(0,0,0,0))
      self.pswd = TextInput(text='Password..', password=True ,size_hint=(1, .1), background_color=(0,0,0,0))
      self.save = CheckBox(size_hint=(.3, 1))
      self.save.bind(active=self.saved)
      layout.add_widget(self.hi)
      layout.add_widget(self.nick)
      layout.add_widget(self.pswd)
      # Layout Y
      layout_y = BoxLayout(orientation='horizontal', size_hint=(.3,.1))
      layout_y.add_widget(self.save)
      layout_y.add_widget(Label(text="Salvar Senha..", size_hint=(1, 1)))
      layout.add_widget(layout_y)
      layout.add_widget(Label(size_hint=(1,.2)))
      # layout X
      layout_x = BoxLayout(orientation='horizontal', size_hint=(1, .8))
      layout_x.add_widget(Button(text='Entrar', size_hint=(1, .2), background_normal='img/btn.png', border=(2,2,2,2),on_press= self.logar))
      layout_x.add_widget(Button(text='Cadastrar-se', size_hint=(1, .2), background_normal='img/btn.png', border=(2,2,2,2), on_press=self.register))
      layout.add_widget(layout_x)

      page.add_widget(layout)

      return page


  # Alterar -> Trocar modificacao de text pra Popup

  def saved(self,checkbox, value):
    # Salvar Apelido e Senha..
    if value:
        if self.nick.text == "Nickname.." or self.nick.text == "":
            self.save.active = False
            self.hi.color=(1,0,0,1)
            self.hi.text = "Digite seu Nickname!"
        elif self.pswd.text == "Password.." or self.pswd.text == "":
            self.save.active = False
            self.hi.color=(1,0,0,1)
            self.hi.text = "Digite sua Password!"
        else:
            self.hi.color=(1,1,1,1)
            self.hi.text = "Lembrarei de voce "+self.nick.text

  def logar(self, nick):
      if self.nick.text == "Nickname.." or self.nick.text == "":
          self.hi.color=(1,0,0,1)
          self.hi.text = "Digite seu Nickname!"
      elif self.pswd.text == "Password.." or self.pswd.text == "":
          self.hi.color=(1,0,0,1)
          self.hi.text = "Digite sua password!"
      else:
          sql = "select * from users where nickname ='"+self.nick.text+"' and passwd='"+self.pswd.text+"'"
          enc = cur.execute(sql)
          if enc:
              # Login..
              pass
          else:
              # Not Login
              p = Popup(title='Login Error', content=Label(text="Usuario nao encontrado!"),size_hint=(.6, .2))
              p.open()


  def register(self, nick):
    if self.nick.text == "Nickname.." or self.nick.text == "":
        self.hi.color=(1,0,0,1)
        self.hi.text = "Digite seu Nickname!"
    elif self.pswd.text == "Password.." or self.pswd.text == "":
        self.hi.color=(1,0,0,1)
        self.hi.text = "Digite sua password!"
    else:
        sql = "select * from users where nickname = '"+self.nick.text+"'"
        rows = cur.execute(sql)
        if rows > 0:
            self.hi.text = "Este nick esta em uso!"
        else:
            sql = "insert into users (nickname, passwd, level, photo, online) values ('"+self.nick.text+"', '"+self.pswd.text+"', 'Usuario', default, '0')"
            cur.execute(sql)
            con.commit()
            # Cadastrado! redirecione o usuario a nova janela

if __name__ == '__main__':
  Login().run()
