import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
#   key = record[0]
    if record[0]=="a":
      for k in range(0,5):
        key=(record[1],k)
        value = [record[0],record[2],record[3]]
        mr.emit_intermediate(key,value)
    else:
      for i in range(0,5):
        key=(i,record[2])
        value = [record[0],record[1],record[3]]
        mr.emit_intermediate(key,value)
#   value = record[1]
#   words = value.split()
#   for w in words:
#     mr.emit_intermediate(w, 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
#   for v in list_of_values:
#     total += v
#   mr.emit((key, total))
#   list_of_values.sort(key = lambda row: row[2])
    a=[0]*5
    b=[0]*5
    for i in range(len(list_of_values)):
      if list_of_values[i][0]=="a":
        a[list_of_values[i][1]]=list_of_values[i][2]
    for i in range(len(list_of_values)):
      if list_of_values[i][0]=="b":
        b[list_of_values[i][1]]=list_of_values[i][2]
    total=0
    for i in range(0,5):
      total+=(a[i]*b[i])
#   mr.emit((key,total))
    mr.emit((key[0],key[1],total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
