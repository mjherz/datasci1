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
    document_id = record[0]
    value = record[1]
    words = value.split()
#   for w in words:
    for key in words:
#     mr.emit_intermediate(w,1)
      mr.emit_intermediate(key,document_id)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
#   total = 0
#   for v in list_of_values:
#     total += v
#   mr.emit((key, total))
    list_of_values = list(set(list_of_values))
    mr.emit((key, list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
