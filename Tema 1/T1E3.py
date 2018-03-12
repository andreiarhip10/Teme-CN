import numpy as np

A=np.array([[2,4,3,5],[3,2,6,1],[1,3,4,5],[4,5,6,7]])
B=np.array([[2,4,3,5],[3,2,6,1],[1,3,4,5],[4,5,6,7]])


C=np.dot(A,B)
#print(C)



def multiply_Strassen(a,b,n,nmin):
    c=0
    if n==nmin :
        return np.dot(a,b)


    else:
        n=len(a)//2
        a11 = a[:n, :n]
        a12 = a[:n, n:]
        a21 = a[n:, :n]
        a22 = a[n:, n:]
        # print(a11,a12,a21,a22)

        b11 = b[:n, :n]
        b12 = b[:n, n:]
        b21 = b[n:, :n]
        b22 = b[n:, n:]


        p1 = multiply_Strassen(np.add(a11,a22),np.add(b11,b22),n,nmin)
        p2 = multiply_Strassen(np.add(a21,a22),b11,n,nmin)
        p3 = multiply_Strassen(a11, np.subtract(b12,b22),n,nmin)
        p4 = multiply_Strassen(a22, np.subtract(b21,b11),n,nmin)
        p5 = multiply_Strassen(np.add(a11,a12),b22,n,nmin)
        p6 = multiply_Strassen(np.subtract(a21,a11),np.add(b11,b12),n,nmin)
        p7 = multiply_Strassen(np.subtract(a12,a22),np.add(b21,b22),n,nmin)


        c11 = np.subtract(np.add(np.add(p1,p4),p7),p5)
        c12 = np.add(p3,p5)
        c21 = np.add(p2,p4)
        c22 = np.subtract(np.add(np.add(p1,p3),p6),p2)

        c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
        return c




A=np.loadtxt('matrix_A.txt', delimiter=' ',comments="#")
B=np.loadtxt('matrix_B.txt', delimiter=' ',comments="#")
n=len(A)



print(np.dot(A,B),"\n")
nmin = int(input("Choose nmin"))
while nmin %2==1:
    nmin=int(input("Choose nmin"))
c=multiply_Strassen(A, B,n,nmin)
print(c)

