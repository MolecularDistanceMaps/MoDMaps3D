
filename = "Haplogroups_African.txt"

import numpy as np

fout = ("output.txt", "w")
fin = open(filename, "r")
dt = fin.readlines()
s = 0
for i,line in enumerate(dt):
	# print i,line.strip()
	if i %10 ==3 and i > 3:
		tmp = str(line.strip())
		print tmp
		# print len(tmp)
		s += 1

mapsize = np.sum(map(int,dt[0].split(",")))
if s != mapsize:
	print "NUMBERS DO NOT MATCH!!!"
	print s, mapsize


