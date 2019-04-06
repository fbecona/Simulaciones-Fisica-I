from graphics import *
from math import *
import time

def PosicionX(t,t0):
        X0 = 350                        
        r = 3
        vang = 3.14159265359	#no nos deja usar la función math.pi
        return X0+r*cos(vang*(t-t0))

def PosicionY(t,t0):
        Y0 = 250
        r = 3
        vang= 3.14159265359     #no nos deja usar la función math.pi
        return Y0+r*sin(vang*(t-t0))

def VelocidadX(t,t0):
        r = 3
        vang=3.14159265359
        return -r*vang*sin(vang*(t-t0))

def VelocidadY(t,t0):
        r = 3
        vang=3.14159265359
        return r*vang*cos(vang*(t-t0)) 

def PosicionX1(t,t0):
        T = 4
        k = 0.3
        X0 = PosicionX(t0+k*T,t0)
        Vx0 = VelocidadX(t0+k*T,t0) 
        return X0 + Vx0 * (t - (t0+k*T))

def PosicionY1(t,t0):
        T = 4
        k = 0.3
        Y0 = PosicionY(t0+k*T,t0)
        Vy0 = VelocidadY(t0+k*T,t0)
        a = 9.8
        return Y0 + Vy0 *((t - (t0+k*T)))+ (a*((t - (t0+k*T))**2)/2)

def main():
        win = GraphWin("MRU", 500, 500)
        k = 0.3
        T = 4
        MPP=1												         
        c = Circle(Point(PosicionX(0,0),PosicionY(0,0)),10)
        c.draw(win)

        win.getKey() 											         

        t0 = time.time()
        t = time.time()

        DeltaT = 1/100
        n = 1
        while(t < t0 + T):
                t = time.time()
                if t<t0+k*T:
                        if t<=t0+n*DeltaT:
                                c.move(PosicionX(t,t0)-PosicionX(t-DeltaT,t0),PosicionY(t,t0)-PosicionY(t-DeltaT,t0))
                                n=n+1
                elif t>=t0+k*T:
                        if t<=t0+n*DeltaT:
                               c.move(PosicionX1(t,t0)-PosicionX1(t-DeltaT,t0),PosicionY1(t,t0)-PosicionY1(t-DeltaT,t0))
                               n=n+1
        win.close()
main()
