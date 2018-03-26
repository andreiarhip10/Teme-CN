import numpy as np
from numpy.linalg import inv
from random import randint
import math

def random_system_matrix():
    n = randint(2, 5)
    a = [];
    b = [];
    line = [];
    for i in range(0, n):
        b.append(randint(0, 100))
        for j in range(0, n):
            line.append(randint(0, 100))
        a.append(line)
        line = []
    return a, b
#print (random_system_matrix()[1])
# ainit=np.array([[0,0,4,],[0,2,6],[2,4,3]])
# binit=np.array([2,3,1])
(ainit, binit) = random_system_matrix()
a=ainit
b=binit
n=len(a)
xgauss = np.zeros((n,), dtype=float)

m=2
#m = int(input("Precizia, m"))
eps=pow(10,-m)

print("Matricea A: ")
for i in range(0,n):
    print(ainit[i])
print("Matricea B: ", binit)

#rezolvare directa
xlib = np.zeros((n,), dtype=float)
if np.linalg.det(ainit)!=0:
     print("Rezultat librarie: ")
     xlib=(np.dot(inv(ainit),binit))
     print(xlib)
else:
     print("Nu are solutie")


#verificare solutie
def verifica_solutie(x):
    print(x)
    print("Rezultat verificare: ")
    print(np.dot(ainit,x)-binit)

# metoda substitutiei
def rez_sistem(a,b,n,x):

    x[n - 1] = b[n - 1] / a[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = b[i]
        for j in range(i, n - 1):
            x[i] -= a[i][j + 1] * x[j + 1]
        x[i] /= a[i][i]
    return x

def algoritm(a,b,n):
    l=0
    #cauta pivot
    max= abs(a[l][l])
    i0=l
    for i in range (l+1,n):
        if abs(a[i][l])>max:
            max=abs(a[i][l])
            i0=i

    #interschimba
    for i in range(l,n):
        aux=a[i0][i]
        a[i0][i]=a[l][i]
        a[l][i]=aux
    aux = b[i0]
    b[i0] = b[l]
    b[l] = aux

    l=0

    #dat de la tastatura
    #eps=0
    while(l<n-1 and a[l][l]>eps):

        ##gauss 5,6,7
        for i in range(l+1,n):
            #verificare impartire 
            if abs(a[l][l]) > eps:
                f=-a[i][l]/a[l][l]
                b[i]=b[i]-f*b[l]
                for j in range(l,n):
                    a[i][j]+=f*a[l][j]
        l+=1

        #cauta pivot
        max = abs(a[l][l])
        i0 = l
        for i in range(l + 1, n):
            if abs(a[i][l]) > max:
                max = abs(a[i][l])
                i0 = i

        #interschimba
        for i in range(0, n):
            aux = a[i0][i]
            a[i0][i] = a[l][i]
            a[l][i] = aux
        aux = b[i0]
        b[i0] = b[l]
        b[l] = aux

    if a[l][l]<=eps:
        print("Matrice singulara")
    else:
        # print("Matricea A transformata: ")
        # for i in range(0,n):
        #     print(a[i])
        rez_sistem(a,b,n,xgauss)
        verifica_solutie(xgauss)

print("Rezultat Gauss: ")
algoritm(a,b,n)

no1=[]
no2=[]
print("Norme: ")
inva=inv(ainit)
for i in range(0,n):
    no1.append(math.sqrt(pow(xgauss[i],2)+pow(xlib[i],2)-2*xgauss[i]*xlib[i]))
print(no1)
print(no2)