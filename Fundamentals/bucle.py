# Databricks notebook source
consumo = {"Adolf":11,"Luis":23,"David":10,"Oli":45,"Gabo":22,"Adrian":6,"Gaby":7}

for x,y in consumo.items():
    print(f"{x} dijo el numero {y}", sep="\n")
    
print("\n", f"El numero mas grande fue {max(consumo.values())}, el mas pequeño fue {min(consumo.values())}")

# COMMAND ----------

import random 

consumo = {x:y for x,y in zip(["Adolf","Luis","David","Oli","Gabo","Adrian","Gaby"],
                     [round(random.random()*100) for x in range(7)])}

for x,y in consumo.items():
    print(f"{x} dijo el numero {y}", sep="\n")
    
print(f"\n El numero mas grande fue {max(consumo.values())}, el mas pequeño fue {min(consumo.values())}")

# COMMAND ----------


