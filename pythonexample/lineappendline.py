# coding=utf-8
file = open(r"")
fileMatrix = open(r"")
fileOutput =open(r"","w")

fileList=[fileLine for fileLine in file]
fileMatrix=[fileMatrixLine for fileMatrixLine in fileMatrix]

for fileList,fileMatrix in zip(fileList,fileMatrix):
    fileOutput.write(fileList.strip('\n')+fileMatrix)