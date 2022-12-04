import os
import pandas as pd

os.chdir("/Users/anto/Desktop/Advent of Code/Advent-of-Code/JOUR 4")
data = pd.read_csv("input.txt")


data = data.assign(Zone1_Deb = str(None) ,
                       Zone1_Fin = str(None),
                       Zone2_Deb = str(None),
                       Zone2_Fin=str(None))

val = 0
for i in range(len(data)):
    data["Zone1_Deb"].loc[i] = int(str(data["Zone1"].loc[i].replace("\n","")).split("-")[0])
    data["Zone1_Fin"].loc[i] = int(str(data["Zone1"].loc[i].replace("\n","")).split("-")[1])
    data["Zone2_Deb"].loc[i] = int(str(data["Zone2"].loc[i].replace("\n","")).split("-")[0])
    data["Zone2_Fin"].loc[i] = int(str(data["Zone2"].loc[i].replace("\n","")).split("-")[1])

    z1_d =int(str(data["Zone1"].loc[i].replace("\n","")).split("-")[0])
    z1_f =int(str(data["Zone1"].loc[i].replace("\n","")).split("-")[1])
    z2_d =int(str(data["Zone2"].loc[i].replace("\n","")).split("-")[0])
    z2_f =int(str(data["Zone2"].loc[i].replace("\n","")).split("-")[1])

    seq1 = range(z1_d,z1_f)
    seq2 = range(z2_d, z2_f)
    if(z2_d >= z1_d) and (z2_f <= z1_f):
            val = val +1
    elif(z1_d >= z2_d) and (z1_f <= z2_f):
            val = val +1
print(val)
