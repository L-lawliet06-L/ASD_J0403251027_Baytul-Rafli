# ========================================================== 
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1 
#  Latihan 5: Rotasi Kiri pada BST Tidak Seimbang 
# ========================================================== 
 
# Class Node 
class Node: 
    def __init__(self, data): 
        self.data = data # menyimpan nilai pada node
        self.left = None # child kiri
        self.right = None # child kanan
 
 
# Fungsi preorder untuk melihat isi tree 
def preorder(root): 
    if root is not None: #1. Jika root tidak kosong, lakukan langkah berikut:
        print(root.data, end=" ") #2. Kunjungi node saat ini (root) dan tampilkan datanya
        preorder(root.left) #3. Kunjungi subtree kiri dengan memanggil fungsi preorder pada child kiri root
        preorder(root.right) #4. Kunjungi subtree kanan dengan memanggil fungsi preorder pada child kanan root
 
 
# Fungsi untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): # Fungsi ini digunakan untuk menampilkan struktur tree dengan indentasi berdasarkan level dan posisi node (Root, L untuk kiri, R untuk kanan). Alur fungsi tampil_struktur adalah sebagai berikut:
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") #1. Jika root tidak kosong, tampilkan posisi dan data node dengan indentasi sesuai level
        tampil_struktur(root.left, level + 1, "L") #2. Kunjungi subtree kiri dengan memanggil fungsi tampil_struktur pada child kiri root, tingkatkan level dan set posisi ke "L"
        tampil_struktur(root.right, level + 1, "R") #3. Kunjungi subtree kanan dengan memanggil fungsi tampil_struktur pada child kanan root, tingkatkan level dan set posisi ke "R"
 
 
# Fungsi rotasi kiri 
def rotate_left(x): # Fungsi ini digunakan untuk melakukan rotasi kiri pada node x. Alur fungsi rotate_left adalah sebagai berikut:
    # x adalah root lama 
    y = x.right       # y adalah child kanan x 
    T2 = y.left       # subtree kiri milik y disimpan sementara 
 
    # Proses rotasi 
    y.left = x        # x menjadi child kiri dari y 
    x.right = T2      # child kanan x diganti dengan T2 
 
    # y menjadi root baru 
    return y 
 
 
 
 
 
 
# ----------------------------- 
# Program utama 
# ----------------------------- 
# Membuat tree yang tidak seimbang: 
# 10 -> 20 -> 30 
root = Node(10) # Root utama bernilai 10
root.right = Node(20) # Child kanan dari root adalah 20
root.right.right = Node(30) # Child kanan dari 20 adalah 30, sehingga membentuk BST yang tidak seimbang ke kanan

print("Preorder sebelum rotasi kiri:") # Memanggil
preorder(root) # Outputnya akan menampilkan data dalam urutan preorder yaitu 10 20 30 karena data dimasukkan berurutan naik sehingga membentuk BST yang tidak seimbang ke kanan.

print("\n\nStruktur sebelum rotasi kiri:") # Memanggil fungsi tampil_struktur untuk menampilkan struktur tree sebelum rotasi
tampil_struktur(root) # Outputnya akan menampilkan struktur BST dengan Root 10, lalu child kanan 20, dan child kanan dari 20 adalah 30. Tidak ada child kiri karena data dimasukkan berurutan naik sehingga membentuk BST yang tidak seimbang ke kanan.
# Melakukan rotasi kiri pada root 
root = rotate_left(root) # Setelah rotasi kiri, node 20 menjadi root baru, node 10 menjadi child kiri dari 20, dan node 30 tetap menjadi child kanan dari 20. Sehingga struktur tree setelah rotasi kiri akan terlihat seperti berikut:

print("\nPreorder sesudah rotasi kiri:") # Memanggil
preorder(root) # Outputnya akan menampilkan data dalam urutan preorder yaitu 20 10 30 karena setelah rotasi kiri, node 20 menjadi root baru, node 10 menjadi child kiri dari 20, dan node 30 tetap menjadi child kanan dari 20.

print("\n\nStruktur sesudah rotasi kiri:") # Memanggil fungsi tampil_struktur untuk menampilkan struktur tree setelah rotasi
tampil_struktur(root)# Outputnya akan menampilkan struktur BST dengan Root 20, lalu child kiri 10, dan child kanan 30. Setelah rotasi kiri, node 20 menjadi root baru, node 10 menjadi child kiri dari 20, dan node 30 tetap menjadi child kanan dari 20. Sehingga struktur tree setelah rotasi kiri akan terlihat seperti berikut:
# Root: 20