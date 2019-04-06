from graphics import *
from math import *
import time

def PosicionY(t,t0):
        A = 1
        m = 1
        b = 5
        g = -1
        e = 2.7182818284590452353602874713527
        y0= 30
        return -A*m/b*e**(-b/m*(t-t0))-m*g/b*(t-t0)+y0

def main():
        win = GraphWin("MRU", 500, 500)
        T = 4
        MPP=1												         
        c = Circle(Point(250,PosicionY(0,0)),10)
        c.draw(win)

        win.getKey() 											         

        t0 = time.time()
        t = time.time()

        DeltaT = 1/10
        n = 1
        while(t < t0 + T):
                t = time.time()
                if t<=t0+n*DeltaT:
                        c.move(0,PosicionY(t,t0)-PosicionY(t-DeltaT,t0))
                        n=n+1
        win.close()
main()

