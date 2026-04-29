# ========================================================== 
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1 
# Impelentasi BFS
# ========================================================== 

#struktur data untuk membuat antrian, kita gunakan collection dari bawaan python
from collections import deque

#implementasi graph
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}

def dfs(graph, node, visited):
    #fungsi untuk melakukan penelusuran graph menggunakan DFS
    #graph : dictionary yang menyimpan graph
    #node : menyimpan node yang sedang dikunjungi
    #visited : menyimpan node yang sudah dikunjungi

    #tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)

    #tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    #periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        #jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            #lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)

#Menjalankan dfs dari A

visited = set() #set untuk menyimpan node yang sudah dikunjungi

dfs(graph, "A", visited)
