#Federico Becoña
#Rodrigo López
#Pablo Luchinetti
#Julio Suaya

from graphics import *
import math
import time

def FuerzaY(p1,p2,p3,V):
    k=100
    b=0.2
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

    return Fr1y+Fr2y+FrozY


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
    CNT_PART = 80

    lst_part = []
    for n_part in range(CNT_PART):
        pos_x = 20+((WIDTH-40)/(CNT_PART-1))*n_part
        circulo=Circle(Point(pos_x,HEIGHT/2),5)
        lst_part.append([circulo,0])
        circulo.draw(win)
        circulo.setFill("red")


    #Click para comenzar
    win.getMouse()

    t0 = time.time()
    t = t0

    #Cuadros por segundo
    DeltaT = 1/240
    n = 0

    ##
    A = 25
    periodo = 0.5
    w = 2*math.pi/periodo
    yy = 0

    while(t < t0 + T):
        t = time.time()
        if(t >= t0 + n * DeltaT):

            if DeltaT*n  <=  2*math.pi/w :

                y = A*(1-math.cos(w*(n * DeltaT)))

                lst_part[0][0].move(0,y-yy)
                yy = y


            for n_part in range(1,CNT_PART-1):
                ##Movimiento
                VY_NN = lst_part[n_part][1] + DeltaT*FuerzaY(lst_part[n_part-1][0],lst_part[n_part][0],lst_part[n_part+1][0],lst_part[n_part][1])/M
                Dy = lst_part[n_part][1]*DeltaT
                lst_part[n_part][1] = VY_NN
                lst_part[n_part][0].move(0,Dy)

            n += 1/4
            
    win.close()
main()
