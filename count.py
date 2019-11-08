from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty

class CountWidget(Widget):
    text = StringProperty()
    count = 0
    def __init__(self, **kwargs):
        super(CountWidget, self).__init__(**kwargs)
        self.text = ''

    def buttonClicked(self):
        self.count += 1
        self.text = f'{self.count} Clicked'

class CountApp(App):
    def __init__(self, **kwargs):
        super(CountApp, self).__init__(**kwargs)
        self.title='Hello, kivi'

    def build(self):
        return CountWidget()
   
if __name__ == '__main__':
    CountApp().run()