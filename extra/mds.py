#######################################################
## MoDMaps3D                                         ##
## MultiDimensional Scaling in Python                ##
## Coded by Rallis Karamichalis                      ##
## Github Repo: https://github.com/rallis/MoDMaps3D  ##
#######################################################


import math, sys
import numpy as np
map_output = ""


print "Reading [mapheader.txt]\n"
header = open ("mapheader.txt", "r")
for line in header:
	map_output += line
header.close()


print "Reading [accIDs.txt]\n"
accIDs = open ("accIDs.txt", "r")
accessions = accIDs.readlines()
accIDs.close()	
tmp = accessions[0].split('"')
accessions = [tmp[it] for it in range(1,len(tmp),2)]


print "Reading [allSequences.txt]\n"
allSeq = open ("allSequences.txt", "r")
allSequences = allSeq.readlines()
allSeq.close()	
tmp = allSequences[0].split('"')
allSequences = [[tmp[it], tmp[it+2], tmp[it+4], tmp[it+6]] for it in range(1,len(tmp),8)]


print "Reading [dMatrix.txt]\n"
dMat = open ("dMatrix.txt", "r")
distMat = dMat.readlines()
dMat.close()
tmp = distMat[0].split('{')
dMat=[]
for row in range(2,len(tmp)):
	dMat.append(tmp[row].split("}")[0].split(","))
dMat = np.array(dMat, dtype="float64")


print "Computing eigenvalues..\n"
eigValues, eigVectors = np.linalg.eig(dMat)
idx = eigValues.argsort()[::-1][0:5]  
selEigValues = eigValues[idx]
selEigVectors = eigVectors[:,idx]
#print idx 
#print selEigValues.shape
#print selEigVectors.shape

if False in (selEigValues > 0):
    print "First 5 largest eigenvalues are not all positive. Exiting.."
    sys.exit(-1)


selEigVectors = np.array(selEigVectors)

diagValues = []
for i in range(len(selEigValues)):
    diagValues.append(math.sqrt(eigValues[i]))
#print diagValues
    
diag = np.diag(diagValues)
points = np.dot(selEigVectors,diag)
#print "pointsSize=", points.shape

minmaxScaling = []
for i in range(5):
	minmaxScaling.append([ min(points[:,i]), max(points[:,i]) ])
#print minmaxScaling

scaledPoints = []
for i in range(len(accessions)):
	scaledPoints.append([0, 0, 0, 0, 0])
	for j in range(5):
		scaledPoints[i][j] = 2.0 *(points[i][j] - minmaxScaling[j][0]) / ( minmaxScaling[j][1] - minmaxScaling[j][0]) - 1

print "Writing output [map_output.txt]\n"
for i in range(len(accessions)):
	map_output += str(scaledPoints[i][0]) + "\n"
	map_output += str(scaledPoints[i][1]) + "\n"
	map_output += str(scaledPoints[i][2]) + "\n"
	map_output += str(scaledPoints[i][3]) + "\n"
	map_output += str(scaledPoints[i][4]) + "\n"
	map_output += str(i) + "\n"
	map_output += allSequences[i][0] + "\n"
	map_output += allSequences[i][3].split("|")[-1] + "\n"
	map_output += allSequences[i][1] + "\n"
	map_output += allSequences[i][2] + "\n"


fout = open("map_output.txt", "w")
fout.write(map_output)
fout.close()

