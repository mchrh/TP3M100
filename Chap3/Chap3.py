# 3.1 Question a)
import numpy as np

vec1= np.arange(5,10)

vec2 = np.arange(3,10,2)

print vec1
print vec2

# 3.1 Question b)
np.linspace(2,5, num=10)

a = np.array([[1,2,3,4,5,6]]) # vecteur original à transformer

b = np.reshape(a, (3,2)) # transformation du vecteur a en matrice 2x3

c = np.reshape(b, (2,3)) # transformation de b en matrice 3x2

np.transpose(c) # transposée de la matrice c

# 3.2 Question a)

# Dérivée d'une liste

v=[1,4,10,17,26,35,38,49,100]

def diff_list(v):
    n = len(v)
    d = [v[i+1] - v[i] for i in range(n-1)]
    return d

diff_list(v)

# Dérivée d'un vecteur Numpy

def diff_np (l):
    t=np.array(l,dtype=float)
    n=len(t)
    c=np.zeros(n-1,dtype=float)
    for i in range (len(t)-2):
        a=t[i:i+2]
        b=t[i+1:i+3]
        c[i:i+2]=b-a
    return c

# 3.2 Question b)
a_list = [np.random.random() for _ in range(1000)]
a_np = np.random.random(1000)

%%timeit diff_list(a_list)

# 3.3 Question a)
import numpy as np
import matplotlib.pyplot as plt
import math as m


x=np.linspace(0,2*m.pi,100)
y1=np.cos(x)
y2=np.cos(2*x)
y3=np.cos(3*x)
y4=np.sin(x)
y5=np.sin(2*x)
y6=np.sin(3*x)
plt.plot(x,y1,label="cos(x)")
plt.plot(x,y2,label="cos(2x)")
plt.plot(x,y3,label="cos(3x)")
plt.plot(x,y4,label="sin(x)")
plt.plot(x,y5,label="sin(2x)")
plt.plot(x,y6,label="sin(3x)")
plt.xticks(np.arange(0, 2.5*m.pi, step=m.pi/2),('0','π/2','π','2π/3','2π'))
plt.yticks(np.arange(-1,1.25,step=0.25))
plt.title('Fonctions trigonométriques')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# 3.3 Question b)
import numpy as np
import matplotlib.pyplot as plt
import math as m


plt.imshow(np.random.random((10, 10)), interpolation='none')
plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)
plt.show()

# 3.3 Question c)
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 300)
y = np.linspace(-3, 3, 301)
X, Y = np.meshgrid(x, y)

Z = (-Y/5) + np.exp(-X**2 - Y**2)

plt.pcolor(X, Y, Z)

plt.show()

# 3.4 a)
c=np.array([0.9602, -0.99, 0.2837, 0.9602, 0.7539, -0.1455, -0.99, -0.9111, 0.9602, -0.1455, -0.99, 0.5403, -0.99, 0.9602, 0.2837, -0.99, 0.2837, 0.9602])
cond= (c<=0)
c[cond]=0
