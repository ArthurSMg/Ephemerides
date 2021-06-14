# https://in-the-sky.org/data/asteroids.php#     ###Website to get the data about the asteroid position

import pandas
import numpy as np
import matplotlib.pyplot as plt

## READING THE FILE
data= pandas.read_csv("eph_table.csv",skiprows=2)   #reading the file
print(data["AU"])  #printing a list of only the data position in astronomical units


## DOING THE GRAPH
plt.figure(figsize=(10,5))  #size of the grap
ax = plt.axes()
#ax.set_facecolor("#e6e6e6")   #here you can put color to the backgournd 
dias = np.linspace(0,500,500)     #number of days used
plt.plot(dias, data["AU"].head(500), lw = 3)  #ploting 
plt.ylabel("Distancia ao Sol (AU)")
plt.xlabel("Dias")
plt.title("Efemerides de 4Vega")

plt.show()  #generates the graph

## ADITIONAL INFORMATION
apogeu = max(data["AU"])  #gets you the apogee
perigeu = min(data["AU"])  #gets you the perigee

print("Afelio:", apogeu)
print("Perielio:", perigeu)

