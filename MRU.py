#Dudas: Que significaría si yo cambio el segundo cero de la posición inicial en X o Y no entiendo que quiere decir eso porque la posición la cambio con el de la izquierda

from graphics import * #cd desktop y el nombre del archivo.py
from math import *
import time

#	Simulacion de movimiento de una particula
#	con Movimiento Rectilíneo Uniforme 


def PosicionX(t,t0):
	X0 = 20		                                                                                        # Posicion inicial
	Vx0 = 1500                                                                                               # Velocidad inicial en m/s (en este ejemplo es constante)

	return X0 + Vx0 * (t - t0)

def PosicionY(t,t0):
	Y0 = 280	                                                                                        # Posicion inicial
	Vy0 = -500
	a= 150
	return Y0 + Vy0 *((t - t0))+ (a*((t - t0)**2)/2)
	

def main():
	
	win = GraphWin("MRU", 1000, 500)						                 # Defino una ventana donde se simulará el movimiento
	
	T = 20												         # tiempo de la simulacion
	
	MPP=1												         # Metros Por Pixel
	
	c = Circle(Point(PosicionX(0,0),PosicionY(0,0)),50)						         # dibujo un círculo en la posición inicial PosicionX(0,0) es la posición en X
	c.draw(win)
	
	win.getKey() 											         # La simulacion comienza con un clic sobre la ventana
	
	t0 = time.time()										         # Se registra el tiempo inicial de la simulacion
	t = time.time()
	
	DeltaT = 1/10000										         # La posición de la particula es evaluada 10000 veces por segundo
	n = 1												         # Indice utilizado para contar las iteraciones
	
	while(t < t0 + T):										         # Simulacion de T segundos
		
		t = time.time()										         # Evaluo el tiempo de simulacion
		
		if(t >= t0 + n * DeltaT):								         # El >= es importante para asegurar que la evaluación de la posición se hace
                                                                                                                 # inmediatamente después de t0 + n * DeltaT
																
			c.move(PosicionX(t,t0)-PosicionX(t-DeltaT,t0),PosicionY(t,t0)-PosicionY(t-DeltaT,t0))        # Desplaza la particula en la direccion horizontal
			n = n + 1
		
	win.close()
	
main()
