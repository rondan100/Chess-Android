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
    # MDLabel:
    #     text: "Content1"
    #     pos_hint: {"center_x": 0.95, "center_y": 0.2}

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
                # orientation: 'vertical'

                ScrollView:
                    do_scroll_x: False
                    do_scroll_y: True

                    GridLayout:
                        # id: box
                        size_hint_y: None
                        height: self.minimum_height
                        cols: 1
                        rows: 2
                        size: root.width, root.height 
                        # pos_hint:{'x': 0.02, 'y': 0.85 }

                        orientation: 'vertical'

                        BoxLayout:
                            id: box
                            size_hint: 0.8, 0.8
                            pos_hint:{'x': 0.1, 'y': 0.8 }

                        BoxLayout:
                            id: box
                            size_hint: 0.8, 1
                            pos_hint:{'x': 0.1, 'y': 0.3 }

                Button:
                    text:'Update'
                    font_size: 20
                    bold: True
                    size_hint: 0.1, 0.08
                    pos_hint: {'x':0.8, 'y': 0.1 }
                    color: 1, 1, 1, 1
                    on_press: root.show_alert_dialog()
                Button:
                    text:'Limpar'
                    font_size: 20
                    bold: True
                    size_hint: 0.1, 0.08
                    pos_hint: {'x':0.8, 'y': 0 }
                    color: 1, 1, 1, 1
                    on_press: root.Update2()
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
    # box2 = ObjectProperty(None)
    dialog = None

    def add_plot(self):
        from chess_init import chess_initt, speed_games, pd, sns, plt, np
        # opcao = str(input("Atualizar?"))
        # if opcao=='1':
        #     chess_initt()
        # else:
        #     print("nao atualizou")

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

        plt.xlabel('Number of Games', fontsize=11)
        plt.ylabel('My Elo', fontsize=13)
        plt.title('My Elo Over Time', fontsize=15)
        plt.xlim(-20)
        plt.legend(['elo', '30-day MA'])
        self.fig1 = plt.gcf()

        return self.fig1

    def add_plot2(self):
        from chess_init import chess_initt, speed_games, pd, sns, plt, np

        country_average = speed_games.groupby(speed_games['opponent_country']).mean()
        country_count = speed_games.groupby(speed_games['opponent_country']).count()
        country_stats = pd.DataFrame(country_average['result']).join(pd.DataFrame(country_count['my_elo']), how='inner')
        sns.set_style("whitegrid")
        plt.figure(figsize=(13, 7))

        sns.barplot(y='result',
                    x=country_stats[country_stats.my_elo > 3].index,
                    data=country_stats[country_stats.my_elo > 3],
                    order=country_stats[country_stats.my_elo > 3].sort_values('result', ascending=False).index,
                    palette="coolwarm"
                )

        plt.xticks(rotation=90)
        plt.ylim(.1,1)

        plt.xlabel('Country (n > 3)', fontsize=13)
        plt.ylabel('Win Percentage', fontsize=13)
        plt.title('Win Percentage by Country', fontsize=15)
        self.fig2 = plt.gcf()

        return self.fig2

    def Update(self, dialog):
        # self.box.remove_widget(FigureCanvasKivyAgg(self.fig1))
        self.dialog.dismiss()
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = MainScreen.add_plot(self)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1,size_hint=(0.5,0.8),pos_hint={"top":1}))

    def Update2(self):
        if isinstance(self.fig2, MainScreen):
            self.box.remove_widget(FigureCanvasKivyAgg(self.fig1))
        # self.dialog.dismiss()
        plt.cla()
        self.box.clear_widgets()
        self.fig2 = MainScreen.add_plot2(self)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig2,size_hint=(0.5,1),pos_hint={"top":1}))

    def Limpar(self):
        self.box.clear_widgets()

    def Cancelar(self,dialog):
        self.dialog.dismiss()


    
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Discard draft?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL", 
                        # text_color=self.box.theme_cls.primary_color,
                        on_release=self.Cancelar
                    ),
                    MDFlatButton(
                        text="ATUALIZAR?", 
                        # text_color=self.box.theme_cls.primary_color,
                        on_release= self.Update

                    ),
                ],
            )
        self.dialog.open()

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
        # if platform not in ('android', 'ios'):
        #     Config.set('graphics', 'resizable', '0')
        #     Window.size = (320, 420)
        super().__init__(**kwargs)

    def build(self):
        return ScreensManager() 

if __name__ == "__main__":
    MyApp().run()