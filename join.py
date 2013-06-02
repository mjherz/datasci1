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
#   value = record[1]
    order_id = record[1]
    list_record=[record[0],record[2:len(record)]]
#   words = value.split()
#   for w in words:
#     mr.emit_intermediate(w,1)
    mr.emit_intermediate(order_id,list_record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
#   total = 0
#   for v in list_of_values:
#     total += v
#   mr.emit((key, total))
    line_item_list=[]
    order_list=[]
    for i in range(len(list_of_values)):
      if list_of_values[i][0]=="line_item":
        line_item_list.append(list_of_values[i])
      else:
        order_list.append(list_of_values[i])
    joinstr=r'", "'
    for i in range(len(order_list)):
      for j in range(len(line_item_list)):
        returnlist=["order",key,joinstr.join(order_list[i][1]),"line_item",key,joinstr.join(line_item_list[j][1])]
#       returnlist=["order",key,"\', \'".join(order_list[i][1]),"line_item",key,', '.join(line_item_list[j][1])]
        mr.emit(returnlist)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
