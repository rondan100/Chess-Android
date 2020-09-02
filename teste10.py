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


kv = '''
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

<Tab>:
    MDLabel:
        text: "Content1"
        pos_hint: {"center_x": 0.95, "center_y": 0.2}

<ScreensManager>:
    MainScreen:
    SecondScreen:

<MainScreen>:
    name: "main_screen"
    box: box
    
    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: toolbar
            title: "Chess Statistics"
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
            right_action_items: [["dots-vertical", lambda x: nav_drawer.set_state("open")]]


        MDTabs:
            Tab:
                text: "DASHBOARD"
                MDFloatingActionButton:
                    id: float_act_btn
                    icon: 'plus'
                    opposite_colors: True
                    md_bg_color: app.theme_cls.primary_color
                    pos_hint: {'center_x': 0.84, 'center_y': 0.1}
            Tab:
                text: "STUDY"
                BoxLayout:
                    id: box
                    size_hint: 0.8, 0.8
                    pos_hint:{'x': 0.1, 'y': 0.2 }
                Button:
                    text:'Update'
                    font_size: 20
                    bold: True
                    size_hint: 0.15, 0.08
                    pos_hint: {'x':0.8, 'y': 0.1 }
                    color: 1, 1, 1, 1
                    on_press: root.Update()
            Tab:
                text: "PRACTICE"

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                # box: box
                name: "Scr_1"

                BoxLayout:
                    # id: box
                    size_hint: 0.8, 0.75
                    pos_hint:{'x': 0.15, 'y': 0.1 }

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

    


<SecondScreen>:
    name: "second_screen"
                
'''

Builder.load_string(kv)

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class ScreensManager(ScreenManager):
    pass

class MainScreen(Screen):
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
        self.fig1 = MainScreen.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1,size_hint=(1,0.5),pos_hint={"top":1}))

    def Limpar(self):
        self.box.clear_widgets()

class SecondScreen(Screen):
    pass

class MyApp(MDApp):
	data = {
		"language-python": "Chess.com",
		"language-php": "LiChess",
		"language-cpp": "Chess24",
	}

	def __init__(self, **kwargs):
		self.title = "Do Not Forget"
		self.theme_cls.primary_palette = "Teal"
		Window.size = (350, 650)
		super().__init__(**kwargs)

	def build(self):
		return ScreensManager() 

if __name__ == "__main__":
    MyApp().run()