def triangulo(a, b, c):
    if  ( a < (b+c) and b < (a+c) and c < (a+b) ):
        return("Entradas formam um triangulo")
    else:
        return("Entradas nao formam um triangulo")

