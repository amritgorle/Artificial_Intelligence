import csv
import numpy
import pdb

def f(x,y):
    return (4.*(x**2.) - 3.*x*y + 2.*(y**2.) + 24*x - 20*y)
def f_vector(vect):
    x = vect[0]
    y = vect[1]
    return (4. * (x ** 2.) - 3. * x * y + 2. * (y ** 2.) + 24 * x - 20 * y)
def grad():
    def deri(x,y):
        der = numpy.array([8.*x - 3.*y + 24,-3.*x + 4.*y - 20])
        return der
    return deri
def error(x_vector,val=0):
    deri = grad()
    return sum(abs(deri(x_vector[0],x_vector[1])))
def OneDmin(function,E=0.01,a=0.,b=1.):
    if abs(a-b)<E:
        return (a+b)/2
    c = ((b-a)/3)+a
    d = 2*((b-a)/3)+a
    fc = function(c)
    fd = function(d)
    if(fc<fd):
        return OneDmin(function, E, a, d)
    else:
        return OneDmin(function, E, c, b)

def minimize_f():
    count = 0
    x_vector = numpy.array([1.,1.])
    while(True):
        if error(x_vector)<0.00001:
            return count
        deltaf = grad()
        #lam = OneDmin(lambda L:f((x_vector-L*deltaf(x_vector[0],x_vector[1]))[0],(x_vector-L*deltaf(x_vector[0],x_vector[1]))[1]))
        lam = OneDmin(lambda L:f_vector(x_vector-L*deltaf(x_vector[0],x_vector[1])))
        #lam = 0.161
        delta = -lam * deltaf(x_vector[0],x_vector[1])
        x_vector = x_vector+delta
        count+=1
        print(x_vector)
        if count>100000:
            print(x_vector)
            count=0
            x_vector = numpy.array([1., 1.])
"""
def minimize_f(writer):
    for i in range(1,200):
        #pdb.set_trace()
        lam = i/1000
        print(lam)
        count = 0
        x_vector = numpy.array([1.,1.])
        while(True):
            if error(x_vector)<0.00001:
                writer.write(str(lam)+","+str(count)+"\n")
                break
            deltaf = grad()
            #lam = OneDmin(lambda L:f((x_vector-L*deltaf(x_vector[0],x_vector[1]))[0],(x_vector-L*deltaf(x_vector[0],x_vector[1]))[1]))
            #lam = OneDmin(lambda L:f_vector(x_vector-L*deltaf(x_vector[0],x_vector[1])))
            delta = -lam * deltaf(x_vector[0],x_vector[1])
            x_vector = x_vector+delta
            count+=1
            #print(x_vector)
            if count>100000:
                print(x_vector)
                count=0
                x_vector = numpy.array([1., 1.])
"""
print(minimize_f())
#function = grad()
#print(function(-1.56521739,3.82608696))