import math
import numpy as np

b=[]
n=0
def read_matrix(file):

    with open(file, "r") as ins:
        count = 0

        for line in ins:
            line = line.strip('\n')
            if line == "":
                count += 1

            if count == 0:
                n = int(line)
                vector = [[0 for x in range(1)] for y in range(int(n))]
            elif count == 1 and line != "":
                b.append(float(line))
            elif count == 2 and line != "":

                element = line.split(', ')
                valoare = float(element[0])
                i = int(element[1])
                j = int(element[2])

                if(vector[i]==[0]):
                    vector[i].remove(0)

                    vector[i].append((valoare,j))
                else:
                    vector[i].append((valoare,j))

        #sortare + elementul de pe diagonala pe ultima pozitie
        for i in range(0,n):
            for j in range(0,len(vector[i])):

                if(vector[i][j][1]==i):
                    aux=vector[i][j]
                    vector[i].remove(vector[i][j])
                    break

            vector[i].sort(key=lambda tup: (tup[1], tup[0]))
            vector[i].append(aux)

        #daca apar aceiasi indecsi
        for i in range(0, n):
            for j in range(1,len(vector[i])):
                if vector[i][j][1] == vector[i][j-1][1]:
                    vector[i][j][0] += vector[i][j-1][1]
                    vector[i].remove(vector[i][j-1])

        ok=1
        for i in range(0, n):
            if len(vector[i])>10:
                ok=0
                break
        if ok==1:
            print("Exista maxim 10 elemente nenule pe linie")
        else:
            print("Nu")
        return (vector,n)


def multiply_vector(matrix_a, x):
    for vect in matrix_a:
        vect.sort(key=lambda tup: (tup[1], tup[0]))
    vector=list()
    for i in range(0,n):
        vect = list()
        sum = 0
        for j in range(0, len(matrix_a[i])):
            a = matrix_a[i][j]
            sum+=a[0]*x[a[1]]
        vect.append((sum,i))
        vect.sort(key=lambda tup: (tup[1], tup[0]))
        for i in vect:
            vector.append(i[0])
    return vector


def solve(matrix):
    xc = [0] * n
    k = 0
    while True:
        xp = xc[:]

        for i in range(0,n):
            sum1 = 0
            sum2 = 0

            for j in range(0,len(matrix[i])-1):
                el=matrix[i][j]
                if el[1] < i:
                    sum1 += el[0] * xp[el[1]]

                else:
                    sum2 += el[0] * xc[el[1]]

            diag=matrix[i][len(matrix[i])-1][0]
            xc[i] = (b[i] - sum1 - sum2) / diag

        delta_x = get_norm(xp, xc, n)
        k += 1
        if not (delta_x >= epsilon and k <= kmax and delta_x <= const):
            break

    if delta_x < epsilon:
        print("Solutia: ",xc)
        print("Nr iteratii: ",k)
        verify(matrix, xc)
    else:
        print("Divergenta")


def get_norm(xc, xp, n):
    sum = 0
    for i in range(n):
        sum += pow((xc[i] - xp[i]), 2)
    sum = math.sqrt(sum)

    return sum


def verify(matrix,xgs):
    x = multiply_vector(matrix, xgs)
    delta_x = get_norm(x, b, n)
    print("Verificare: ", delta_x)


kmax = 10000
p = 7
epsilon = pow(10, -p)
const = pow(10, 8)

ok=1
read=read_matrix("m_rar_2018_2.txt")
matrix=read[0]
n=int(read[1])

#verific daca se poate rezolva sistemul
for i in range(0, n):
    diag = matrix[i][len(matrix[i]) - 1][0]
    if diag==0 :
        ok=0
        break
if(ok==1):
    solve(matrix)
else:
    print("Nu se poate rezolva")