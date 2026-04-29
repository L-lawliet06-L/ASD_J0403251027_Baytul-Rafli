# ========================================================== 
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1 
# Impelentasi dasar graph
# ========================================================== 
graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D'],
    'C' : ['A', 'D'],
    'D' : ['B', 'C'],
}
for node in graph:
    print(node, "->", graph[node])