from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty

class QCountWidget(Widget):
    text = StringProperty()
    correctCount = 0
    wrongCount = 0
    def __init__(self, **kwargs):
        super(QCountWidget, self).__init__(**kwargs)
        self.text = ''
        self.show()

    def correct(self):
        self.correctCount += 1
        self.show()

    def wrong(self):
        self.wrongCount += 1
        self.show()
    
    def reset(self):
        self.correctCount = 0
        self.wrongCount = 0
        self.show()

    def show(self):
        self.text = f"{self.correctCount} - {self.wrongCount}"


class QCountApp(App):
    def __init__(self, **kwargs):
        super(QCountApp, self).__init__(**kwargs)
        self.title='QScorer'

    def build(self):
        return QCountWidget()
   
if __name__ == '__main__':
    QCountApp().run()