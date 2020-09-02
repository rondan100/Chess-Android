from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np
from kivy.uix.widget import Widget

from kivy.core.window import Window 

Window.size = (350, 650)

KV = '''
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "Example Tabs"

    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)

    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: False


<Tab>:
    MDIconButton:
        id: icon
        icon: app.icons[0]
        user_font_size: "48sp"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: root.Update()
'''

class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    
class Example(MDApp):
    icons = list(md_icons.keys())[15:30]

    data = {
        "language-python": "Chess.com",
        "language-php": "LiChess",
        "language-cpp": "Chess24",
    }

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for name_tab in self.icons:
            self.root.ids.tabs.add_widget(Tab(text=name_tab))

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        count_icon = [k for k, v in md_icons.items() if v == tab_text]
        instance_tab.ids.icon.icon = count_icon[0]

Example().run()