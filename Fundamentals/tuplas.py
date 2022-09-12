# Databricks notebook source
ejemplo = (1,2.3,"hola",True, [])

# COMMAND ----------

eje_lista = list(ejemplo) 

# COMMAND ----------

ejemplo = {x:y for x,y in zip(range(1,6), ejemplo)}

# COMMAND ----------


