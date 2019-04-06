#Federico Becoña
#Julio Suaya
#Rodrigo López

#Escala 1m = 200Px

from graphics import *
import math
import time

def FuerzaX(t,t0,M,X,CX1,CX2,Y,CY1,CY2,VX):
    k=2
    l=1
    b=0.1
    
    #Calculo L1
    L1=math.sqrt((Y-CY1)**2+(X-CX1)**2)
    #Calculo L2
    L2=math.sqrt((Y-CY2)**2+(X-CX2)**2)
    
    FrozX=-b*VX
    Fr1x=-k*(L1-l)*(X-CX1)/L1
    Fr2x=-k*(L2-l)*(X-CX2)/L2
    
    return Fr1x+Fr2x+FrozX

def FuerzaY(t,t0,M,X,CX1,CX2,Y,CY1,CY2,VY):
    k=2
    l=1
    b=0.1
    g=9.81
    
    #Calculo L1
    L1=math.sqrt((Y-CY1)**2+(X-CX1)**2)
    #Calculo L2
    L2=math.sqrt((Y-CY2)**2+(X-CX2)**2)
    print([L1,L2])

    FrozY=-b*VY
    Fr1y=-k*(L1-l)*(Y-CY1)/L1
    Fr2y=-k*(L2-l)*(Y-CY2)/L2
    
    return Fr1y+Fr2y-M*g+FrozY

def main():
    win = GraphWin("Sistema de resortes", 700, 500)
    win.setCoords(0, 0, 700, 1400)
    
    #Tiempo de simulacion
    T = 100
    
    #Masa
    M = 1
    
    #Coordenadas de los puntos de agarre de los resortes
    CX1 = 0.25
    CY1 = 6.5
    
    CX2 = 3.25
    CY2 = 6.5

    #Coordenadas iniciales del cuerpo
    X0 = CX1+1
    Y0 = CY1
    
    #Velocidad inicial del cuerpo 2m/s hacia abajo
    V0Y = -2
    V0X = 0

    #Dibujo puntos de agarre de los resortes
    d = Circle(Point(CX1*200,CY1*200),3)
    d.draw(win)
    e = Circle(Point(CX2*200,CY2*200),3)
    e.draw(win)
    
    #Dibujo el cuerpo
    c = Circle(Point(X0*200,Y0*200),10)
    c.draw(win)
    
    win.getMouse()
    t0 = time.time()
    t = t0

    DeltaT = 1/150
    n = 0

    # Condiciones iniciales para la iteración
    VY_N = V0Y
    VX_N = V0X
    
    Y_N = Y0
    X_N = X0
    
    
    
    while(t < t0 + T):
        t = time.time()
        if(t >= t0 + n * DeltaT):
            ##Movimiento en Y
            VY_NN = VY_N + DeltaT*FuerzaY(t,t0,M,X_N,CX1,CX2,Y_N,CY1,CY2,VY_N)/M
            ##Movimiento en X
            VX_NN = VX_N + DeltaT*FuerzaX(t,t0,M,X_N,CX1,CX2,Y_N,CY1,CY2,VX_N)/M
            

            ##Valores Y
            Dy = VY_N*DeltaT
            Y_N = Y_N + Dy
            VY_N = VY_NN
            
            
            ##Valores X
            Dx = VX_N*DeltaT
            X_N = X_N + Dx
            VX_N = VX_NN

            win.plot(X_N*200,Y_N*200)
            c.move(Dx*200,Dy*200)
            n = n + 1
            
    win.getMouse()
    win.close()

main()
