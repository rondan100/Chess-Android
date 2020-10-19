# ------------------------------------------------------------------------------------
# Gambiarra para funcionar no buildozer, pois o apk crash quando abre
# import imp
# import sys

# class ImportBlocker(object):

#     def __init__(self, *args):
#         self.black_list = args

#     def find_module(self, name, path=None):
#         if name in self.black_list:
#             return self

#         return None

#     def load_module(self, name):
#         module = imp.new_module(name)
#         module.__all__ = [] # Necessary because of how bs4 inspects the module

#         return module

# sys.meta_path = [ImportBlocker('bs4.builder._htmlparser')]

from bs4 import BeautifulSoup
# ---------------------------------------------------------------------------------------
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from functools import partial
from kivymd.uix.list import OneLineAvatarListItem
from kivy.properties import StringProperty
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from Progress_Bar import CircularProgressBar

from chess_init import (find_color, pull_dates, pull_game_links, pull_moves, pull_player_stats,
        pull_results, pull_speed, remove_dups)
from requests import get

from threading import Thread

# from seaborn import set_style, lineplot

from collections import Counter

# from kivy.properties import BooleanProperty

from matplotlib.pyplot import (gcf, cla, figure, xlabel,ylabel,title,xlim,legend,subplots_adjust,subplots,
imread,get_cmap,grid,plot,savefig,xticks, yticks)

# from matplotlib import use
# use('module://kivy.garden.matplotlib.backend_kivy')
# from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
# from matplotlib.backends.backend_agg import FigureCanvasAgg
# from kivy_garden.graph import Graph, MeshLinePlot
# from math import sin
# from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas

from kivy.uix.image import Image

# import matplotlib.pyplot as plt

# import pandas as pd
from pandas import DataFrame, read_csv, to_datetime, Series, value_counts

# import numpy as np
from numpy import where, array, zeros, arange

class Content(BoxLayout):
    pass

class Item(OneLineAvatarListItem):
    divider = None
    source = StringProperty()

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class ScreensManager(ScreenManager):
    pass

class SecondScreen(Screen):
    pass

