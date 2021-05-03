i want to reference an MDLabel with `id: output` to print the result on it instead of the eerminal, I did that with this line of code
`self.root.ids.screen_manager.get_screen("Caesar_Screen").ids.output.text = out_encrypted`
but I always get this error message:



C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\Scripts\python.exe C:\Users\Samoo\PycharmProjects\CryptoMD2\main.py
[INFO   ] [Logger      ] Record log in C:\Users\Samoo\.kivy\logs\kivy_21-05-03_57.txt
[INFO   ] [deps        ] Successfully imported "kivy_deps.gstreamer" 0.3.2
[INFO   ] [deps        ] Successfully imported "kivy_deps.angle" 0.3.0
[INFO   ] [deps        ] Successfully imported "kivy_deps.glew" 0.3.0
[INFO   ] [deps        ] Successfully imported "kivy_deps.sdl2" 0.3.1
[INFO   ] [Kivy        ] v2.0.0
[INFO   ] [Kivy        ] Installed at "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\__init__.py"
[INFO   ] [Python      ] v3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)]
[INFO   ] [Python      ] Interpreter at "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\Scripts\python.exe"
[INFO   ] [KivyMD      ] v0.104.1
[INFO   ] [Factory     ] 186 symbols loaded
[INFO   ] [Image       ] Providers: img_tex, img_dds, img_sdl2, img_pil (img_ffpyplayer ignored)
[INFO   ] [Window      ] Provider: sdl2
[INFO   ] [GL          ] Using the "OpenGL" graphics system
[INFO   ] [GL          ] GLEW initialization succeeded
[INFO   ] [GL          ] Backend used <glew>
[INFO   ] [GL          ] OpenGL version <b'4.3.0 - Build 20.19.15.5126'>
[INFO   ] [GL          ] OpenGL vendor <b'Intel'>
[INFO   ] [GL          ] OpenGL renderer <b'Intel(R) HD Graphics 4600'>
[INFO   ] [GL          ] OpenGL parsed version: 4, 3
[INFO   ] [GL          ] Shading version <b'4.30 - Build 20.19.15.5126'>
[INFO   ] [GL          ] Texture max size <16384>
[INFO   ] [GL          ] Texture max units <32>
[INFO   ] [Window      ] auto add sdl2 input provider
[INFO   ] [Window      ] virtual keyboard not allowed, single mode, not docked
[INFO   ] [Text        ] Provider: sdl2
[INFO   ] [GL          ] NPOT texture support is available
[INFO   ] [Base        ] Start application main loop
B                                                              #this is the message I want to display on the Label.

[INFO   ] [Base        ] Leaving application in progress...
 Traceback (most recent call last):
   File "kivy\properties.pyx", line 861, in kivy.properties.ObservableDict.__getattr__
 KeyError: 'screen_manager'
 
 During handling of the above exception, another exception occurred:
 
 Traceback (most recent call last):
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\main.py", line 46, in <module>
     CryptoMD().run()
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\app.py", line 950, in run
     runTouchApp()
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\base.py", line 582, in runTouchApp
     EventLoop.mainloop()
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\base.py", line 347, in mainloop
     self.idle()
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\base.py", line 391, in idle
     self.dispatch_input()
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\base.py", line 342, in dispatch_input
     post_dispatch_input(*pop(0))
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\base.py", line 248, in post_dispatch_input
     listener.dispatch('on_motion', etype, me)
   File "kivy\_event.pyx", line 709, in kivy._event.EventDispatcher.dispatch
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\core\window\__init__.py", line 1412, in on_motion
     self.dispatch('on_touch_down', me)
   File "kivy\_event.pyx", line 709, in kivy._event.EventDispatcher.dispatch
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\core\window\__init__.py", line 1428, in on_touch_down
     if w.dispatch('on_touch_down', touch):
   File "kivy\_event.pyx", line 709, in kivy._event.EventDispatcher.dispatch
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\uix\screenmanager.py", line 1198, in on_touch_down
     return super(ScreenManager, self).on_touch_down(touch)
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\uix\widget.py", line 545, in on_touch_down
     if child.dispatch('on_touch_down', touch):
   File "kivy\_event.pyx", line 709, in kivy._event.EventDispatcher.dispatch
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\uix\relativelayout.py", line 297, in on_touch_down
     ret = super(RelativeLayout, self).on_touch_down(touch)
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\uix\widget.py", line 545, in on_touch_down
     if child.dispatch('on_touch_down', touch):
   File "kivy\_event.pyx", line 709, in kivy._event.EventDispatcher.dispatch
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\uix\widget.py", line 545, in on_touch_down
     if child.dispatch('on_touch_down', touch):
   File "kivy\_event.pyx", line 709, in kivy._event.EventDispatcher.dispatch
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\uix\widget.py", line 545, in on_touch_down
     if child.dispatch('on_touch_down', touch):
   File "kivy\_event.pyx", line 709, in kivy._event.EventDispatcher.dispatch
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\uix\behaviors\button.py", line 138, in on_touch_down
     if super(ButtonBehavior, self).on_touch_down(touch):
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\uix\widget.py", line 545, in on_touch_down
     if child.dispatch('on_touch_down', touch):
   File "kivy\_event.pyx", line 709, in kivy._event.EventDispatcher.dispatch
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\uix\widget.py", line 545, in on_touch_down
     if child.dispatch('on_touch_down', touch):
   File "kivy\_event.pyx", line 709, in kivy._event.EventDispatcher.dispatch
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivymd\uix\behaviors\ripplebehavior.py", line 231, in on_touch_down
     return super().on_touch_down(touch)
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivymd\uix\button.py", line 961, in on_touch_down
     return super().on_touch_down(touch)
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\uix\behaviors\button.py", line 151, in on_touch_down
     self.dispatch('on_press')
   File "kivy\_event.pyx", line 705, in kivy._event.EventDispatcher.dispatch
   File "kivy\_event.pyx", line 1248, in kivy._event.EventObservers.dispatch
   File "kivy\_event.pyx", line 1132, in kivy._event.EventObservers._dispatch
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\venv\lib\site-packages\kivy\lang\builder.py", line 57, in custom_callback
     exec(__kvlang__.co_value, idmap)
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\cryptomd.kv", line 100, in <module>
     app.out_encrypt(Text.text, key.text) if key.text != "" else None
   File "C:\Users\Samoo\PycharmProjects\CryptoMD2\main.py", line 34, in out_encrypt
     self.root.ids.screen_manager.get_screen("Caesar_Screen").ids.output.text = out_encrypted
   File "kivy\properties.pyx", line 864, in kivy.properties.ObservableDict.__getattr__
 AttributeError: 'super' object has no attribute '__getattr__'
 
 
