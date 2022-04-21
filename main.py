# probar clase fraccion.py
from Fraction import Fraction


numerador = int(input("Ingrese el numerador: "))
denominador = int(input("Ingrese el denominador: "))
f1 = Fraction(numerador, denominador)
print("Fraccion 1: ", f1)
f1.simplificar()
print("Fraccion 1 simplificada: ", f1)
numerador = int(input("Ingrese el numerador: "))
denominador = int(input("Ingrese el denominador: "))
f2 = Fraction(numerador, denominador)
print("Fraccion 2: ", f2)
f2.simplificar()
print("Fraccion 2 simplificada: ", f2)
print("Suma: ", f1.suma(f2))
print("Resta: ", f1.resta(f2))
print("Multiplicacion: ", f1.multiplicacion(f2))
print("Division: ", f1.division(f2))

