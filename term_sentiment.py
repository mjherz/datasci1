import json
import sys

######################
#read data from unicode file, last line removed in notepad
#read into appended list to index
######################
#script, filename = argv
#infile = open("outline20.txt").read().decode('utf-16').split('\n')
infile = open(sys.argv[2],"r").read().decode('utf-16').split('\n')
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
afinnfile = open(sys.argv[1])
scores = {} 
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. 
  scores[term] = int(score)  # Convert the score to an integer.

#print len(scores.items()),type(scores.items()),scores.items()[0]

linescore=[0]*i
nomatchdict=[]
for j in range(0,i):
  lineinit=0
# print "LINE ",j," TEXT",text[j]
  scoreditems=[]
  nomatchline=[]
  for k in range(len(text[j])):
    matchdict='FALSE'
    l=0
    while (l<len(scores.items()) and (matchdict=='FALSE')):
      if(text[j][k]==scores.items()[l][0]):
        lineinit=lineinit+scores.items()[l][1]
        matchdict='TRUE'
        scoreditems.append(scores.items()[l][1])
#       print scores.items()[l]
      l=l+1
    if (matchdict=='FALSE'):
      nomatchline.append(text[j][k])
  linescore[j]=float(lineinit)
# print "TOTAL=",linescore[j]
#####################
#after done with line, run through all words and assign them values of known
#####################
  for m in range(len(nomatchline)):
    n=0
    matchdict='FALSE'
    while ((n<len(nomatchdict)) and (matchdict=='FALSE')):
      if (nomatchline[m]==nomatchdict[n][0]):
#       nomatchdict[n][1].append(scoreditems)  #INCORRECT
        nomatchdict[n][1]=nomatchdict[n][1]+scoreditems  
        matchdict='TRUE'
      n=n+1
    if (matchdict=='FALSE'):
      nomatchdict.append([nomatchline[m],scoreditems])

######################
#calculate score for each line
######################
for p in range(len(nomatchdict)):
  if(nomatchdict[p][1]==[]):
    nomatchdict[p][1]=[0]  
    nomatchdict[p].append([0])
  else:
    averageword=float(sum(nomatchdict[p][1])/float(len(nomatchdict[p][1])))
    nomatchdict[p].append([averageword]) 

######################
#print score for each line
######################
for p in range(len(nomatchdict)):
  print nomatchdict[p][0],nomatchdict[p][2][0]
