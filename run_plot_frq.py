import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
with open('OUTPUT_SP_PEB_FRQ.csv', 'r') as f: frq_data = [[int(j) for j in i if j.isdigit()] for i in csv.reader(f)][1:]
x = [i[0] for i in frq_data]
y = [i[1] for i in frq_data]
z = [i[2] for i in frq_data]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
plt.show()
