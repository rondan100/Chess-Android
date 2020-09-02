
import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas
import matplotlib.pyplot as plt
from kivy.core.window import Window

from chess_init import chess_initt, speed_games, pd, sns, plt, np


class PlotApp(App):
    def build(self):
        sv = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))

        layout = GridLayout(cols=1, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        fig1, ax1 = plt.subplots()
        ax1.plot([1, 2, 3], [1, 6, 7])
        my_mpl_kivy_widget = FigureCanvas(fig1)

        bx1 = BoxLayout(size_hint=(None, None), size=(Window.width, Window.height/1.2))
        bx1.add_widget(my_mpl_kivy_widget)

        layout.add_widget(bx1)

        
        fig2, ax2 = plt.subplots()
        ax2.plot([1, 2, 3], [1, 6, 7])
        my_mpl_kivy_widget2 = FigureCanvas(fig2)

        bx2 = BoxLayout(size_hint=(None, None), size=(Window.width, Window.height/1.2))
        bx2.add_widget(my_mpl_kivy_widget2)

        layout.add_widget(bx2)

        sv.add_widget(layout)
        return sv
PlotApp().run()


