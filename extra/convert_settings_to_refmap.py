
import sys,os,glob

os.chdir(".")
s=0

for file in glob.glob("settings_*.txt"):
  s+=1
  print(file)
  fin = open(file, "r")
  data = fin.readlines()
  print "lines="+str(len(data))
  groups = int(data[0].strip())
  print "groups="+str(groups)+"\n"
  filenamesets = []
  filecolorsets = []
  filesets = []
  totseq = 0

  for index in range(0,groups):
  	# print index
  	filenamesets.append(data[3*index+1].strip())
  	filecolorsets.append(data[3*index+2].strip())
  	filesets.append(data[3*index+3].strip())
  	totseq += len(data[3*index+3].strip().split(","))
  	
  fin.close()

  # print filenamesets
  # print filecolorsets
  # print filesets

  out = '{'
  out += '"mapDescription": "'+str(totseq)+' '+ " ".join(file.split(".")[0].split("_")[1:])+'",\n'
  out += '"numofsets": '+str(groups)+',\n'
  out += '"namesets": '+str(filenamesets)+',\n'
  out += '"colorsets": '+str(filecolorsets)+',\n\n'
  out += '"sets": ['
  for index in range(0,groups):
  	out += '"'+filesets[index]+'",\n\n'
  # remove 2x \n + ,
  out = out[:-3]
  out += '\n]\n}'
  out = out.replace('\'','"')

  fout = open("refmap_"+"_".join(file.split("_")[1:]), "w")
  fout.write(out)
  fout.close()

print s



