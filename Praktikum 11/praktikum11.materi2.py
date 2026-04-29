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

def bfs(graph, start):
    #fungsi untuk melakukan penelusuran dengan bfs
    #graph ini adalah dictionary yang menyimpan struktur dari graph
    #start node awal penelusuran
    #queue untuk menyimpan node yang akan dikunjungi
    queue = deque()
    visited = set() #set untuk menyimpan node yang sudah dikunjungi

    queue.append(start) #tambahkan node awal ke dalam antrian

    visited.add(start) #tandai node awal sebagai sudah dikunjungi

    while queue:
        node = queue.popleft() #ambil node dari antrian

        #tampilkan
        print(node, end=" ")


        #periksa semua tetangga dari node yang sedang dikunjungi
        for neighbor in graph[node]:
            #jika tetangga belum dikunjungi, tambahkan ke dalam antrian dan tandai sebagai sudah dikunjungi
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
bfs(graph, 'A')
