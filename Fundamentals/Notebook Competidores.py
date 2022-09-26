# Databricks notebook source
import pandas as pd

# COMMAND ----------

path = '/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 12 - Actividad Competidores Olimpicos/athlete_events.csv'
df = pd.read_csv(path)

# COMMAND ----------

# MAGIC %md # Competidores Olímpicos  
# MAGIC   
# MAGIC <br>
# MAGIC 
# MAGIC * Crear un programa en Visual Studio que me permita saber cuál es el competidor más veterano que ha recibido medalla para los NOC´s MEX, COL y ARG (oro, plata o bronce) 
# MAGIC * Crear un programa en Visual Studio que me permita saber cuál es el competidor más joven que ha recibido medalla de oro para los NOC´s USA y CAN
# MAGIC * Encuentra al competidor más ganador de la historia en medallas totales, medallas de oro, medallas de plata y medallas de broce para los NOC´s USA, CHN y RUS. Crea un csv con toda su información.

# COMMAND ----------

# MAGIC %md ##  MEX, COL y ARG

# COMMAND ----------

veteranos = df[df["NOC"].map(lambda x: x in ["MEX","COL","ARG"])].groupby(["NOC","Medal"]).agg({"Age":"max"}).reset_index()
df.merge(veteranos, how = "inner", on = ["NOC","Medal","Age"])

# COMMAND ----------

veteranos = df[(~(df.Medal.isnull()))]
veteranos = veteranos[veteranos["NOC"].map(lambda x: x in ["MEX","COL","ARG"])].groupby(["NOC"]).agg({"Age":"max"}).reset_index()
resultado = df.merge(veteranos, how = "inner", on = ["NOC","Age"])
resultado[~(resultado["Medal"].isnull())]

# COMMAND ----------

# MAGIC %md ## USA & CAN

# COMMAND ----------

veteranos = df[df["NOC"].map(lambda x: x in ["USA","CAN"])].groupby(["NOC","Medal"]).agg({"Age":"min"}).reset_index()
resultado = df.merge(veteranos, how = "inner", on = ["NOC","Medal","Age"])
resultado[resultado["Medal"]=="Gold"]

# COMMAND ----------

# MAGIC %md ## USA, CHN y RUS

# COMMAND ----------


veteranos = df[df["NOC"].map(lambda x: x in ["USA", "CHN", "RUS"])]
veteranos = veteranos[~(veteranos.Medal.isnull())].groupby(["ID"]).agg({"Age":"count"}).reset_index()
ganador = veteranos[veteranos.Age ==  veteranos.Age.max()]

ganador_hist = df[df.ID == 94406]
ganador_hist[~(ganador_hist.Medal.isnull())].to_csv("Ganadores.csv",index=False)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

prueba = df[df["Year"]==df["Year"].max()]
prueba[~(prueba.Medal.isnull())]["Team"].value_counts(1).head(20).plot(kind = 'pie')

# COMMAND ----------

display(prueba[~(prueba.Medal.isnull())]["Team"].value_counts(1).head(20).to_frame().reset_index())

# COMMAND ----------


