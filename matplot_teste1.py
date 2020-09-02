from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt

from chess_init import chess_initt, speed_games, pd, sns, plt, np


plt.plot([1, 23, 2, 4])
plt.ylabel('some numbers')

# sns.set_style("whitegrid")
# plt.figure(figsize=(13, 7))

# sns.lineplot(y='my_elo', 
#              x=speed_games.index,
#              data=speed_games, 
#              color='darkslategray')

# sns.lineplot(y='my_elo_ma', 
#              x=speed_games.index,
#              data=speed_games, 
#              color='red')

# plt.xlabel('Number of Games', fontsize=13)
# plt.ylabel('My Elo', fontsize=13)
# plt.title('My Elo Over Time', fontsize=15)
# plt.xlim(-20)

# plt.legend(['elo', '30-day MA'])


class MyApp(App):

    def build(self):
        box = BoxLayout()
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        return box

MyApp().run()
