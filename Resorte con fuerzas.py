from graphics import *
from math import *
import time

#	Simulacion de movimiento de una particula
#	con Movimiento Rectilíneo Uniforme


def FuerzaPeso(t,t0,M,X,V, K, XX, LL):
	g = 9.81
	return M*g - K*(XX-LL)


def main():

	win = GraphWin("Caída Libre", 600, 600)							# Defino una ventana donde se simulará el movimiento

	T = 30														# tiempo de la simulacion

	K = 20
	M = 100
	LL = 200
	X0 = 300
	Y0 = 300
	V0 = -60

	c = Circle(Point(X0,Y0),50)									# dibujo un círlo en la posición inicial
	c.draw(win)

	win.getKey()

	 													# La simulacion comienza con un clic sobre una tecla

	t0 = time.time()											# Se registra el tiempo inicial de la simulacion
	t = t0

	DeltaT = 1/100												# La posición de la particula es evaluada 10 veces por segundo
	n = 0														# Indice utilizado para contar las iteraciones

	# Inicialización de velocidad para la iteración
	V_N = V0
	X_N = X0
	XX_N = X0

	while(t < t0 + T):											# Simulacion de T segundos

		t = time.time()											# Evaluo el tiempo de simulacion

		if(t >= t0 + n * DeltaT):								# El >= es importante para asegurar que la evaluación de la posición se hace
																# inmediatamente después de t0 + n * DeltaT
			V_NN = V_N + DeltaT*FuerzaPeso(t,t0,M,X_N,V_N, K, XX_N, LL)/M
			Dy = V_N*DeltaT
			XX_N = XX_N + Dy										# Actualizo el valor de la posicion (para el clalculo de la fuerza)
			V_N = V_NN

			c.move(0,Dy)										# Desplaza la particula en la direccion horizontal

			n = n + 1

	win.close()


main()



