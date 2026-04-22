# ========================================================== 
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1 
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang 
# ========================================================== 
 
# Class Node
# 1. Definisi kelas Node untuk simpul BST
class Node:
    def __init__(self, key):
        self.key = key        # Nilai data pada node
        self.left = None      # Anak kiri
        self.right = None     # Anak kanan

# 2. Fungsi rotasi kanan
def rightRotate(y): # Fungsi ini digunakan untuk melakukan rotasi kanan pada node y. Alur fungsi rightRotate adalah sebagai berikut:
    # y adalah root lama
    x = y.left          # Ambil anak kiri dari y (20)
    T2 = x.right        # Simpan subtree kanan dari x (None)

    # Lakukan rotasi
    x.right = y         # Jadikan y (30) sebagai anak kanan dari x (20)
    y.left = T2         # Subtree T2 (None) dipasang sebagai anak kiri dari y (30)

    return x            # Root baru adalah x (20)

# 3. Fungsi inorder traversal untuk menampilkan isi BST
def inorder(root): # Fungsi ini digunakan untuk melakukan inorder traversal pada BST. Alur fungsi inorder adalah sebagai berikut:
    if root is not None: #1. Jika root tidak kosong, lakukan langkah berikut:
        inorder(root.left) #2. Kunjungi node saat ini (root) dan tampilkan datanya
        print(root.key, end=" ") #3. Kunjungi subtree kanan dengan memanggil fungsi inorder pada child kanan root
        inorder(root.right) #4. Jika root kosong, kembalikan (tidak melakukan apa-apa)


# 4. Program utama
# Buat BST tidak seimbang: 30 -> 20 -> 10
root = Node(30) # Root utama bernilai 30
root.left = Node(20) # Child kiri dari root adalah 20
root.left.left = Node(10) # Child kiri dari 20 adalah 10, sehingga membentuk BST yang tidak seimbang ke kiri

print("Sebelum Rotasi (Inorder):") # Memanggil
inorder(root)   # Output: 10 20 30
print("\nStruktur: 30 -> 20 -> 10 (tidak seimbang)") # Menampilkan struktur BST sebelum rotasi, dimana 30 adalah root, 20 adalah anak kiri dari 30, dan 10 adalah anak kiri dari 20. Tidak ada anak kanan karena data dimasukkan berurutan turun sehingga membentuk BST yang tidak seimbang ke kiri.

# Lakukan rotasi kanan pada root
root = rightRotate(root) # Setelah rotasi kanan, root baru adalah 20, dengan 10 sebagai anak kiri dan 30 sebagai anak kanan. Struktur BST sekarang menjadi seimbang.

print("\nSesudah Rotasi Kanan (Inorder):") # Memanggil
inorder(root)   # Output: 10 20 30
print("\nStruktur: 20 sebagai root, dengan anak kiri 10 dan anak kanan 30 (seimbang)") # Menampilkan struktur BST setelah rotasi, dimana 20 adalah root, 10 adalah anak kiri dari 20, dan 30 adalah anak kanan dari 20. Struktur ini sekarang seimbang karena kedua anak dari root memiliki kedalaman yang sama.



