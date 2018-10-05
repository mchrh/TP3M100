# 4.1 a)
import numpy as np

def fct1(x):
    return np.exp(x**2)

#4.1 b)
def rectangle(f, a, b, N):
    z = 0
    delta = float(b-a) / N
    x = a
    for i in range(0, N + 1):
        z += f(x) * delta
        x += delta
    return z

rectangle(fct1,0,1,10)

#4.1 c)
def rectangle2(f,a,b,N,alpha):
    if (alpha > 1) or (alpha < 0):
        return "Veuillez entrez une valeur appartenant à [0,1]"
    else :
        z = 0
        delta = float(b-a) / N
        x = a
        for i in range(0, N + 1):
            z += f(x) * delta
            x += delta
        return z
def f(x):
    return rectangle2(fct1,0,1,10,0.5)

#4.1 d)

import matplotlib
import matplotlib.patches as patches

def plot_rectangle(f,a,b,N,alpha):
    delta = (b-a)/N
    x=np.linspace(a,b,50)
    fig=plt.plot(x,f(x))
    axes = fig[0].axes
    t=a
    while t<b:
        axes.add_patch(patches.Rectangle(
            (t,0),
            1/N,
            f(t+alpha*delta))


plt.show()

#4.1 e)
%timeit rectangle(fct1, 2, 8, 5)

#4.2 a)
def trapezes(f,a,b,N):
    delta = (b-a)/float(N)
    z = 0.5*(f(a) + f(b))
    for i in range(1,N):
        z=+f(a+i*delta)
    return delta*z

#4.2 c)
%timeit trapezes(fct1, 2, 8, 5)
