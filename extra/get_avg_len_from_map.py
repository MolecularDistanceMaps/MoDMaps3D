fin = open("Haplogroups_3_L0-L6.txt", "r")
dt =fin.readlines()

alldata=[]
s=0
avg = 0
for i,line in enumerate(dt):
	# print i,line.strip()
	if i%10==5 and i>6:
		s+=1
		print i,line.strip()
		alldata.append(line.strip())
		avg += int(line.strip())

print s
print len(alldata)
print avg
print avg*1.0/s

# print (297060*20+ 205150*20)*1.0/40

