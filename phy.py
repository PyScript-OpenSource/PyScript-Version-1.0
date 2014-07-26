import turtle,time,tkinter

class phy():
        def getForce(m,a):
                F = m*a
                return F
        def getCurrent(v,r):
                C = v/r
                return C
        def getFallTime(d,a):
                timeS = int((2 * d)/a)
                return timeS
        def bullet(v,m):
                a = v*m
                return a
        def getVelocity(s,d):
                V = s*d
                return V
        def getAcceleration(v,u,t):
                a = v-u/t
                return a
        def getDensity(m,V):
                D = m/V
                return D
        def getPressure(F,A):
                P=F/A
                return P
        def getImpulse(F,t):
                I = F*t
                return I
        
        
        
