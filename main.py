from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

#Loads the kivy file
Builder.load_file('frontend.kv')

#Creates a class for the first screen, will do one for every screen
class FirstScreen(Screen):
    def search_image(self):
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