from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label

#importしたAppを用いて、画面作成
class HelloApp(App):

    #画面にHello World!と表示
    def build(self):
        lbl=Label(text='Hello World!')
        return lbl

#Main
if __name__ == '__main__':
    #アプリの起動
    HelloApp().run()