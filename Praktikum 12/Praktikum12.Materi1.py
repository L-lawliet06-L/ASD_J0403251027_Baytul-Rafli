#=============================================
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1 
# Materi 1 :  Algoritma Dijkstra 
#=============================================

import heapq 
graph = { 
'A': {'B': 4, 'C': 2}, 
'B': {'D': 5}, 
'C': {'D': 1}, 
'D': {} 
} 
 
 
def dijkstra(graph, start): 
    # Menyimpan jarak minimum 
    distances = {node: float('inf') for node in graph} 
 
    # Jarak node awal = 0 
    distances[start] = 0 
 
    # Priority queue 
    pq = [(0, start)] 
 
    while pq: 
        current_distance, current_node = heapq.heappop(pq) 
 
        # Periksa semua tetangga 
        for neighbor, weight in graph[current_node].items(): 
 
            distance = current_distance + weight 
 
            # Jika ditemukan jarak lebih kecil 
            if distance < distances[neighbor]: 
 
                distances[neighbor] = distance 
 
                heapq.heappush(pq, (distance, neighbor)) 
 
    return distances 
 
hasil = dijkstra(graph, 'A') 
print(hasil)

#Output : {'A': 0, 'B': 4, 'C': 2, 'D': 3} 
#Penjelasan : 
#• Jarak dari A ke A = 0  
#• Jarak dari A ke B = 4  
#• Jarak dari A ke C = 2  
#• Jarak dari A ke D = 3 
#Karena A ➔  C ➔  D = 2 + 1 = 3 
 
#Kelemahan utama algoritma Dijkstra adalah algoritma ini tidak dapat bekerja dengan benar 
#pada graph yang memiliki bobot negatif. Dijkstra menggunakan pendekatan greedy dengan 
#asumsi bahwa jarak terpendek yang sudah dipilih tidak akan berubah lagi, sehingga jika 
#terdapat edge dengan bobot negatif, algoritma dapat menghasilkan perhitungan shortest path 
#yang salah. Selain itu, pada graph yang sangat besar dengan jumlah node dan edge yang 
#banyak, proses perhitungan juga dapat menjadi lebih kompleks dan membutuhkan 
#penggunaan struktur data tambahan seperti priority queue agar tetap efisien.