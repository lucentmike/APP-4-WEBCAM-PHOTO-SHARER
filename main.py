from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from fileshare import FileSharer
from kivy.core.clipboard import Clipboard

import time
import webbrowser

#Loads the kivy file
Builder.load_file('files/frontend.kv')


class CameraScreen(Screen):
    def start(self):
        """
        Turns on the camera and changes button text

        """
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture
        self.ids.camera.opacity = 1

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None
        self.ids.camera.opacity = 0

        """
        Turns on the camera and changes button text

        """

    def capture(self):
        """
        Captures a picture, set the name to do current date and time and saves the picture. Then switches to the second screen and sets the backround image to the picure

        """
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath =f"images/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath

class ImageScreen(Screen):

    link_message = "Create a link first"

    def create_link(self):
        """
        Takes the filepath and uploads it to filestack using API.
        Then displays the url

        """
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        fileshare = FileSharer(filepath=file_path)
        self.url = fileshare.share()
        self.ids.link.text = self.url

    def copy_link(self):
        """
        Copys URL to clipboard
        """
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        """
        using webbrowser to open URL
        """
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message


#Creates the RootWidget, subclass of ScreenManager (neccesary) 
class RootWidget(ScreenManager):
    pass


#Creates the MainApp, subclass of App (neccesary)
class MainApp(App):

    def build(self):
        return RootWidget()

#Runs the MainApp
MainApp().run() 