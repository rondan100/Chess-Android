from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.config import Config
from kivy.utils import platform
from funcoes_ import MainScreen, ContentNavigationDrawer, Tab, ScreensManager, SecondScreen
from kivymd.uix.menu import MDDropdownMenu

MainScreen
ContentNavigationDrawer
Tab
ScreensManager
SecondScreen

class MyApp(MDApp):
    data = {
        "language-python": "Chess.com",
        "language-php": "LiChess",
        "language-cpp": "Chess24",
    }

    def __init__(self, **kwargs):
        self.title = "Chess Statistics"
        self.theme_cls.primary_palette = "Teal"
        # Builder.load_file("versao13.kv")
        Window.size = (420, 810)
        super().__init__(**kwargs)

    #     self.screen = Builder.load_file("versao13.kv")
    #     menu_items = [{"text": f"Item {i}"} for i in range(5)]

    #     self.menu = MDDropdownMenu(
    #         caller=self.screen.ids.box.ids.toolbar.ids.botao,
    #         items=menu_items,
    #         width_mult=4,
    #     )
    #     self.menu.bind(on_release=self.menu_callback)
    
    # def menu_callback(self, instance_menu, instance_menu_item):
    #     instance_menu.dismiss()

    def build(self):
        return ScreensManager()

if __name__ == "__main__":
    MyApp().run()