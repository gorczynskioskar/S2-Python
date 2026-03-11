#Oskar Górczyñski, 57785, 7/7
import matplotlib.pyplot as plt
import numpy as np

# Zadanie 1
f=lambda x: np.cos(x)
g=lambda x: np.sign(x)
x=np.linspace(-np.pi,np.pi,128)
plt.figure()
plt.plot(x,f(x),label='f(x)=cos(x)', color="black")
plt.plot(x,g(x),label='g(x)=sign(x)', color="red")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykresy funkcji f(x) i g(x)')
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi])
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi])
plt.legend(loc='upper left')
plt.savefig('lab12_zad1.png')
plt.show()

# Zadanie 2
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
F=lambda X,Y: np.sin(X)*np.cos(Y-1)
X=np.linspace(-5,5,100)
Y=np.linspace(-5,5,100)
X, Y = np.meshgrid(X, Y)
zad2=plt.figure()
ax=zad2.add_subplot(projection='3d')
ax.plot_surface(X,Y, F(X,Y), cmap=cm.coolwarm)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('F(X,Y)')
ax.set_title('Wykres powierzchni funkcji F(X,Y)')
plt.show()

# Zadanie 3

f=lambda x: np.sin(10*x)
g=lambda x: np.cos(5*x)
x=np.linspace(-np.pi,np.pi,128)
plt.figure()
plt.plot(x, f(x), color="blue")
plt.ylim([-1,3])
inset = plt.axes([0.32, 0.6, 0.4, 0.2])
inset.set_xlim([-np.pi,np.pi])
inset.set_xticks([-3,-2,-1,0,1,2,3])
inset.plot(x, g(x), color="blue")
plt.show()

# Zadanie 4
# Parametry

# Wykres
x= np.random.uniform(0, 3, size=1024)
y= np.random.uniform(0, 3, size=1024)
mask= (((x<1) & (y<1)) | ((x>2) & (y<1)) | ((x<1) & (y>2)) | ((x>2) & (y>2)) | (((x>1) & (y>1)) & ((x<2) & (y<2))))
plt.figure()
plt.scatter(x[mask], y[mask], color='blue', alpha=0.7)
plt.scatter(x[~mask], y[~mask], color='red', alpha=0.7)
plt.xlim([0,3])
plt.ylim([0,3])
plt.show()

# Zadanie 5
mozliwe_oceny=[2,2.5,3,3.5,4,4.5,5]
wylosowane= np.random.choice(mozliwe_oceny, size=30, replace=True)
bin_edges = [1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25]
plt.figure()
counts, bins, patches = plt.hist(
    wylosowane,
    bins=bin_edges,
    orientation='vertical',
    color="green",
    rwidth=0.7,
    histtype='bar',
    align='mid'
)

plt.xticks(mozliwe_oceny)
plt.xlabel('Oceny')
plt.ylabel('Liczba ocen')
plt.title('Histogram ocen studentow')
plt.show()

# Zadanie 6
X = list(range(12))
Y=np.random.normal(size=12)
plt.figure()
plt.bar(X, Y, color='red', edgecolor='black')
plt.xticks(X)
for i in range(12):
    if(Y[i]<=0): plt.text(i-0.35, 0.05, f"Y[{i}]={Y[i]:.2f}", fontsize=10)
    else: plt.text(i-0.35, Y[i]+0.05, f"Y[{i}]={Y[i]:.2f}", fontsize=10)
plt.show()

# Zadanie 7
x=np.linspace(-2,2,256)
y=np.linspace(-2,2,256)
X,Y = np.meshgrid(x,y)
Z = -y**3 + X**2 + Y**2 + 2*X -1
plt.figure()
plt.contourf(X, Y, Z, levels=20, cmap='YlOrRd_r')
C=plt.contour(X, Y, Z, levels=10, colors='black', linewidths=1)
plt.clabel(C, inline=True, fontsize=8, fmt='%1.3f')
plt.show()