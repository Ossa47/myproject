from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen, ScreenManager
from funcs import Encrypt



class Caesar_Screen(Screen):
    pass

class Aes_Screen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Caesar_Screen(name='Caesar'))
sm.add_widget(Aes_Screen(name='Aes'))


class CryptoMD(MDApp):

    def __init__(self, **kwargs):
        self.Encrypt = Encrypt()
        self.title = 'Crypto'
        self.theme_cls.primary_palette = "Purple"
        super().__init__(**kwargs)

    def out_encrypt(self, Text, key):
        obj = Encrypt()
        Text = Text.lower()
        key = key
        Key = int(key)
        out_encrypted = obj.encrypt(Text, key)
        self.root.ids.screen_manager.get_screen("Caesar_Screen").ids.output.text = out_encrypted

    def out_decrypt(self, Text, key):
        obj = Encrypt()
        Text = Text.lower()
        key = key
        Key = int(key)
        out_decrypted = obj.decrypt(Text, key)
        self.root.Caesar.ids.output.text = out_decrypted


if __name__ == '__main__':
    CryptoMD().run()