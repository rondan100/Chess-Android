from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons

from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.app import MDApp
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np

from kivy.core.window import Window 

Window.size = (350, 650)

KV = '''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Screen 1"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "Scr_1"

            OneLineListItem:
                text: "Screen 2"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "Scr_2"

Screen:
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: False

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                box: box
                name: "Scr_1"

                BoxLayout:
                    id: box
                    size_hint: 0.8, 0.75
                    pos_hint:{'x': 0.15, 'y': 0.1 }

                Button:
                    text:'Update'
                    font_size: 20
                    bold: True
                    size_hint: 0.15, 0.08
                    pos_hint: {'x':0.8, 'y': 0.5 }
                    color: 1, 1, 1, 1
                    on_press: root.Update()

                MDLabel:
                    text: "Screen 1"
                    halign: "center"

            Screen:
                name: "Scr_2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Scr_1(Screen):
    box = ObjectProperty(None)
    def add_plot(self, N):

        phase = np.random.normal(-np.pi/2, +np.pi/2)
        noise = np.random.normal(0, 1, N)
        nbr = np.linspace(0,1,N)
        func = 0.01*noise+np.sin(nbr/0.1+phase)

        plt.plot(nbr,func,label='Line1',color='r')
        plt.ylabel('Sinus')
        plt.xlabel('Range')
        plt.grid(True)
        self.fig1 = plt.gcf()

        return self.fig1

    def Update(self):
        # self.box.remove_widget(FigureCanvasKivyAgg(self.fig1))
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Scr_1.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1,size_hint=(1,0.4),pos_hint={"top":1.2}))

    def Limpar(self):
        self.box.clear_widgets()


class TestNavigationDrawer(MDApp):
    icons = list(md_icons.keys())[15:30]

    data = {
        "language-python": "Chess.com",
        "language-php": "LiChess",
        "language-cpp": "Chess24",
    }
    
    def build(self):
        return Builder.load_string(KV)
    

TestNavigationDrawer().run()