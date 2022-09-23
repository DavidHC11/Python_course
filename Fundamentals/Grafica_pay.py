# Databricks notebook source
import pandas as pd

# COMMAND ----------

path = '/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 12 - Actividad Competidores Olimpicos/athlete_events.csv'
df = pd.read_csv(path)

# COMMAND ----------

prueba = df[df["Year"]==df["Year"].max()]
prueba[~(prueba.Medal.isnull())]["Team"].value_counts(1).head(20).plot(kind = 'pie')

# COMMAND ----------

display(prueba[~(prueba.Medal.isnull())]["Team"].value_counts(1).head(20).to_frame().reset_index())

# COMMAND ----------


