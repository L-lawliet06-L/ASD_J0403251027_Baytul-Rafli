# ========================================================== 
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: B/P1 
# Latihan 3: Implementasi Bellman-Ford 
# ========================================================== 

# Weighted graph dengan bobot negatif 
graph = { 
    'A': {'B': 5, 'C': 4}, 
    'B': {}, 
    'C': {'B': -2} 
} 

def bellman_ford(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Bellman-Ford. 
    """ 

    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 

    # Jarak dari start ke start adalah 0 
    distances[start] = 0 

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1 
    for _ in range(len(graph) - 1): 
        # Periksa semua edge 
        for node in graph: 
            for neighbor, weight in graph[node].items(): 
                # Jika jarak ke node saat ini sudah diketahui, 
                # dan ditemukan jarak yang lebih kecil ke neighbor, 
                # maka lakukan update jarak 
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 

    return distances 

hasil = bellman_ford(graph, 'A') 

print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance) 

# Jawaban Analisis: 
# 1. Berapa bobot langsung dari A ke B? 
#    = 5
# 2. Berapa total bobot jalur A -> C -> B? 
#    = 4 + (-2) = 2
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B? 
#    = Jalur A -> C -> B (total bobot 2 lebih kecil daripada bobot langsung 5).
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif? 
#    = Karena algoritma ini tetap melakukan relaksasi berulang kali 
#      dan bisa mendeteksi jika ada siklus negatif, sehingga tetap aman 
#      untuk bobot negatif (selama tidak ada negative cycle).
# 5. Apa yang dimaksud dengan proses relaksasi edge? 
#    = Proses membandingkan jarak saat ini dengan jarak baru melalui suatu edge, 
#      lalu memperbarui jarak jika jalur baru lebih pendek.
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra? 
#    = Dijkstra hanya cocok untuk bobot positif dan menggunakan priority queue, 
#      sedangkan Bellman-Ford bisa menangani bobot negatif dengan relaksasi berulang 
#      dan mampu mendeteksi siklus negatif.
