# ==========================================================
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: B/P1 
# Latihan: Jalur Terpendek Antar Kota
# Algoritma: Dijkstra
# ==========================================================
import heapq

# 1. Representasi graph berbobot menggunakan dictionary
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # 2. Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # 3. Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, lewati
        if current_distance > distances[current_node]:
            continue

        # 4. Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 5. Input node awal (Bogor)
hasil = dijkstra(graph, 'Bogor')

# Output jarak terpendek dari Bogor ke semua kota
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")

# ==========================================================
# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
#    = Bogor
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    = Depok (2)
# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    = Bandung (8)
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
#    = Algoritma Dijkstra memulai dari node Bogor dengan jarak 0,
#      lalu memilih jalur dengan bobot terkecil secara bertahap menggunakan priority queue.
#      Setiap kali menemukan jalur lebih pendek ke suatu kota, jarak diperbarui.
#      Proses berlanjut hingga semua node sudah diperiksa, menghasilkan jarak terpendek
#      dari Bogor ke Jakarta (4), Depok (2), dan Bandung (8).
# ==========================================================
