# ========================================================== 
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1
# Latihan 4: Membuat BST yang Tidak Seimbang 
# ========================================================== 
 
# Class Node untuk menyimpan data BST
# Node memiliki atribut data untuk menyimpan nilai, left untuk child kiri, dan right untuk child kanan. 
class Node: 
    def __init__(self, data): 
        self.data = data      # nilai pada node 
        self.left = None      # child kiri 
        self.right = None     # child kanan 
 
 
# Fungsi insert untuk BST 
# Fungsi ini digunakan untuk memasukkan data ke dalam BST. Alur fungsi insert adalah sebagai berikut:
#1. Jika root kosong, buat node baru dengan data dan kembalikan node tersebut
def insert(root, data): 
    # Jika root kosong, buat node baru 
    if root is None: 
        return Node(data) #2. Jika data lebih kecil dari data pada root, masukkan data ke subtree kiri
 
    # Jika data lebih kecil, masuk ke subtree kiri 
    if data < root.data: 
        root.left = insert(root.left, data) #3. Jika data lebih besar dari data pada root, masukkan data ke subtree kanan dengan memanggil fungsi insert pada child kanan root
 
    # Jika data lebih besar, masuk ke subtree kanan 
    elif data > root.data: 
        root.right = insert(root.right, data) #4. Jika data sama dengan data pada root, tidak perlu memasukkan (BST tidak boleh memiliki duplikat)
 
    return root #5. Kembalikan root setelah proses penyisipan selesai
 
 
# Fungsi preorder untuk melihat bentuk tree 
def preorder(root): 
    if root is not None: #1. Jika root tidak kosong, lakukan langkah berikut:
        print(root.data, end=" ") #2. Kunjungi node saat ini (root) dan tampilkan datanya
        preorder(root.left) #3. Kunjungi subtree kiri dengan memanggil fungsi preorder pada child kiri root
        preorder(root.right) #4. Kunjungi subtree kanan dengan memanggil fungsi preorder pada child kanan root
    #5. Jika root kosong, kembalikan (tidak melakukan apa-apa
 
 
# Fungsi sederhana untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): # Fungsi ini digunakan untuk menampilkan struktur tree dengan indentasi berdasarkan level dan posisi node (Root, L untuk kiri, R untuk kanan). Alur fungsi tampil_struktur adalah sebagai berikut:
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") #1. Jika root tidak kosong, tampilkan posisi dan data node dengan indentasi sesuai level
        tampil_struktur(root.left, level + 1, "L") #2. Kunjungi subtree kiri dengan memanggil fungsi tampil_struktur pada child kiri root, tingkatkan level dan set posisi ke "L"
        tampil_struktur(root.right, level + 1, "R") #3. Kunjungi subtree kanan dengan memanggil fungsi tampil_struktur pada child kanan root, tingkatkan level dan set posisi ke "R"
    #4. Jika root kosong, kembalikan (tidak melakukan apa-apa)
# ----------------------------- 
# Program utama 
# ----------------------------- 
root = None 
# Data dimasukkan berurutan naik 
data_list = [10, 20, 30] 
# Kita iterasi melalui setiap data dalam daftar tersebut dan memanggil fungsi insert untuk memasukkan data ke dalam BST. Setelah semua data dimasukkan, kita mencetak pesan bahwa data berhasil dimasukkan ke dalam BST.
for data in data_list: 
    root = insert(root, data) #Memanggil fungsi insert untuk setiap data dalam daftar, memperbarui root setiap kali data baru dimasukkan ke dalam BST

print("Preorder BST:") #Memanggil fungsi preorder untuk menampilkan isi BST dalam urutan preorder (root, kiri, kanan)
preorder(root) #Outputnya akan menampilkan data dalam urutan preorder yaitu 10 20 30 karena data dimasukkan berurutan naik sehingga membentuk BST yang tidak seimbang ke kanan.

print("\n\nStruktur BST:") #Memanggil fungsi tampil_struktur untuk menampilkan struktur tree. Fungsi ini akan menampilkan posisi dan data setiap node dalam BST dengan indentasi yang menunjukkan levelnya. Dalam kasus ini, karena data dimasukkan berurutan naik, maka struktur BST akan terlihat seperti berikut:
# Root: 10
tampil_struktur(root) #Outputnya akan menampilkan struktur BST dengan Root 10, lalu child kanan 20, dan child kanan dari 20 adalah 30. Tidak ada child kiri karena data dimasukkan berurutan naik sehingga membentuk BST yang tidak seimbang ke kanan.