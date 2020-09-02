import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from matplotlib.figure import Figure
from numpy import arange, sin, pi
from kivy.app import App

import numpy as np
# from matplotlib.mlab import griddata
from kivy.garden.matplotlib.backend_kivy import FigureCanvas,\
                                                NavigationToolbar2Kivy

# from backend_kivy import FigureCanvasKivy as FigureCanvas

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from matplotlib.transforms import Bbox
from kivy.uix.button import Button
from kivy.graphics import Color, Line, Rectangle

import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# fig, ax = plt.subplots()
fig, ax = plt.subplots()

X = np.arange(-508, 510, 203.2)
Y = np.arange(-508, 510, 203.2)
X, Y = np.meshgrid(X, Y)

Z = np.random.rand(6, 6)

plt.contourf(X, Y, Z, 100, zdir='z', offset=1.0, cmap=cm.hot)
plt.colorbar()

ax.set_ylabel('Y [mm]')
ax.set_title('NAILS surface')
ax.set_xlabel('X [mm]')

canvas = fig.canvas



def callback(instance):

    global fig, ax
    # fig, ax = plt.subplots()

    X = np.arange(-508, 510, 203.2)
    Y = np.arange(-508, 510, 203.2)
    X, Y = np.meshgrid(X, Y)

    Z = 1000*np.random.rand(6, 6)
    plt.clf()
    plt.contourf(X, Y, Z, 100, zdir='z', offset=1.0, cmap=cm.hot)
    plt.colorbar()

    # ax.set_ylabel('Y [mm]')
    # ax.set_title('NAILS surface')
    # ax.set_xlabel('X [mm]')

    # canvas = fig.canvas
    canvas.draw()


class MatplotlibTest(App):
    title = 'Matplotlib Test'

    def build(self):
        fl = BoxLayout(orientation="vertical")
        a = Button(text="press me", height=40, size_hint_y=None)
        a.bind(on_press=callback)

        fl.add_widget(canvas)
        fl.add_widget(a)
        return fl

if __name__ == '__main__':
    MatplotlibTest().run()