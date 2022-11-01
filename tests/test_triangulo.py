import pytest

import src.triangulo.triangulo as triangulo

class Test:

    def teste1(self):
        assert triangulo.triangulo(10,7,8) == "Entradas formam um triangulo"

    def teste2(self):
        assert triangulo.triangulo(5,5,11) == "Entradas nao formam um triangulo"

    def teste3(self):
        assert triangulo.triangulo(0,5,4) == "Entradas nao formam um triangulo"

    def teste4(self):
        assert triangulo.triangulo(5,5,10) == "Entradas nao formam um triangulo"