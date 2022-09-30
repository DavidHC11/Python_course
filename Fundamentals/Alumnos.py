# Databricks notebook source
import pandas as pd
import seaborn as sns

# COMMAND ----------

df = pd.read_csv('/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 17 - Alumnos por grado/clean_students_complete.csv')

# COMMAND ----------

df.isnull().sum().to_frame("Nulos")

# COMMAND ----------

df[(df["reading_score"]<1) | (df["math_score"]<1)]

# COMMAND ----------

resumen = df.groupby(["grade","gender"]).agg({"Student ID":"count","reading_score":"mean","math_score":"mean"}).reset_index()
sns.barplot(data=df, x="grade", y="Student ID", hue="gender")

# COMMAND ----------

resumen

# COMMAND ----------


