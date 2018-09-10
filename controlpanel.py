#!/usr/bin/python

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

from kivy.core.window import Window

from kivy.properties import NumericProperty

#import RPi.GPIO as gpio

def iniciar_pines():
	pines = [4,5,12,13,16,17,18,21,22,23,25,26]
	print('#[:)]# Estableciendo modo gpio a BCM')
	#gpio.setmode(gpio.BCM)
	print('#[:)]# Estableciendo pines de salida')
	for pin in pines:
		pass
		#gpio.setup(pin, gpio.OUT, initial=gpio.LOW)
	print('#[:)]# Sistema gpio inciado')


class MainPanelWidget(GridLayout):
	pass


class RPIButton(ToggleButton):
	pin = NumericProperty(0)
	
	def on_press(self):
		estadoPin = True if self.state=='down' else False
		#gpio.output(self.pin, self.estadoPin)
		print('#[:)]# Pulsado botón {0} con PIN {1} y estado {2}'
				.format(self.text, self.pin, estadoPin))


class ControlPanelApp(App):
	def build(self):
		return MainPanelWidget()


if __name__ == '__main__':
	#Window.fullscreen = 'auto'
	iniciar_pines()
	ControlPanelApp().run()
