# Databricks notebook source
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# COMMAND ----------

df = pd.read_csv('/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 17 - Alumnos por grado/clean_students_complete.csv')

# COMMAND ----------

df.isnull().sum().to_frame("Nulos")

# COMMAND ----------

df[(df["reading_score"]<1) | (df["math_score"]<1)]

# COMMAND ----------

resumen = df.groupby(["grade","gender"]).agg({"Student ID":"count","reading_score":"mean","math_score":"mean"}).reset_index()
sns.barplot(data=resumen, x="grade", y="Student ID", hue="gender")

# COMMAND ----------

resumen

# COMMAND ----------

# MAGIC %md ## Feature Engineering

# COMMAND ----------

def transform(x):
    if x < 50:
        return "reprobado"
    elif x<70:
        return "regular"
    elif x>90:
        return "bueno"
    else:
        return "excelente"

# COMMAND ----------

df["transform_reading_score"] = df["reading_score"].apply(transform)
df["transform_math_score"] = df["math_score"].apply(transform)

# COMMAND ----------

df

# COMMAND ----------

calificaciones = df.groupby(["gender","transform_reading_score","transform_math_score"]).agg({"Student ID":"count"}).reset_index()

# COMMAND ----------

sns.barplot(data=calificaciones, x="transform_reading_score", y="Student ID", hue="gender")

# COMMAND ----------

sns.barplot(data=calificaciones, x="transform_math_score", y="Student ID", hue="gender")

# COMMAND ----------

calificaciones = df.groupby(["school_name","gender","transform_reading_score"]).agg({"Student ID":"count"}).reset_index()
calificaciones = calificaciones[calificaciones["transform_reading_score"]=="excelente"]

plt.figure(figsize = (33,8))
sns.barplot(data=calificaciones, x="school_name", y="Student ID", hue="gender")

# COMMAND ----------

calificaciones_bajas = df.groupby(["school_name","gender","transform_reading_score"]).agg({"Student ID":"count"}).reset_index()
calificaciones_bajas = calificaciones_bajas[(calificaciones_bajas["transform_reading_score"]=="regular") | (calificaciones_bajas["transform_reading_score"]=="reprobado")]

# COMMAND ----------

plt.figure(figsize = (33,8))
sns.barplot(data=calificaciones_bajas, x="school_name", y="Student ID", hue="gender")

# COMMAND ----------


