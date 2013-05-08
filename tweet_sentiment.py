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

#for i in range(10):
#  print result[i]["iso_language_code"]
#  print result[i]["text"]

######################
#break into strings
######################
text=['']*i
for j in range(0,i):
  if "text" in ldata[j]:
    str1=ldata[j]["text"].encode('utf-8')
#   print j, str1
    text[j]=str1.split()
# else:
#   print j,'key not found'

#print text[0][5],len(text[0])

######################
#from createdict1.py
#create dictionary from AFINN
######################
afinnfile = open("AFINN-111.txt")
scores = {} 
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. 
  scores[term] = int(score)  # Convert the score to an integer.

#print len(scores.items()),type(scores.items()),scores.items()[0]

linescore=[0]*i
for j in range(0,i):
  lineinit=0
# print "LINE ",j
# print text[j]
  for k in range(len(text[j])):
    for l in range(len(scores.items())):
      if(text[j][k]==scores.items()[l][0]):
        lineinit=lineinit+scores.items()[l][1]
#       print text[j][k],' MATCH=',scores.items()[l][1] 
#     else:
#       print 'NOMATCH'
  linescore[j]=lineinit
# print "TOTAL=",linescore[j]
  print float(linescore[j])
