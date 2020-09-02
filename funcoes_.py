from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
import os.path


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class ScreensManager(ScreenManager):
    Builder.load_file("versao13.kv")
    # pass

class SecondScreen(Screen):
    pass

class MainScreen(Screen):
    box1 = ObjectProperty(None)
    box2 = ObjectProperty(None)
    dialog = None

    def add_plot(self):
        from chess_init import chess_initt, speed_games, pd, sns, plt, np
        # opcao = str(input("Atualizar?"))
        # if opcao=='1':
        #     chess_initt()
        # else:
        #     print("nao atualizou")

        if os.path.exists('./chess_games.csv') == False:
            self.dialog.dismiss()
            chess_initt()
        else:

            sns.set_style("whitegrid")
            plt.figure(figsize=(5, 0.5))

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
        self.box1.clear_widgets()
        self.fig1 = MainScreen.add_plot(self)
        self.box1.add_widget(FigureCanvasKivyAgg(self.fig1,size_hint=(1,1),pos_hint={"top":1}))

    def Update2(self):
        # if isinstance(self.fig2, MainScreen):
        #     self.box.remove_widget(FigureCanvasKivyAgg(self.fig1))
        # self.dialog.dismiss()
        plt.cla()
        self.box2.clear_widgets()
        self.fig2 = MainScreen.add_plot2(self)
        self.box2.add_widget(FigureCanvasKivyAgg(self.fig2,size_hint=(0.5,1),pos_hint={"top":1}))

    def Limpar(self):
        self.box.clear_widgets()

    def Cancelar(self,dialog):
        self.dialog.dismiss()

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Atualizar dados?",
                text="Isso irá importar os dados e poderá levar alguns instantes.",
                size_hint=(0.8,1),
                buttons=[
                    MDFlatButton(
                        text="CANCELAR", 
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


