from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.tab import MDTabsBase

KV = '''
<Tab1>:
    BoxLayout:
        MDFloatingActionButtonSpeedDial:
            data: app.data
<Tab2>:
    BoxLayout:
        MDFloatingActionButtonSpeedDial:
            data: app.data

BoxLayout:
    MDTabs:
        Tab1:
            id: tab1
            text: "tab 1"
        Tab2:
            id: tab2
            text: "tab 2"
'''
class Tab1(BoxLayout, MDTabsBase):
    pass
class Tab2(BoxLayout, MDTabsBase):
    pass

class MainApp(MDApp):
    data = {
        'language-python': 'Python',
        'language-php': 'PHP',
        'language-cpp': 'C++',
    }
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
