# Databricks notebook source
dbutils.widgets.dropdown("edad", "18", [str(x) for x in range(1,100)])
dbutils.widgets.dropdown("genero", "Mujer", ["Hombre","Mujer"])

edad = int(dbutils.widgets.get("edad"))
genero = dbutils.widgets.get("genero")

# COMMAND ----------

if edad < 18:
    print(f"{genero} menor de edad")
else:
    print(f"{genero} mayor de edad")

# COMMAND ----------


