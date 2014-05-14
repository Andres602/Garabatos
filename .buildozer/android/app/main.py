from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.graphics import Color
from random import randint
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.window import Window


tiempo=75.0


class ThemeBox(Widget):
	hue = NumericProperty(0)
	sat = NumericProperty(0)
	tipo = StringProperty("cajas")


class Button(Widget):
	texo = StringProperty("cajas")	

class Label(Widget):
	texto = StringProperty("cajas")	

class Selec(Widget):
	x = NumericProperty(0)
	y = NumericProperty(25)

class PictionaryGame(Widget):
	global tiempo
	persona = ObjectProperty(None)
	cosa   = ObjectProperty(None)
	accion = ObjectProperty(None)
	dificil  = ObjectProperty(None)
	todos   = ObjectProperty(None)
	boton = ObjectProperty(None)
	inicio = ObjectProperty(None)
	fin = ObjectProperty(None)	
	word = ObjectProperty(None)
	circulo = ObjectProperty(None)
	#circulo2 = ObjectProperty(None)
	src=open('words', 'r')
	card=src.readlines()
	s = SoundLoader.load('tada.wav')

	

	i=0
	cont=0
	pressed=False
	tipo=0
	number_card=0
	t_start=False
	t_clock= tiempo
	
	

	def setup_box(self):
		self.persona.hue=.56
		self.persona.tipo="Lugar, Persona, Animal"
		self.cosa.hue=.7
		self.cosa.tipo="Cosa"
		self.accion.hue=.17
		self.accion.tipo="Accion"
		self.dificil.hue=.3
		self.dificil.tipo="Dificil"
		self.todos.hue=1
		self.todos.tipo="Todos Juegan"
		self.boton.texto="Palabra"
		self.inicio.texto="Start"
		self.fin.texto="Stop"
		self.word.texto="Garabatos"
		self.circulo.x=0
		self.circulo.y=9*Window.size[1]/10
		#self.circulo2.x=0
		#self.circulo2.y=9*Window.size[1]/10

	def random_word(self):
		if self.t_start==False:
			self.pressed=True
			self.i=0
			self.cont=0
			self.tipo=randint(0, 4)
			self.number_card=randint(0,len(self.card)-1)

	def start_time(self):
		if self.t_start==False and self.pressed==False:
			self.t_start=True
			self.t_clock=tiempo

	def stop_time(self):
		if self.t_start==True:
			self.t_start=False
			self.boton.texto="Word"
		
		
	def update(self, dt):

		if self.t_start==True:
			self.t_clock=self.t_clock-(1.0/60)
			segundo=int(self.t_clock%60)
			seg=str(segundo)
			if segundo<10:
				seg='0'+ seg
			minuto=int(self.t_clock/60)
			self.boton.texto=str(minuto)+":"+ seg
			if self.t_clock<=0:
				self.s.play()
				self.stop_time()
		

		if self.pressed==True:
			i=self.i
			if i==0:
				self.circulo.y=9*Window.size[1]/10				
			elif i==1:
				self.circulo.y=8*Window.size[1]/10
			elif i==2:
				self.circulo.y=7*Window.size[1]/10
			elif i==3:
				self.circulo.y=6*Window.size[1]/10
			elif i==4:
				self.circulo.y=5*Window.size[1]/10
			self.i=i+1
			self.cont=self.cont+1
			if self.i%5==0:
				self.i=0
			if self.cont==6+self.tipo:
				strings=self.card[self.number_card].split(',')
				self.word.texto=strings[self.tipo]
				self.pressed=False

			
			
				
	

class PictionaryApp(App):
    def build(self):
	game=PictionaryGame()
	game.setup_box()
	Clock.schedule_interval(game.update, 1.0/60)	
        return game


if __name__ == '__main__':
	PictionaryApp().run()
