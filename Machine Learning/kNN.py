# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:24:43 2017

@author: AYEAH
"""

from numpy import *
import operator

def createDateSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

group, labels = createDateSet()
group.shape[0]
labels


#k-近邻算法
def classify0(inx, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inx, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

classify0([0,0], group, labels, 3)

#测试
dataSetSize = group.shape[0]
diffMat = tile([0,0], (dataSetSize,1)) - group
sqDiffMat = diffMat**2
sqDistances = sqDiffMat.sum(axis=1)
distances = sqDistances**0.5
sortedDistIndicies = distances.argsort()
k=3
classCount = {}
for i in range(k):
    voteIlabel = labels[sortedDistIndicies[i]]
    classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse=True)
sortedClassCount[0][0]

#Text record
def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    fr= open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append((listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

datingDataMat, datingLabels = file2matrix(r"C:\Users\AYEAH\Desktop\Learn Python\Machine Learning\datingTestSet.txt")

fr=open("C:\\Users\\AYEAH\\Desktop\\Learn Python\\Machine Learning\\datingTestSet.txt")


import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*datingLabels,15.0*datingLabels)



#标签数字化
datingDataMat
datingLabels[0:20]
def factor(x):
    if x=='largeDoses':
        x=1
    elif x=='smallDoses':
        x=2
    else:
        x=3
    return x
a=factor(datingLabels[1])
datingLabels=list(map(factor,datingLabels))

f2 = plt.figure(2)
plt.subplot(211)
datingLabels=array(datingLabels)
plt.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*datingLabels,15.0*datingLabels)

plt.subplot(212)
plt.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*datingLabels,15.0*datingLabels)

#画图
x = rand(50,30)  
f1 = plt.figure(1)  
plt.subplot(211)  
plt.scatter(x[:,1],x[:,0])
plt.subplot(212)  
label = list(ones(20))+list(2*ones(15))+list(3*ones(15))  
label = array(label)  
plt.scatter(x[:,1],x[:,0],15.0*label,15.0*label) 

#标准化
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals- minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet, ranges, minVals


normMat, ranges, minVals = autoNorm(datingDataMat)

#模型检测
def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix(r"C:\Users\AYEAH\Desktop\Learn Python\Machine Learning\datingTestSet.txt")
    datingLabels=list(map(factor,datingLabels))
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m =normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount +=1.0
    print("the total error rate is: %f" % (errorCount/float(numTestVecs)))
    

datingClassTest()

#预测
def classifyPerson():
    resultList = ['not at all','in small doses', 'in large doses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels = file2matrix(r"C:\Users\AYEAH\Desktop\Learn Python\Machine Learning\datingTestSet.txt")
    datingLabels=list(map(factor,datingLabels))
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])
    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print("You will probably like this person:",resultList[classifierResult - 1])

classifyPerson()

percentTats = float(input("percentage of time spent playing video games?"))



