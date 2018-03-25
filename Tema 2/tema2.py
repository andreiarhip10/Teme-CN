import numpy as np
from numpy.linalg import inv

ainit=np.array([[0,0,4,],[0,2,6],[2,4,3]])
binit=np.array([2,3,1])
a=ainit
b=binit
n=len(a)

#rezolvare directa
x = np.zeros((n,), dtype=float)
x = np.linalg.solve(a, b)
print(x)

#verificare solutie
def verifica_solutie(x):
    print(x)

# metoda substitutiei
def rez_sistem(a,b,n):
    x = np.zeros((n,), dtype=float)
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
    eps=0
    while(l<n-1 and a[l][l]>eps):

        ##gauss 5,6,7
        for i in range(l+1,n):
            if  a[l][l]>0:
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
        rez_sistem(a,b,n)
        verifica_solutie(x)

algoritm(a,b,n)


