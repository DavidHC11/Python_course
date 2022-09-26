# Databricks notebook source
def calculadora():
    boton = True
    a = float(input("Ingresa el primer valor: "))
    while boton:
        b = float(input("Ingresa el segundo valor: "))
        operacion = input("Ingresa la operacion a realizar + (para suma) | - (para resta) | / (para división) | * (para multiplicación) | r (para raiz) | ** (para potencia): ")
        if operacion != "r":
            return eval(str(a) + operacion + str(b)) 
        else:
            b = float(input("Ingresa el valor de la raiz: "))
            return a ** (1/b)

# COMMAND ----------

calculadora()
