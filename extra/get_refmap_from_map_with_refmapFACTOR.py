import numpy as np
import random

random.seed(a=12345)
refmapFactor = 0.04
file = "Haplogroups_All.txt"
fin = open(file,"r")
dt = fin.readlines()

groupsAvailable = map(int,dt[0].split(","))
totseq = np.sum(groupsAvailable)
names1 = dt[5].strip().split(",")

print groupsAvailable
print totseq
print names1

filenamesets = "["
for i in names1:
  filenamesets += '"'+i.split(" (")[0]+'", '
filenamesets = filenamesets[:-2]
filenamesets += "]"

filecolorsets = "["
for i in dt[1].strip().split(","):
  filecolorsets += '"'+i+'", '
filecolorsets = filecolorsets [:-2]
filecolorsets += "]"


allacc = []
for i,line in enumerate(dt):
    if i%10==3 and i >3:
      allacc.append(line.strip())
# print allacc  


out = ""
outputset="["
curpos=0
tot_seq_in_refmap = 0
for i in xrange(len(groupsAvailable )):
  localout = '"'
  this_group_tot_seq_in_refmap = 0
  print "group= "+str(i), groupsAvailable[i]
  if groupsAvailable[i] > 0:
    # print len(groupsAvailable[i])
    for j in xrange(groupsAvailable[i]):
      if random.uniform(0,1) <= refmapFactor:
      	localout  += allacc[curpos]+", "
      	this_group_tot_seq_in_refmap += 1
      curpos +=1
    if this_group_tot_seq_in_refmap > 0:
      localout = localout [:-2]
  print this_group_tot_seq_in_refmap
  tot_seq_in_refmap += this_group_tot_seq_in_refmap
  localout += '"'
  outputset +=localout+",\n\n"  

outputset = outputset [:-3]
outputset += "\n]"
# print outputset 

out += outputset  
out +="\n}"

print
print
outheader = '{'
outheader += '"mapDescription": "'+str(tot_seq_in_refmap)+' '+ " ".join(file.split(".")[0].split("_")[:])+'",\n'
outheader += '"numofsets": '+str(len(groupsAvailable))+',\n'
outheader += '"namesets": '+str(filenamesets)+',\n'
outheader += '"colorsets": '+str(filecolorsets)+',\n\n'
outheader += '"sets": '

out = outheader + out
# print out
print file.split(".")[0]
print tot_seq_in_refmap

fout = open("refmap_"+file.split(".")[0]+".txt", "w")
fout.write(out)
fout.close()

