import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

fig = plt.figure() 
ax = fig.add_subplot(111)

import kNN

datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
plt.show()  
