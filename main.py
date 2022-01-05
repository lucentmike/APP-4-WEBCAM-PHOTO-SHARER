from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from fileshare import FileSharer
import time

#Loads the kivy file
Builder.load_file('files/frontend.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        filepath =f"images/{current_time}.png"
        self.ids.camera.export_to_png(filepath)

class ImageScreen(Screen):
    pass





#Creates the RootWidget, subclass of ScreenManager (neccesary) 
class RootWidget(ScreenManager):
    pass


#Creates the MainApp, subclass of App (neccesary)
class MainApp(App):

    def build(self):
        return RootWidget()

#Runs the MainApp
MainApp().run() 