class MainScreen(Screen):
    # pass
    # isShownLabel = BooleanProperty(False)

    def add_plot(self):
        try:
            self.matrix(0,0)    
            # self.fig1 = gcf()
            # return self.fig1
        except Exception:
            self.dialog = None
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Oops! Talvez devesse importar os dados antes!",
                    radius=[20, 7, 20, 7],
                )
                self.dialog.open()

    def add_plot2(self):
        try:
            self.matrix(0,1)
            # self.fig2 = gcf()
            # return self.fig2
        except Exception:
            self.dialog = None
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Oops! Talvez devesse importar os dados antes!",
                    radius=[20, 7, 20, 7],
                )
                self.dialog.open()

    def add_plot3(self):
        try:
            self.g_bar()

        except Exception:
            self.dialog = None
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Oops! Talvez devesse importar os dados antes!",
                    radius=[20, 7, 20, 7],
                )
                self.dialog.open()

    def Update3(self, dialog):
        self.dialog.dismiss()
        self.box1.clear_widgets()
        MainScreen.add_plot3(self)       
        self.fig3 = Image(source = 'pizza.png')
        self.fig3.size_hint_y = 1.05

        self.box1.add_widget(self.fig3)
       
    def Update(self, dialog):
        self.dialog.dismiss()
        # cla()
        self.box3.clear_widgets()
        # self.fig1 = MainScreen.add_plot(self)
        MainScreen.add_plot(self)       
        self.fig1 = Image(source = 'teste1.png')
        # self.fig1.allow_stretch = True
        # self.fig1.keep_ratio = False
        # self.fig1.width = self.width
        self.fig1.size_hint_x = 1.62
        self.box3.padding = 15
        # self.fig1.pos = (100, 50) 

        self.box3.add_widget(self.fig1)
        
        # self.box3.add_widget(FigureCanvasKivyAgg(self.fig1,size_hint=(1,1),pos_hint={"top":1.025}))
        # self.box3.add_widget(FigureCanvasAgg(self.fig1))
        # canvas = self.fig1.canvas
        # canvas.draw()
        # self.box3.add_widget(canvas)
        
        # graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
        # x_ticks_major=25, y_ticks_major=1,
        # y_grid_label=True, x_grid_label=True, padding=5,
        # x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
        # plot = MeshLinePlot(color=[1, 0, 0, 1])
        # plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        # graph.add_plot(plot)
        # self.box3.add_widget(graph)

    def Update2(self,dialog):
        self.dialog.dismiss()
        # cla()
        self.box4.clear_widgets()
        # self.fig2 = MainScreen.add_plot2(self)
        # self.box4.add_widget(FigureCanvasAgg(self.fig2,size_hint=(1,1),pos_hint={"top":1}))
        # canvas = self.fig2.canvas
        MainScreen.add_plot2(self)
        self.fig2 = Image(source = 'barra1.png')
        self.fig2.size_hint_y = 1.25
        self.box4.padding = 35
        self.box4.add_widget(self.fig2)

    def Limpar(self):
        self.box1.clear_widgets()

    def Cancelar(self, arg):
        self.dialog.dismiss()

    def Cancelar_(self, arg):
        self.screen_manager.current = "Scr_2"
        Clock.schedule_interval(self.animate, 0.01)

    def animate(self, dt):
        circProgressBar = self.manager.get_screen('main_screen').ids.cp
        if circProgressBar.value<80:
            circProgressBar.set_value(circProgressBar.value+1)
        else:
            circProgressBar.set_value(0)

    def tread_nick(self,arg):

        # adquirir a variavel de texto
        for obj in self.dialog.content_cls.children:
            self.nick = (obj.text)
        # create the thread to invoke other_func with arguments (2, 5)
        t = Thread(target=self.chess_initt)
        # set daemon to true so the thread dies when app is closed
        t.daemon = True
        # start the thread
        t.start()
        
        if self.dialog:
            self.dialog.dismiss()
        self.screen_manager.current = "Scr_2"
        self.event = Clock.schedule_interval(self.animate, 0.01)
        # Clock.schedule_once(self.animate)

        Clock.schedule_interval(partial(self.disable, t),0.1)
        # self.g_bar()

    def disable(self, t, what):
        if not t.isAlive():
            Clock.unschedule(self.event)
            self.screen_manager.current = "Scr_1"
            # self.add_plot3()
            return False

    def my_elo(self):
        self.dialog = None
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

    def left_menu(self):
        self.dialog = None
        if not self.dialog:
            self.dialog = MDDialog(
                # title="Atualizar dados?",
                type="simple",
                size_hint=(0.4,0.6),
                pos_hint= {'center_x': .75, 'center_y': .8},
                items=[
                    Item(text="user01@gmail.com", source="user-1.png"),
                    Item(text="user02@gmail.com", source="user-2.png"),
                    Item(text="Add account", source="add-icon.png"),
                ],
            )
        self.dialog.open()

    def nickname(self):
        self.dialog = None
        if not self.dialog:
            self.dialog = MDDialog(
                title="Chess.com",
                type="custom",
                content_cls=Content(),
                size_hint=(0.8,0.6),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_release=self.Cancelar
                    ),
                    MDFlatButton(
                        text="OK",
                        on_release= self.tread_nick
                    ),
                ],
            )
        self.dialog.open()

    def country(self):
            self.dialog = None
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
                            on_release= self.Update2

                        ),
                    ],
                )
            self.dialog.open()

    def barra_box1(self):
            self.dialog = None
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
                            on_release= self.Update3

                        ),
                    ],
                )
            self.dialog.open()

    # def table_(self):
    #     self.data_tables = MDDataTable(
    #         size_hint=(0.8, 0.6),
    #         use_pagination=False,
    #         check=True,
    #         column_data=[
    #             ("No.", dp(30)),
    #             ("Column 1", dp(30)),
    #             ("Column 2", dp(30)),
    #         ],
    #         row_data=[
    #             (f"{i + 1}", "2.23", "3.65")
    #             for i in range(50)
    #         ],
    #     )
    #     self.data_tables.open()

