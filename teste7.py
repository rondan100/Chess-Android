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


kv = '''
<ScreensManager>:
    MainScreen:
    SecondScreen:

<MainScreen>:
    name: "main_screen"
    
    BoxLayout:
        MDBottomNavigation:
            orientation: 'vertical'

            MDBottomNavigationItem:
                name: 'screen1'
                text: 'active'
                icon: 'note-plus'

                MDFloatingActionButton:
                    id: float_act_btn
                    icon: 'plus'
                    opposite_colors: True
                    md_bg_color: app.theme_cls.primary_color
                    pos_hint: {'center_x': 0.85, 'center_y': 0.08}    

            MDBottomNavigationItem:
                name: 'screen2'
                text: 'medicine'
                icon: 'pill'

                Button:
                    text:'Update'
                    font_size: 20
                    bold: True
                    size_hint: 0.15, 0.08
                    pos_hint: {'x':0.8, 'y': 0.5 }
                    color: 1, 1, 1, 1
                    on_press: root.Update()

                MDFloatingActionButton:
                    pos_hint:{"center_x": .85, "center_y": .075}
                    icon: 'plus'
                    md_bg_color: app.theme_cls.primary_color
                    on_release:
                        app.root.current = "second_screen"
                        root.manager.transition.direction = "left"

            MDBottomNavigationItem:
                name: 'screen3'
                text: 'calendar'
                icon: 'calendar'


<SecondScreen>:
    name: "second_screen"
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'vertical'
            padding: 20

            MDLabel:
                text: "Insert your data"

            Widget:

            MDLabel:
                text:"Name of medicine"

            MDTextField:
                id: name_med
                hint_text: "Name"
                mode: "rectangle"

            Widget:

            MDLabel:
                text:"How many pills do you have?"

            MDTextField:
                id: pills_amount
                hint_text: "Pills amount"
                mode: "rectangle"

            Widget:

            MDLabel:
                text:"How many times a day to take them?"

            MDTextField:
                id: times_amount
                hint_text: "Times a day"
                mode: "rectangle"

        FloatLayout:
            MDFloatingActionButton:
                pos_hint:{"center_x": .2, "center_y": .2}
                icon: 'arrow-left'
                on_release:
                    app.root.current = "main_screen"
                    root.manager.transition.direction = "right"

            MDFloatingActionButton:
                pos_hint:{"center_x": .8, "center_y": .2}
                icon: 'check'
                md_bg_color: app.theme_cls.primary_color
                on_release:
                    app.root.current = "main_screen"
                    root.manager.transition.direction = "right"
'''

Builder.load_string(kv)

class ScreensManager(ScreenManager):
    pass

class MainScreen(Screen):
    box = ObjectProperty()

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
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1,size_hint=(1,0.4),pos_hint={"top":1.2}))

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