import numpy as np

file = "Animalia_mtDNA_ClassInsecta.txt"
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


print
print
out = '{'
out += '"mapDescription": "'+str(totseq)+' '+ " ".join(file.split(".")[0].split("_")[:])+'",\n'
out += '"numofsets": '+str(len(groupsAvailable))+',\n'
out += '"namesets": '+str(filenamesets)+',\n'
out += '"colorsets": '+str(filecolorsets)+',\n\n'
out += '"sets": '

print out

allacc = []
for i,line in enumerate(dt):
    if i%10==3 and i >3:
      allacc.append(line.strip())

print allacc  

outputset="["
curpos=0
for i in xrange(len(groupsAvailable )):
  localout = '"'
  print "group= "+str(i), groupsAvailable[i]
  if groupsAvailable[i] > 0:
    for j in xrange(groupsAvailable[i]):
      localout  += allacc[curpos]+", "
      curpos +=1
    localout = localout [:-2]
  localout += '"'
  outputset +=localout+",\n\n"  

outputset = outputset [:-3]
outputset += "\n]"
# print outputset 

out += outputset  
out +="\n}"

print out

print file.split(".")[0]

fout = open("refmap_"+file.split(".")[0]+".txt", "w")
fout.write(out)
fout.close()


