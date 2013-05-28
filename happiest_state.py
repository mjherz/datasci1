import json
import sys
import random

##########################################################################

def createtextloc(ldata,linect,USline,text,location):

  for j in range(0,linect):
    if "text" in ldata[j]:
      str1=ldata[j]["text"].encode('utf-8')
      text[j]=str1.split()
      if ldata[j]["place"]!=None:
        if ldata[j]["place"]["full_name"]!=None:
          if ldata[j]["place"]["country_code"].encode('utf-8')=="US":
            str1=ldata[j]["place"]["full_name"].encode('utf-8').split(', ')
            USline.append(j)
            if str1[1]=='US':
              location[j]=str1[0]
            else:
              location[j]=str1[1]

##########################################################################

def convert(location,USline,states): 

  states = {
  "VERMONT": "VT", 
  "GEORGIA": "GA", 
  "IOWA": "IA", 
  "Armed Forces Pacific": "AP", 
  "GUAM": "GU", 
  "KANSAS": "KS", 
  "FLORIDA": "FL", 
  "AMERICAN SAMOA": "AS", 
  "NORTH CAROLINA": "NC", 
  "HAWAII": "HI", 
  "NEW YORK": "NY", 
  "CALIFORNIA": "CA", 
  "ALABAMA": "AL", 
  "IDAHO": "ID", 
  "FEDERATED STATES OF MICRONESIA": "FM", 
  "Armed Forces Americas": "AA", 
  "DELAWARE": "DE", 
  "ALASKA": "AK", 
  "ILLINOIS": "IL", 
  "Armed Forces Africa": "AE", 
  "SOUTH DAKOTA": "SD", 
  "CONNECTICUT": "CT", 
  "MONTANA": "MT", 
  "MASSACHUSETTS": "MA", 
  "PUERTO RICO": "PR", 
  "Armed Forces Canada": "AE", 
  "NEW HAMPSHIRE": "NH", 
  "MARYLAND": "MD", 
  "NEW MEXICO": "NM", 
  "MISSISSIPPI": "MS", 
  "TENNESSEE": "TN", 
  "PALAU": "PW", 
  "COLORADO": "CO", 
  "Armed Forces Middle East": "AE", 
  "NEW JERSEY": "NJ", 
  "UTAH": "UT", 
  "MICHIGAN": "MI", 
  "WEST VIRGINIA": "WV", 
  "WASHINGTON": "WA", 
  "MINNESOTA": "MN", 
  "OREGON": "OR", 
  "VIRGINIA": "VA", 
  "VIRGIN ISLANDS": "VI", 
  "MARSHALL ISLANDS": "MH", 
  "WYOMING": "WY", 
  "OHIO": "OH", 
  "SOUTH CAROLINA": "SC", 
  "INDIANA": "IN",
  "NEVADA": "NV",
  "LOUISIANA": "LA", 
  "NORTHERN MARIANA ISLANDS": "MP", 
  "NEBRASKA": "NE", 
  "ARIZONA": "AZ", 
  "WISCONSIN": "WI", 
  "NORTH DAKOTA": "ND", 
  "Armed Forces Europe": "AE", 
  "PENNSYLVANIA": "PA", 
  "OKLAHOMA": "OK", 
  "KENTUCKY": "KY", 
  "RHODE ISLAND": "RI", 
  "DISTRICT OF COLUMBIA": "DC", 
  "ARKANSAS": "AR", 
  "MISSOURI": "MO", 
  "TEXAS": "TX", 
  "MAINE": "ME"
  }
  for i in USline:
    if location[i].upper() in states:
      location[i]=states[location[i].upper()]
    
##########################################################################

#def createnomatch(scores,text,dictline):
def createnomatch(scores,text):

  nomatchdict=[]
  for j in range(len(text)):
    print "Line",j
    scoreditems=[]
    nomatchline=[]
    for k in range(len(text[j])):
      if(text[j][k] in scores):
        scoreditems.append(scores[text[j][k]])
      else:
        scores[text[j][k]]=0
        nomatchline.append(text[j][k])

#####################
#after done with line, run through all words and assign them values of known
#####################
    for m in range(len(nomatchline)):
      n=0
      matchdict='FALSE'
      while ((n<len(nomatchdict)) and (matchdict=='FALSE')):
        if (nomatchline[m]==nomatchdict[n][0]):
          nomatchdict[n][1]=nomatchdict[n][1]+scoreditems  
          matchdict='TRUE'
        n=n+1
      if (matchdict=='FALSE'):
        nomatchdict.append([nomatchline[m],scoreditems])

######################
#calculate score for each new term 
######################
  for p in range(len(nomatchdict)):
    if(nomatchdict[p][1]==[]):
      nomatchdict[p][1]=[0]  
    else:
      averageword=float(sum(nomatchdict[p][1])/float(len(nomatchdict[p][1])))
      nomatchdict[p][1]=[averageword]  
    scores[nomatchdict[p][0]]=float(nomatchdict[p][1][0])

##########################################################################

def applyscore(scoreline,location,scores,text,USline):

  for j in range(len(USline)):
    linenum=USline[j]
    linescore=0
    for k in range(len(text[linenum])):
      if text[linenum][k] in scores:
        linescore=linescore+scores[text[linenum][k]]
    scoreline.append([linescore,location[linenum]])

##########################################################################

def findstate(scoreline,statescore):

  for i in range(len(scoreline)):
    if scoreline[i][1] in statescore:
      statescore[scoreline[i][1]]=scoreline[i][0]+statescore[scoreline[i][1]]
    else:
      statescore[scoreline[i][1]]=0


##########################################################################
#main
##########################################################################

######################
#read data from unicode file, last line removed in notepad
#read into appended list to index
######################
#infile = open("outline20.txt").read().decode('utf-16').split('\n')
infile = open(sys.argv[2],"r").read().decode('utf-16').split('\n')
linect=0
ldata=[]
for line in infile:
  data=json.loads(line)
  linect=linect+1
  ldata.append(data)
print "Read data"    

######################
#break into strings
#find location and text
######################
USline=[]
text=['']*linect
location=['']*linect
createtextloc(ldata,linect,USline,text,location)
print "Parsed data"

#####################
#Convert state to abbreviation
#####################
states={}
convert(location,USline,states)
print "Converted abbreviation"

######################
#from createdict1.py
#create dictionary from AFINN
######################
afinnfile = open(sys.argv[1])
scores = {} 
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. 
  scores[term] = int(score)  # Convert the score to an integer.
print "Read affinity file"

######################
#Using algorithm in p3, create nomatchdict
######################
#dictbasedline=list(USline)
#for y in range(100*len(USline)):
#  dictbasedline.append(random.randint(0,linect-1))
#createnomatch(scores,text,dictbasedline)
createnomatch(scores,text)
#print "Created no match dictionary from",len(dictbasedline),"lines"

######################
#Calculate score for each line
######################
scoreline=[]
applyscore(scoreline,location,scores,text,USline)
print "Calculated score for each line with state"

######################
#Find state with highest score
######################
statescore={}
findstate(scoreline,statescore)
print "Found state with highest score"
print max(statescore.iterkeys(), key=(lambda key: statescore[key]))
