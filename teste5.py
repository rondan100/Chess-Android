from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons

KV = '''
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "Example Tabs"

    MDTabs:
        id: tabs


<Tab>:

    MDIconButton:
        id: icon
        icon: "arrow-right"
        user_font_size: "48sp"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.switch_tab()
'''


class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class Example(MDApp):
    icons = list(md_icons.keys())[15:30]

    def build(self):
        self.iter_list = iter(list(self.icons))
        return Builder.load_string(KV)

    def on_start(self):
        for name_tab in list(self.icons):
            self.root.ids.tabs.add_widget(Tab(text=name_tab))

    def switch_tab(self):
        '''Switching the tab by name.'''

        try:
            self.root.ids.tabs.switch_tab(next(self.iter_list))
        except StopIteration:
            pass


Example().run()