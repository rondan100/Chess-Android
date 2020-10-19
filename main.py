from kivymd.app import MDApp
from kivy.lang import Builder
from funcoes_ import MainScreen, ContentNavigationDrawer, Tab, ScreensManager, SecondScreen

MainScreen
ContentNavigationDrawer
Tab
ScreensManager
SecondScreen

class MyApp(MDApp):

    def __init__(self, **kwargs):
        self.title = "Chess Science"
        # self.theme_cls.primary_palette = "Teal"
        # Window.size = (420, 810)
        super().__init__(**kwargs)

    def build(self):
        Builder.load_file("main.kv")
        self.theme_cls.primary_palette = "Teal"
        return ScreensManager()

if __name__ == "__main__":
    MyApp().run()