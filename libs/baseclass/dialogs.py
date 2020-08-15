import os
import socket

from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem
from libs.baseclass.list_items import KitchenSinkOneLineLeftAvatarItem
from kivymd.uix.snackbar import Snackbar


class KitchenSinkDialogsCustomContent(BoxLayout):
    pass


class KitchenSinkItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False


class KitchenSinkDialogs(Screen):
    app = ObjectProperty()
    simple_dialog = None
    alert_dialog = None
    custom_dialog = None
    confirmation_dialog = None

    def cliente(self, soquete):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('192.168.0.22', 12345))
        except Exception:
            Snackbar(text="Falha ao criar conexão.").show()
        else:
            Snackbar(text="Conexão estabelecida").show()
            s.send(bytes("Cliente enviouuu!!!", "utf-8"))

        self.alert_dialog.dismiss()

    def show_example_simple_dialog(self):
        if not self.simple_dialog:
            self.simple_dialog = MDDialog(
                title="Set backup account",
                type="simple",
                items=[
                    KitchenSinkOneLineLeftAvatarItem(
                        text="user01@gmail.com",
                        source=f"{os.environ['KITCHEN_SINK_ASSETS']}py.png",
                    ),
                    KitchenSinkOneLineLeftAvatarItem(
                        text="user02@gmail.com",
                        source=f"{os.environ['KITCHEN_SINK_ASSETS']}py.png",
                    ),
                    KitchenSinkOneLineLeftAvatarItem(
                        text="Add account",
                        source=f"{os.environ['KITCHEN_SINK_ASSETS']}py.png",
                    ),
                ],
            )
        self.simple_dialog.open()

    def show_example_alert_dialog(self):
        if not self.alert_dialog:
            self.alert_dialog = MDDialog(
                title="Reset settings?",
                text="This will reset your device to its default factory settings.",
                buttons=[
                    MDFlatButton(
                        text="CANCELAR",
                        text_color=self.app.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="ACEITAR",
                        text_color=self.app.theme_cls.primary_color,
                        on_release=self.cliente,
                    ),
                ],
            )
        self.alert_dialog.open()
