import MapReduce
import sys
import collections

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
    A = record[0]
#   value = record[1]
    B = record[1]
#   words = value.split()
#   for w in words:
#     mr.emit_intermediate(w, 1)
    mr.emit_intermediate(A,B)
    mr.emit_intermediate(B,A)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
#   total = 0
#   for v in list_of_values:
#     total += v
#   mr.emit((key, total))
    y=collections.Counter(list_of_values)
    duplicates=[i for i in y if y[i]>1]
    for i in range(len(list_of_values)):
      if (list_of_values[i] not in duplicates):
        mr.emit((key, list_of_values[i]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
