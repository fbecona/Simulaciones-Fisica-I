#Federico Becoña
#Rodrigo López
#Pablo Luchinetti
#Julio Suaya

from graphics import *
import math
import time

def Fuerza(p1,p2,p3,V):
    k=25
    b=0.1
    l=0

    #Particula anterior
    p1_x = p1.getCenter().getX()
    p1_y = p1.getCenter().getY()

    #Particula central
    p2_x = p2.getCenter().getX()
    p2_y = p2.getCenter().getY()

    #Particula siguiente
    p3_x = p3.getCenter().getX()
    p3_y = p3.getCenter().getY()


    #Calculo L1
    L1=math.sqrt((p2_y - p1_y)**2 + (p2_x - p1_x)**2)
    #Calculo L2
    L2=math.sqrt((p2_y - p3_y)**2 + (p2_x - p3_x)**2)

    FrozY=-b*V

    Fr1y=-k*(L1-l)*(p2_y - p1_y)/L1
    Fr2y=-k*(L2-l)*(p2_y - p3_y)/L2
    
    return [Fr1y+Fr2y,-k*(L2-l)]


def main():

    #Defino las propiedades de la ventana y el sistema de coordenadas
    WIDTH = 1200
    HEIGHT = 600
    win = GraphWin("Entregable Final",WIDTH,HEIGHT)
    win.setCoords(0,0,WIDTH,HEIGHT)

    aLine = Line(Point(0,HEIGHT/2),Point(WIDTH,HEIGHT/2))
    aLine.draw(win)
    aLine.setFill("blue")

    #Tiempo de simulacion
    T = 1000

    #Masa
    M = 1

    #Cantidad de particulas
    CNT_PART = 100
    #Amplitud
    A = 40
    
    lst_part = []
    for n_part in range(CNT_PART):
        pos_x = 20+((WIDTH-40)/(CNT_PART-1))*n_part
        circulo=Circle(Point(pos_x,HEIGHT/2+A - A/CNT_PART*n_part),5)
        lst_part.append([circulo,0])
        circulo.draw(win)
        circulo.setFill("red")

    #Click para comenzar
    win.getMouse()

    t0 = time.time()
    t = t0

    #Cuadros por segundo
    DeltaT = 1/260
    n = 0
 
    ##
    w = 3
    
    DeltaL = math.sqrt((lst_part[CNT_PART-1][0].getCenter().getX()-lst_part[0][0].getCenter().getX())**2+A**2)
    mu = (M*(CNT_PART-1))/DeltaL
    
    yy = A
    variable = True

    while(t < t0 + T):
        t = time.time()
        if(t >= t0 + n * DeltaT):
            
            ##Oscilacion
            y = A*math.cos(w*(n * DeltaT))
            lst_part[0][0].move(0,y-yy)
            yy = y


            for n_part in range(1,CNT_PART-1):
                Fuerzas = Fuerza(lst_part[n_part-1][0],lst_part[n_part][0],lst_part[n_part+1][0],lst_part[n_part][1])

                ##Movimiento
                VY_NN = lst_part[n_part][1] + DeltaT*Fuerzas[0]/M
                Dy = lst_part[n_part][1]*DeltaT
                lst_part[n_part][1] = VY_NN
                lst_part[n_part][0].move(0,Dy)

    
                ##Velocidades de la onda
                if lst_part[CNT_PART-2][0].getCenter().getY()!= HEIGHT/2+A - A/CNT_PART*(CNT_PART-2) and variable == True:
                    variable = False
                
                    #Tomando desde la primera hasta la penúltima partícula
                    v1 = (lst_part[CNT_PART-2][0].getCenter().getX()-lst_part[0][0].getCenter().getX())/(t-t0)
                    print("La velocidad 1 es de " + str(v1))

                    #Calculada con la tensión y mu
                    v2 = math.sqrt(abs(Fuerzas[1])/mu)
                    print("La velocidad 2 es de " + str(v2))
                    
            n += 1

    win.close()
main()
