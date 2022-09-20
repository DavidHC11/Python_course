# Databricks notebook source
montos = []
boton = True
suma = 0

while boton:
    monto = float(input("Ingresa el monto o coloca 0 para finalizar: "))
    while monto < 0:
        monto = float(input("No ingreses numeros negativos, intenta de nuevo o coloca 0 para finalizar: "))
    if monto == 0:
        boton = False
    else:
        montos.append(monto)
        print(f"Se añadió el monto {monto}")
print("\n")

if sum(montos)>1000:
    print("El total a pagar es : $",sum(montos))
    print("Descuento efectuado por : $", sum(montos)*.1)
    print("Total final: $", sum(montos)*.9)
else:
    print("El total a pagar es : $",sum(montos))

# COMMAND ----------

from math import ceil
tiempo = float(input("Ingresa el tiempo en el estacionamiento en minutos: "))
while tiempo < 0:
        tiempo = float(input("No ingreses numeros negativos, intenta de nuevo o coloca 0 para finalizar: "))

if tiempo < 60:
    cobro = 25
else:
    horas = ceil(tiempo / 60) - 1
    if horas > 8:
        cobro = 200 + 25 + 15 * horas
    else:
        cobro = 25 + 15 * horas

print("Tienes que pagar ", cobro)