# --------------------------------------------------------------------------------
    ''' 
    Ajeitar.. o comando está demorando.. Isso já é notificado pela documentação.
    porém não estou conseguindo fazer da maneira certa. A função init nao reconhece a screen e isso pode estar relacionado 
    com ela não foi inicializada ainda e por isso não reconhece...
    '''

    def tres_pontos(self):

        menu_labels = [
            {"viewclass": "MDMenuItem",
            "text": "Label1"},
            {"viewclass": "MDMenuItem",
            "text": "Label2"},
            ]
        caller = self.manager.get_screen('main_screen').ids.botao
        self.dropdown = MDDropdownMenu(caller=caller, items=menu_labels,
            width_mult=4)
        # self.dropdown.open()

    def drop(self):
        self.tres_pontos()
        self.dropdown.open()
# --------------------------------------------------------------------------------

    def chess_initt(self):
        try:
            results = []
            moves = []
            dates = []
            speed = []
            games = []
            my_elo = []
            my_color = []
            opponent_elo = []
            opponent_country = []
            opponent_name = []

            # self.nick = nick
            # nick = """heru007"""
            chesscom = """https://www.chess.com/games/archive/""" + self.nick + """?
                            gameOwner=other_game&gameTypes%5B0%5D=chess960
                            &gameTypes%5B1%5D=daily&gameType=live&page={}"""
            # print(chesscom)
            for i in range(1,5):

                # Get the page
                text = get(chesscom.format(i)).text
                # Soupifyd
                b = BeautifulSoup(text, 'html.parser')
                
                # Collect results
                results += pull_results(b)
                moves += pull_moves(b)
                dates += pull_dates(b)
                speed += pull_speed(b)
                games += pull_game_links(b)
                my_elo += pull_player_stats(b)[0]
                opponent_elo += pull_player_stats(b)[1]
                opponent_country += pull_player_stats(b)[2]
                opponent_name += pull_player_stats(b)[3]
                my_color += pull_player_stats(b)[4]
                
                # Check progress
                # print(i)
        
            # Make Df
            d = {'date': dates,
                'result': results,
                'moves': moves,
                'speed': speed,
                'link': games,
                'my_elo': my_elo,
                'opponent_elo': opponent_elo,
                'opponent_country': opponent_country,
                'opponent_name': opponent_name,
                'color': my_color
            }

            games_df = DataFrame(d)

            # Escreve as partidas em arquivo .csv
            games_df.to_csv(path_or_buf='chess_games.csv')

        except Exception:
            self.dialog = None
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Oops! Algo pode ter dado errado",
                    radius=[20, 7, 20, 7],
                )
                self.dialog.open()

    def matrix(self,importar, plott):

        if importar == 1:
            self.chess_initt

        if plott == 0:
            self.games_df = read_csv('chess_games.csv', index_col=0)

            self.games_df.set_index(self.games_df.index[::-1], drop=True, inplace=True)
            self.games_df['date'] = to_datetime(self.games_df['date'])

            speed_games = self.games_df[self.games_df.speed=='10 min']
            speed_games.reset_index(drop=True, inplace=True)
            speed_games.set_index(speed_games.index[::-1], drop=True, inplace=True)

            speed_games['my_elo_ma'] = speed_games['my_elo'][::-1].rolling(window=30).mean()
            speed_games['result'] = Series(where(speed_games.result.values == 'win', 1, 0), speed_games.index)

            # set_style("whitegrid")
            # figure(figsize=(13, 7))

            # lineplot(y='my_elo', 
            #             x=speed_games.index,
            #             data=speed_games, 
            #             color='darkslategray')

            # lineplot(y='my_elo_ma', 
            #             x=speed_games.index,
            #             data=speed_games, 
            #             color='red')

            # xlabel('Number of Games', fontsize=11)
            # ylabel('My Elo', fontsize=13)
            # title('My Elo Over Time', fontsize=13)
            # xlim(-20)

            # legend(['elo', '30-day MA'])

            # style.context('dark_background')

            figure(figsize=(13, 7))
            plot(speed_games.index,speed_games['my_elo'],'darkslategray',speed_games.index,speed_games['my_elo_ma'],'red')
            grid(True)
            xlabel('Number of Games', fontsize=20)
            ylabel('My Elo', fontsize=20)
            title('My Elo Over Time', fontsize=24)
            xlim(-20)
            legend(['elo', '30-day MA'],fontsize=20)
            subplots_adjust(bottom=0.14)
            xticks(fontsize=24)
            yticks(fontsize=24)
            savefig('teste1.png')

        elif plott == 1:
            self.games_df = read_csv('chess_games.csv', index_col=0)

            self.games_df.set_index(self.games_df.index[::-1], drop=True, inplace=True)
            self.games_df['date'] = to_datetime(self.games_df['date'])

            speed_games = self.games_df[self.games_df.speed=='10 min']
            speed_games.reset_index(drop=True, inplace=True)
            speed_games.set_index(speed_games.index[::-1], drop=True, inplace=True)

            speed_games['my_elo_ma'] = speed_games['my_elo'][::-1].rolling(window=30).mean()
            speed_games['result'] = Series(where(speed_games.result.values == 'win', 1, 0), speed_games.index)

            figure(figsize=(13, 7))
            quant = speed_games['opponent_country'].value_counts()
            quant.iloc[0:10].sort_values().plot(kind = 'barh')
            xlabel('Country', fontsize=24)
            ylabel('Number of Games', fontsize=24)
            title('Games against Different Countries', fontsize=26)
            subplots_adjust(left=0.3)
            xticks(fontsize=24)
            yticks(fontsize=24)
            savefig('barra1.png')

    def g_bar(self):

        # self.box1.clear_widgets()

        self.games_df = read_csv('chess_games.csv', index_col=0)

        w = Counter(self.games_df['color'])['white']
        b = Counter(self.games_df['color'])['black']

        # figure(figsize=(13, 17))
        self.fig3, ax = subplots()

        size = 0.3
        vals = array([[w], [b]])

        cmap = get_cmap("tab20c")
        outer_colors = cmap(arange(3)*4)

        ax.pie(vals.sum(axis=1), radius=1.5, colors=outer_colors, shadow=True,
            wedgeprops=dict(width=size, edgecolor='w'),startangle=90)

        # ax.set(aspect="equal", title='Partidas Jogadas')
        sizes = vals/sum(vals)*100
        labels = [r'Brancas', r'Pretas']

        legend( loc = 'center', labels=['%s, %1.1f %%' % (l, s) for l, s in zip(labels, sizes)],
         title=('Partidas Jogadas'),fontsize=20, title_fontsize=20)

        title("Rondan1000", x=0.5,y=0.7,fontsize=28)

        # self.box1.add_widget(FigureCanvasKivyAgg(self.fig3,size_hint=(1.8,1),pos_hint={"top":0.98}))
        # self.box1.add_widget(FigureCanvasAgg(self.fig3))
        # canvas = self.fig3.canvas
        # canvas.draw()
        savefig('pizza.png')
        # self.fig3 = Image(source = 'pizza.jpg')
        # self.fig3.size_hint_y = 1.06
        # self.box1.add_widget(self.fig3)

        # aa = self.manager.get_screen('main_screen').ids.label1.opacity
        # print(aa)
        # aa = 0