import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
#from matplotlib.figure import Figure
#from numpy import arange, sin, pi
from kivy.app import App

import numpy as np
#from kivy.garden.matplotlib import FigureCanvasKivyAgg
#from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import matplotlib.pyplot as plt

"""
I am trying to encapsulate the following lines of code that
create the bar graph into a class GT that I can use as a widget.
"""

# _________________________________________________________
def press(event):
    print('press released from test', event.x, event.y, event.button)

def release(event):
    print('release released from test', event.x, event.y, event.button)

def resize(event):
    print('resize from mpl ', event)


N = 5
menMeans = (20, 35, 30, 35, 27)
menStd = (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

womenMeans = (25, 32, 34, 20, 25)
womenStd = (3, 5, 2, 3, 3)

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                '%d' % int(height), ha='center', va='bottom')

fig.canvas.mpl_connect('button_press_event', press)
fig.canvas.mpl_connect('button_release_event', release)
fig.canvas.mpl_connect('resize_event', resize)

canvas = fig.canvas


def callback(instance):
    autolabel(rects1)
    canvas.draw()
# _________________________________________________________


class MatplotlibTest(App):
    title = 'Simpler Matplotlib Test'

    def build(self):
        fl = BoxLayout(orientation="vertical")
        a = Button(text="Run", height=40, size_hint_y=None)
        a.bind(on_press=callback)
        b = Label(text="Feedback goes here", height=100, size_hint_y=0.2)
        #fl.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        fl.add_widget(canvas) # Graph drawing area
        fl.add_widget(b) # Feedback text area
        fl.add_widget(a) # Run button
        """
        Here for adding the graph, I would like to have,
            gt = GT()
            fl.add_widget(gt)
        """
        return fl

if __name__ == '__main__':
    MatplotlibTest().run()

