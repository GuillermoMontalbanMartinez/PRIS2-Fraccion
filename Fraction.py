# clase fraccion que representa una fraccion
class Fraction:
    #constructor
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    # suma de fracciones
    def suma(self, fraccion):
        numerador = self.numerador * fraccion.denominador + self.denominador * fraccion.numerador
        denominador = self.denominador * fraccion.denominador
        return Fraction(numerador, denominador)
    # resta de fracciones
    def resta(self, fraccion):
        numerador = self.numerador * fraccion.denominador - self.denominador * fraccion.numerador
        denominador = self.denominador * fraccion.denominador
        return Fraction(numerador, denominador)
    # multiplicacion de fracciones
    def multiplicacion(self, fraccion):
        numerador = self.numerador * fraccion.numerador
        denominador = self.denominador * fraccion.denominador
        return Fraction(numerador, denominador)
    # division de fracciones
    def division(self, fraccion):
        numerador = self.numerador * fraccion.denominador
        denominador = self.denominador * fraccion.numerador
        return Fraction(numerador, denominador)
    # representacion de la fraccion
    def __str__(self):
        return str(self.numerador) + "/" + str(self.denominador)
    # simplificar fraccion
    def simplificar(self):
        divisor = self.gcd(self.numerador, self.denominador)
        self.numerador = self.numerador // divisor
        self.denominador = self.denominador // divisor
    # maximo comun divisor
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
