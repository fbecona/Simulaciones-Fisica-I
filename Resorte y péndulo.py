from graphics import *
import math
import time

def FuerzaX(t,t0,M,X_N,CX,Y_N,CY,VX_N):
    k=5
    l=20
    L=math.sqrt((Y_N-CY)**2+(X_N-CX)**2)
    #print("Y:"+str(Y-CY))
    #print("X:"+str(X-CX))
    #print(L)
    Frx=k*(L-l)*(CX-X_N)/L
    b = 0.5
    return Frx - b*VX_N

def FuerzaY(t,t0,M,X_N,CX,Y_N,CY,VY_N):
    k=5
    l=20
    L=math.sqrt((Y_N-CY)**2+(X_N-CX)**2)
    Fry=k*(L-l)*(CY-Y_N)/L
    g=9.81
    b = 0.5
    return Fry-M*g - b*VY_N

def main():
    win = GraphWin("RESORTE", 400, 300)
    win.setCoords(0, 0, 400, 300)
    
    #Tiempo de simulacion
    T = 100
    #Masa
    M = 3
    
    #Coordenadas del punto de agarre del resorte
    CX = 200
    CY = 200

    #Coordenadas del punto de agarre del resorte
    X0 = CX-50
    Y0 = CY
    
    #Velocidad inicial
    V0Y = 50
    V0X = 0

    #Dibujo punto de agarre del resorte
    d = Circle(Point(CX,CY),3)
    d.draw(win)

    #Dibujo el cuerpo
    c = Circle(Point(X0,Y0),10)
    c.draw(win)
    
    win.getMouse()
    t0 = time.time()
    t = t0

    DeltaT = 1/60
    n = 0

    # Condiciones iniciales
    VY_N = V0Y
    VX_N = V0X
    
    Y_N = Y0
    X_N = X0
    
    
    
    while(t < t0 + T):
        t = time.time()
        if(t >= t0 + n * DeltaT):
            ##Movimiento en Y
            VY_NN = VY_N + DeltaT*FuerzaY(t,t0,M,X_N,CX,Y_N,CY,VY_N)/M
            Dy = VY_N*DeltaT
            Y_N = Y_N + Dy
            VY_N = VY_NN
            
            ##Movimiento en X
            VX_NN = VX_N + DeltaT*FuerzaX(t,t0,M,X_N,CX,Y_N,CY,VX_N)/M
            Dx = VX_N*DeltaT
            X_N = X_N + Dx
            VX_N = VX_NN

            c.move(Dx,Dy)
            n = n + 1

    win.close()

main()
