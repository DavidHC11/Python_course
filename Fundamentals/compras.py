# Databricks notebook source

montos = []
boton = True

while boton:
    monto = float(input("Ingresa el monto o coloca 0 para finalizar"))
    if monto == 0:
        boton = False
    else:
        montos.append(monto)