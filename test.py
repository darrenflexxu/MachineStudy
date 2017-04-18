# -*- coding: cp936 -*-
import kNN
import matplotlib
import matplotlib.pyplot as plt

datingDataMat, datingLabels = kNN.file2matrix('data.txt')

print 'datingDataMat'
print datingDataMat

normMat, ranges, minVals = kNN.autoNorm(datingDataMat)

print '归一化特征值'
print normMat

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
plt.show()

