import numpy as np
import math

def sumacplx(a, b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)

def productcplx(a, b):
    real = (a[0] * b[0]) - (a[1] * b[1])
    img = (a[0] * b[1]) + (a[1] * b[0])
    return (real, img)

def productomatrices(A, B): #Funcion para realizar el producto entre matrices
    f = len(A)
    c = len(A[0])
    m = []
    for i in range(f):
        fila = []
        for j in range(f):
            suma = (0,0)
            for k in range(c):
                suma = sumacplx(suma, productcplx(A[i][k], B[k][j]))
            fila += [suma]
        m = m + [fila]
    return m

def modulocplx(a):
    return math.sqrt((a[0])**2 + (a[1])**2)

def conjugadocplx(a):
    return (a[0], -1*a[1])

def producto_interno(A, B):
    for i in range(len(A)):
        A[i][0] = conjugadocplx(A[i][0])
    filas = len(A)
    matriz = [0 for i in range(filas)]
    for i in range(filas):
        matriz[i] = A[i][0]
    suma = (0,0)
    for i in range(len(matriz)):
        suma = sumacplx(suma, productcplx(matriz[i], B[i][0]))
    return suma

def norma_vector(v):
    x = [a[:] for a in v]
    resp = producto_interno(v,x)
    return math.sqrt(resp[0])

def divComplex(c1, c2):
    return c1/c2

def inversamatriz(A):
    matriz = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila = fila + [(-1*A[i][j][0],-1*A[i][j][1])]
        matriz = matriz + [fila]
    return matriz

def adicionmatrices(A, B):
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila = fila + [sumacplx(A[i][j], B[i][j])]
        matriz = matriz + [fila]
    return matriz

def multescalarmatriz(c, A):
    matriz = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila = fila + [(c*A[i][j][0],c*A[i][j][1])]
        matriz = matriz + [fila]
    return matriz

def matrizhermitiana(A):
    filas = len(A)
    columnas = len(A[0])
    if filas != columnas:
        return False
    B = [[0 for i in range(filas)]for i in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            B[j][i] = A[i][j]
    for i in range(filas):
        for j in range(columnas):
            B[i][j] = conjugadocplx(B[i][j])
    for i in range(filas):
        for j in range(columnas):
            if B[i][j] != A[i][j]:
                return False
    return True

def probabilidadenpunto(posicion, vector):
    return (100 * ((modulocplx(vector[posicion][0]))**2)/((norma_vector(vector))**2))

def probabilidadVectorAOtro(vector1, vector2):
    multnorma = norma_vector(vector1) * norma_vector(vector2)
    prod = producto_interno(vector2, vector1)
    return (100*(divComplex(complex(prod[0], prod[1]), multnorma)) )

def accionmatrizvectorComplex(A,v):
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        suma = (0,0)
        for j in range(columnas):
            suma = sumacplx(suma, productcplx(A[i][j], v[j][0]))
        matriz = matriz + [(suma)]
    return matriz

def valoresperado(matriz, vector):
    return producto_interno(accionmatrizvectorComplex(matriz, vector), vector)

def crearunitaria(n):
    unitaria = []
    for i in range(n):
        fila = []
        for j in range(n):
            if j == i:
                fila += [(1,1)]
            else:
                fila += [(0, 0)]
        unitaria.append(fila)

def mediaobservable(observable, vectorket):
    return adicionmatrices(observable, inversamatriz(multescalarmatriz(valoresperado(observable, vectorket), crearunitaria(len(observable[0])))))

def traspuestacomplex(A):
    filas = len(A)
    columnas = len(A[0])
    matriz = [[0 for i in range(filas)]for i in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            matriz[j][i] = A[i][j]
    return matriz

def conjugadamatriz(A):
    matriz = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila = fila + [conjugadocplx(A[i][j])]
        matriz = matriz + [fila]
    return matriz

def adjuntamatriz(A):
    return traspuestacomplex(conjugadamatriz(A))

def traceComplex(matriz):
    suma = (0,0)
    for i in range(len(matriz)):
        suma += sumacplx(suma, matriz[i][i])
    return suma

def productointernomatriz(A, B):
    tamano = len(A)
    suma = (0,0)
    A = adjuntamatriz(A)
    for i in range(tamano):
        for j in range(tamano):
            suma += sumacplx(suma, productcplx(A[i][j], B[i][j]))
    return suma

def varianza(observable, vectorket):
    media = mediaobservable(observable, vectorket)
    return valoresperado(productomatrices(media, media),vectorket)

def main():
    print("Ejercicio 1")
    posiciones = int(input("Ingrese el numero de posiciones: "))
    vectorinicial = []
    for i in range(posiciones):
        valores = input("Digite la amplitud, separada por coma (real, img): ")
        amplitud = tuple(int(x) for x in valores.split(","))
        vectorinicial += [[amplitud]]
    posicion = int(input("Digite la posicion la cual desea saber la probabilidad: "))
    vector1 = [x[:] for x in vectorinicial]
    print("La probabilidad es:",probabilidadenpunto(posicion, vector1))

    print("Ejercicio 2")
    vector2 = []
    for i in range(posiciones):
        valores = input("Digite la amplitud, separada por coma (real, img): ")
        amplitud = tuple(int(x) for x in valores.split(","))
        vector2 += [[amplitud]]
    print("La probabilidad es:",probabilidadVectorAOtro(vector2, vectorinicial))

    print("Ejercicio 3")
    tamano = int(input("Digite el tamaño de la matriz cuadrada: "))
    observable = []
    for i in range(tamano):
        fila = []
        for j in range(tamano):
            valores = input("Digite la amplitud en la posicion " + str(i) + "," + str(j) + " separada por comas (real, img): ")
            amplitud = tuple(int(x) for x in valores.split(","))
            fila += [amplitud]
        observable += [fila]
    vectorket = []

    for i in range(tamano):
        valores = input("Digite la amplitud del vector ket, separada por comas (real, img): ")
        amplitud = tuple(int(x) for x in valores.split(","))
        vectorket += [[amplitud]]
    if matrizhermitiana(observable):
        print(mediaobservable(observable, vectorket))
        print(varianza(observable, vectorket))
    else:
        print("La matriz no es hermitiana")
main()
