# Program to Show how to create a Progressbar in .kv file 

# import kivy module	 
import kivy 
	
# base Class of your App inherits from the App class.	 
# app:always refers to the instance of your application 
from kivy.app import App 
	
# this restrict the kivy version i.e 
# below this kivy version you cannot 
# use the app or software 
kivy.require('1.9.0') 
	
# The ProgressBar widget is used to 
# visualize the progress of some task 
from kivy.uix.progressbar import ProgressBar 

# BoxLayout arranges children in a vertical or horizontal box. 
# or help to put the children at the desired location. 
from kivy.uix.boxlayout import BoxLayout 

# The Clock object allows you to schedule a 
# function call in the future 
from kivy.clock import Clock 

# The Button is a Label with associated actions 
# that is triggered when the button 
# is pressed (or released after a click / touch). 
from kivy.uix.button import Button 

# Popup widget is used to create popups. 
# By default, the popup will cover 
# the whole “parent” window. 
# When you are creating a popup, 
# you must at least set a Popup.title and Popup.content. 
from kivy.uix.popup import Popup 

# A Widget is the base building block 
# of GUI interfaces in Kivy. 
# It provides a Canvas that 
# can be used to draw on screen. 
from kivy.uix.widget import Widget 

# ObjectProperty is a specialised sub-class 
# of the Property class, so it has the same 
# initialisation parameters as it: 
# By default, a Property always takes a default 
# value[.] The default value must be a value 
# that agrees with the Property type. 
from kivy.properties import ObjectProperty 



# Create the widget class 
class MyWidget(Widget): 

	progress_bar = ObjectProperty() 
	
	def __init__(self, **kwa): 
		super(MyWidget, self).__init__(**kwa) 
		
		self.progress_bar = ProgressBar() 
		self.popup = Popup( 
			title ='Download', 
			content = self.progress_bar 
		) 
		self.popup.bind(on_open = self.puopen) 
		self.add_widget(Button(text ='Download', on_release = self.pop)) 

	# the function which works when you clicj = k the button 
	def pop(self, instance): 
		self.progress_bar.value = 1
		self.popup.open() 

	# To continuesly increasing the value of pb. 
	def next(self, dt): 
		if self.progress_bar.value>= 100: 
			return False
		self.progress_bar.value += 1

	def puopen(self, instance): 
		Clock.schedule_interval(self.next, 1 / 25) 

# Create the App class 
class MyApp(App): 
	def build(self): 
		return MyWidget() 

# run the App 
if __name__ in ("__main__"): 
	MyApp().run() 

