#=============================================
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1 
# Materi 2 : Algoritma Bellman Ford
#=============================================

def bellman_ford(graph, start):
    # Inisialisasi jarak
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Relaksasi berulang sebanyak |V|-1 kali
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Pengecekan siklus negatif
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph mengandung siklus negatif!")

    return distances
