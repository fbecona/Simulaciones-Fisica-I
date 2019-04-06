from graphics import *
from math import *
import time

def PosicionX(t,t0):
        A = 5                      
        k = 5
        m = 1
        vang = (k/m)**(1/2)
        fi = 10
        return A*cos(vang*(t-t0)+fi)

def main():
        win = GraphWin("MRU", 500, 500)
        T = 4
        MPP=1												         
        c = Circle(Point(PosicionX(0,0),250),10)
        c.draw(win)

        win.getKey() 											         

        t0 = time.time()
        t = time.time()

        DeltaT = 1/100
        n = 1
        while(t < t0 + T):
                t = time.time()
                if t<=t0+n*DeltaT:
                        c.move(PosicionX(t,t0)-PosicionX(t-DeltaT,t0),0)
                        n=n+1
        win.close()
main()
