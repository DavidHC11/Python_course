# Databricks notebook source
import math
def cuadratica(a,b,c):
    x1 = (-b + math.sqrt(b**2 + 4*a*c))/2*a 
    x2 = (-b - math.sqrt(b**2 + 4*a*c))/2*a 
    
    return x1,x2

# COMMAND ----------

xx,yy = cuadratica(1,2,15)

# COMMAND ----------

print("x1 = ",xx, "x2 = ",yy)

# COMMAND ----------


