import json
import sys

######################
#read data from unicode file, last line removed in notepad
#read into appended list to index
######################
#script, filename = argv
#infile = open("outline20.txt").read().decode('utf-16').split('\n')
infile = open(sys.argv[1],"r").read().decode('utf-16').split('\n')
i=0
ldata=[]
for line in infile:
  data=json.loads(line)
  i=i+1
  ldata.append(data)

######################
#break into strings
######################
text=['']*i
for j in range(0,i):
  if "text" in ldata[j]:
    str1=ldata[j]["text"].encode('utf-8')
    text[j]=str1.split()

####################
#tally occurrence
####################
dict=[]
totalocc=0
for j in range(0,i):
  totalocc=totalocc+len(text[j])
  for k in range(len(text[j])):
    matchdict='FALSE'
    l=0
    while ((matchdict=='FALSE') and (l<len(dict))):
      if(text[j][k]==dict[l][0]):
        matchdict='TRUE'
        dict[l][1]=dict[l][1]+1
      l=l+1
    if (matchdict=='FALSE'):
      dict.append([text[j][k],1])

##################
#print output with frequency         
##################
for m in range(len(dict)):
  print dict[m][0],float(dict[m][1])/float(totalocc)
