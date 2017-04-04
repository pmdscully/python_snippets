import numpy as np
import matplotlib.pyplot as plt

data1 = [5,5,4,3,3,5]
data2 = [6,6,4,6,8,5]
data3 = [7,8,4,5,8,2]
data4 = [6,9,3,6,8,4]

data 		= [data1, data3, data2, data4]
labels_list = ['a','b','c','d']
width		= 0.3
symbol		= 'r+'
ymin 		= 0
ymax 		= 10

ax = plt.gca()
ax.set_ylim(ymin,ymax)
ax.set_xticklabels( labels_list, rotation=0 )
ax.grid(True)
ax.set_axisbelow(True)
plt.xlabel('X axis label')
plt.ylabel('Y axis label')
plt.boxplot(data, widths=width)

plt.savefig('boxplot.png')
plt.savefig('boxplot.pdf')
#plt.show()
