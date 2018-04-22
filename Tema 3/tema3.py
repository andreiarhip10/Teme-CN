import time
import numpy as np
v = list()
def read_matrix(file):

    vector = [[0 for x in range(1)] for y in range(2018)]

    with open(file, "r") as ins:
        count = 0

        for line in ins:
            line = line.strip('\n')
            if line == "":
                count += 1

            if count == 0:
                n = line
            elif count == 1 and line != "":
                v.append(float(line))
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
        for i in range(0,2018):
            for j in range(0,len(vector[i])):

                if(vector[i][j][1]==i):
                    aux=vector[i][j]
                    vector[i].remove(vector[i][j])
                    break

            vector[i].sort(key=lambda tup: (tup[1], tup[0]))
            vector[i].append(aux)

        #daca apar aceiasi indecsi
        for i in range(0, 2018):
            for j in range(1,len(vector[i])):
                if vector[i][j][1] == vector[i][j-1][1]:
                    vector[i][j][0] += vector[i][j-1][1]
                    vector[i].remove(vector[i][j-1])
        return (vector)



def add(matrix_a, matrix_b):
    vector=list()
    for i in range(0,2018):
        vect=list()
        n=len(matrix_a[i])
        m=len(matrix_b[i])

        for j in range(0, len(matrix_a[i])-1):
            a = matrix_a[i][j]
            for k in range(0, len(matrix_b[i])-1):
                b = matrix_b[i][k]
                if a[1] == b[1]:
                    aduna = a[0] + b[0]
                    vect.append((aduna, a[1]))
                    matrix_a[i].remove(a)
                    matrix_b[i].remove(b)
        for j in range(0, len(matrix_a[i])-1):
            a = matrix_a[i][j]
            vect.append((a[0], a[1]))
        for j in range(0, len(matrix_b[i])-1):
            b = matrix_b[i][j]
            vect.append((b[0], b[1]))

        a = matrix_a[i][len(matrix_a[i])-1]
        b = matrix_b[i][len(matrix_b[i])-1]
        vect.sort(key=lambda tup: (tup[1], tup[0]))
        vect.append((a[0] + b[0], i))
        vector.append(vect)
    return vector


def multiply_vector(matrix_a, x):
    for vect in matrix_a:
        vect.sort(key=lambda tup: (tup[1], tup[0]))
    vector=list()
    for i in range(0,2018):
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

#######adunare matrix
print("Adunare matrix")
matrix_a = read_matrix("a.txt")
matrix_b = read_matrix("b.txt")

matrix_a_plus_b = read_matrix("aplusb.txt")
matr=add(matrix_a,matrix_b)

#pt verificare precizie
print(matrix_a_plus_b[2])
print(matr[2])

e=pow(10,-5)
# e=0
for i in range(0,2018):
    result = (abs(np.subtract(matr[i],matrix_a_plus_b[i])) <= e).all()
    if(result!=True):
        break
print(result)


#######inmultire cu vectorul x
print("Inmultire cu x")
v=list()
matrix_a = read_matrix("a.txt")
x = list(range(2018,0,-1))

matr=multiply_vector(matrix_a,x)
print(matr)
print(v)

result = (abs(np.subtract(matr,v)) <= e).all()
print(result)
