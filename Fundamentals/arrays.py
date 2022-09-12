# Databricks notebook source
import numpy as np
import random

# COMMAND ----------

ejemplo1 = np.array([x for x in range(3,25)])
ejemplo2 = np.array([random.randint(3, 24) for x in range(3,25)])

# COMMAND ----------

ejemplo3 = np.array([x for x in range(5)]*2)

# COMMAND ----------

np.sort(ejemplo3)

# COMMAND ----------

np.array([[0,1,2],[3,4,5],[6,7,8]])

# COMMAND ----------

m=np.identity(6)

# COMMAND ----------


