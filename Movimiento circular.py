from graphics import *
from math import *
import time

def PosicionX(t,t0):
	X0 = 250                                                                          # Posicion inicial en X
	r = 100																			  # Radio	
	vang = 3.14159265359															  # No pudimos aplicar la función (math.pi)		
	return X0+r*cos(vang*(t-t0))

def PosicionY(t,t0):
	Y0 = 250                                                                          # Posicion inicial en Y
	r = 100																			  # Radio
	vang = 3.14159265359
	return Y0+r*sin(vang*(t-t0))

def main():
	win = GraphWin("MRU", 500, 500)						                         	   # Defino una ventana donde se simulará el movimiento
	
	T = 2												         				       # Tiempo de la simulacion
	
	MPP=1																			   # Metros por Pixel

	c = Circle(Point(PosicionX(0,0),PosicionY(0,0)),20)						         
	c.draw(win)
	
	win.getKey() 											         					# Se activa por toque de tecla, no de mouse.
	
	t0 = time.time()										        			 	    # Se registra el tiempo inicial de la simulacion
	t = time.time()
	
	DeltaT = 1/80										        						# La posición de la particula es evaluada 80 veces por segundo
	n = 1												         				 		# Indice utilizado para contar las iteraciones
	
	while(t < t0 + T):										         					# Simulacion de T segundos
		
		t = time.time()										         					# Evaluo el tiempo de simulacion
		
		if(t >= t0 + n * DeltaT):								         				 # El >= es importante para asegurar que la evaluación de la posición se hace
                                                                                          # inmediatamente después de t0 + n * DeltaT													
			c.move(PosicionX(t,t0)-PosicionX(t-DeltaT,t0),PosicionY(t,t0)-PosicionY(t-DeltaT,t0))    # Desplaza la particula en la direccion horizontal y vertical
			n = n + 1
	win.close()
main()
