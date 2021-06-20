from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from Caesar_funcs import Encrypt



class Caesar_Screen(Screen):
    pass


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
        self.root.get_screen("Caesar_Screen").ids.output.text = out_encrypted

    def out_decrypt(self, Text, key):
        obj = Encrypt()
        Text = Text.lower()
        key = key
        Key = int(key)
        out_decrypted = obj.decrypt(Text, key)
        self.root.get_screen("Caesar_Screen").ids.output.text = out_decrypted


if __name__ == '__main__':
    CryptoMD().run()
