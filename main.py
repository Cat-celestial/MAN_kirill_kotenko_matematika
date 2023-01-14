from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MAN_APP(MDApp):
    def build(self):
        return MDLabel(text="Hello my little kirill, you  should do MAN and train django, i am from past"
                       , halign="center")


MAN_APP().run()
