from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt

# plt.plot([1, 23, 2, 4])
# plt.ylabel('some numbers')

# class MyApp(App):

    # def build(self):
    #     box = BoxLayout()
    #     box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
    #     return box

# MyApp().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'settings'

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'Back to menu'
            on_press:
                # root.manager.transition.direction = 'right'
                # root.manager.current = 'menu'
                self.buildd()
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))

class TestApp(App):

    def build(self):
        return sm

    def buildd(self):
        plt.plot([1, 23, 2, 4])
        plt.ylabel('some numbers')
        add_widget(FigureCanvasKivyAgg(plt.gcf()))


if __name__ == '__main__':
    TestApp().run()