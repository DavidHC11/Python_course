# Databricks notebook source
import pandas as pd

# COMMAND ----------

df = pd.read_csv("/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 14 - Salarios/2022_qna16_remuneraciones.csv")

# COMMAND ----------

df.isnull().sum().to_frame("Nulos")

# COMMAND ----------

resumen = df[['SUELDO_TABULAR_BRUTO', 'SUELDO_TABULAR_NETO']].describe(percentiles=[0.05,.1,.25,.5,.75,.9,.95])
print("SUELDO_TABULAR_BRUTO",(resumen.loc["max"][0] - resumen.loc["min"][0]))
print("SUELDO_TABULAR_NETO",(resumen.loc["max"][1] - resumen.loc["min"][1]))

# COMMAND ----------


