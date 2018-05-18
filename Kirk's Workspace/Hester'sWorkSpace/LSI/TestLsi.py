from LSI import LSI_TFIDF as LSI
from LSI import LSI_NLP as LSINLP
import time

time_start = time.clock()
lsi=LSI.LSI_TFIDF()
time_end = time.clock()
print("ini: ")
print(time_end-time_start)

# lsi.indexing()

# Indexing python_6k
# lsi.path       = "C:\\Users\\soapk\\Desktop\\python_6k"
# lsi.index_path = 'C:\\Users\\soapk\\Desktop\\LSIindex_python_6k.pik'

# print(lsi.path)
# print(lsi.index_path)

# time_start = time.clock()
# result=lsi.getResult("hashlib.md5()")
# time_end = time.clock()
# print("search:")
# print(time_end-time_start)
# result.to_string()

# Indexing java_6k
lsi.path       = "C:\\Users\\soapk\\Desktop\\java_6k"
lsi.index_path = 'C:\\Users\\soapk\\Desktop\\LSIindex_java_6k.pik'

time_start = time.clock()
result=lsi.getResult("hashlib.md5()")
time_end = time.clock()
print("search:")
print(time_end-time_start)
result.to_string()

# Indexing so_50k
lsi_nlp = LSINLP.LSI_TFIDF()
time_start = time.clock()
result = lsi_nlp.getResult("how to sort a list")
time_end = time.clock()
print("search:")
print(time_end-time_start)
result.to_string()

# time_start = time.clock()
# dList=lsi.getDocumentList("min", 1)
# time_end = time.clock()
# print("search: ")
# print(time_end-time_start)