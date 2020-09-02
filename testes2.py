from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp

from kivy.core.window import Window
from chess_init import chess_initt, speed_games, pd, sns, plt, np

from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

from kivy.uix.screenmanager import ScreenManager, Screen



Window.size = (350, 650)

KV = '''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Screen 1"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Screen 2"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"


Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "scr 1"

                MDLabel:
                    text: "Screen 1"
                    halign: "center"
                
                
                MDRectangleFlatButton:
                    text: 'Back'
                    pos_hint: {'center_x':0.5,'center_y':0.1}
                    on_press: root.btn() 

            Screen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer

'''

sns.set_style("whitegrid")
plt.figure(figsize=(13, 7))

sns.lineplot(y='my_elo', 
             x=speed_games.index,
             data=speed_games, 
             color='darkslategray')

sns.lineplot(y='my_elo_ma', 
             x=speed_games.index,
             data=speed_games, 
             color='red')

plt.xlabel('Number of Games', fontsize=13)
plt.ylabel('My Elo', fontsize=13)
plt.title('My Elo Over Time', fontsize=15)
plt.xlim(-20)

plt.legend(['elo', '30-day MA'])



class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class MainWindow(Screen):
    def btn(self):
        print("name: ",self.name2.text)
        self.manager.get_screen('second').ids.destination.add_widget(FigureCanvasKivyAgg(plt.gcf())) 


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)


TestNavigationDrawer().run()