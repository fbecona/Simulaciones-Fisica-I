from graphics import *
from math import *
import time

#	Simulacion de movimiento de una particula
#	con Movimiento Rectilíneo Uniforme 


def FuerzaX(t,t0,M,X,V):
	g = 9.81
	b = 0.05
	return M*g-b*V

def main():
	
	win = GraphWin("MRU", 400, 300)							# Defino una ventana donde se simulará el movimiento
	
	T = 10														# tiempo de la simulacion
	
	M = 1
	X0 = 200
	Y0 = 280
	V0 = -60
	
	c = Circle(Point(X0,Y0),25)									# dibujo un círculo en la posición inicial
	c.draw(win)
	
	win.getMouse() 												# La simulacion comienza con un clic sobre la ventana
	
	t0 = time.time()											# Se registra el tiempo inicial de la simulacion
	t = t0
	
	DeltaT = 1/60												# La posición de la particula es evaluada 10 veces por segundo
	n = 0														# Indice utilizado para contar las iteraciones
	
	# Inicialización de velocidad para la iteración
	V_N = V0
	Y_N = Y0
	X_N = X0
	
	while(t < t0 + T):											# Simulacion de T segundos
		
		t = time.time()											# Evaluo el tiempo de simulacion
		
		if(t >= t0 + n * DeltaT):								# El >= es importante para asegurar que la evaluación de la posición se hace
																# inmediatamente después de t0 + n * DeltaT
			
			
			V_NN = V_N + DeltaT*FuerzaX(t,t0,M,X_N,V_N)/M													
			Dy = V_N*DeltaT
			Y_N = Y_N + Dy										# Actualizo el valor de la posicion (para el clalculo de la fuerza)
			V_N = V_NN
			
			c.move(0,Dy)										# Desplaza la particula en la direccion horizontal
			
			n = n + 1
	
		
	win.close()

	
main()
