#=============================================
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1
# Latihan 1 : BST
#=============================================

#Membuat Node
class Node:
    def __init__(self, data): 
        self.data = data #menyimpan nilai node
        self.left = None #Child kiri
        self.right = None #Child kanan

def insert (root,data): #Alur fungsi insert :
    #1. Jika root kosong, buat node baru dengan data dan kembalikan node tersebut
    if root is None:
        return Node(data) #2. Jika data lebih kecil dari data pada root, masukkan data ke subtree kiri

    if data < root.data:
        root.left = insert(root.left,data) #3. Jika data lebih besar dari data pada root, masukkan data ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right,data) #4. Jika data sama dengan data pada root, tidak perlu memasukkan (BST tidak boleh memiliki duplikat)
    return root #5. Kembalikan root setelah proses penyisipan selesai

#mengisi data bst
#Awalnya BST kosong, jadi root di set ke None. Kemudian kita memiliki daftar data yang ingin dimasukkan ke dalam BST yaitu [50,30,70,20,40,50,80]. Kita iterasi melalui setiap data dalam daftar tersebut dan memanggil fungsi insert untuk memasukkan data ke dalam BST. Setelah semua data dimasukkan, kita mencetak pesan bahwa data berhasil dimasukkan ke dalam BST.
root = None
data_list = [50,30,70,20,40,50,80] #Data yang akan dimasukkan ke dalam BST

for data in data_list:
    root = insert(root,data) #Memanggil fungsi insert untuk setiap data dalam daftar, memperbarui root setiap kali data baru dimasukkan ke dalam BST

print("Data berhasil dimasukkan ke dalam BST") #Setelah semua data dimasukkan, kita mencetak pesan bahwa data berhasil dimasukkan ke dalam BST.


#==============================
#Latihan 2 :Tranversal Inorder
#==============================

#Alur fungsi inorder :
#1. Jika root tidak kosong, lakukan langkah berikut:
def inorder(root):
    if root is not None:
        inorder(root.left) #2. Kunjungi node saat ini (root) dan tampilkan datanya
        print(root.data, end=" ") #3. Kunjungi subtree kanan dengan memanggil fungsi inorder pada child kanan root
        inorder(root.right) #4. Jika root kosong, kembalikan (tidak melakukan apa-apa)

print("Hasil Inorder : ") #Memanggil fungsi inorder untuk menampilkan isi BST dalam urutan inorder (kiri, root, kanan)
inorder(root) #Outputnya akan menampilkan data dalam urutan yang terurut karena sifat dari traversal inorder pada BST. Jadi hasilnya adalah 20 30 40 50 70 80.

#===========================
#Latiham 3 : Search di BST
#===========================

#Alur fungsi search :
#1. Jika root kosong, kembalikan False (data tidak ditemukan)
#2. Jika data pada root sama dengan key, kembalikan True (data ditemukan)
#3. Jika key lebih kecil dari data pada root, cari di subtree kiri
#4. Jika key lebih besar dari data pada root, cari di subtree kanan

def search(root, key): #Fungsi search digunakan untuk mencari apakah suatu nilai (key) ada dalam BST. Fungsi ini menerima dua parameter yaitu root dari BST dan key yang ingin dicari. Alur fungsi search adalah sebagai berikut:
    if root is None: #1. Jika root kosong, kembalikan False (data tidak ditemukan)
        return False
    
    if root.data == key: #2. Jika data pada root sama dengan key, kembalikan True (data ditemukan)
        return True

    if key < root.data:
        return search(root.left,key) #3. Jika key lebih kecil dari data pada root, cari di subtree kiri dengan memanggil fungsi search pada child kiri root
    else:
        return search(root.right,key) #4. Jika key lebih besar dari data pada root, cari di subtree kanan dengan memanggil fungsi search pada child kanan root
    
#UJI PENCARIAN
key = 40 #Kita ingin mencari apakah nilai 40 ada dalam BST. Kita memanggil fungsi search dengan root dari BST dan key yang ingin dicari yaitu 40. Jika fungsi search mengembalikan True, kita mencetak "data ditemukan". Jika fungsi search mengembalikan False, kita mencetak "Data tidak ditemukan". Dalam kasus ini, karena nilai 40 memang ada dalam BST, maka outputnya akan menampilkan "data ditemukan".
if search(root,key):
    print("data ditemukan") #Jika fungsi search mengembalikan True, kita mencetak "data ditemukan". Jika fungsi search mengembalikan False, kita mencetak "Data tidak ditemukan". Dalam kasus ini, karena nilai 40 memang ada dalam BST, maka outputnya akan menampilkan "data ditemukan".
else:
    print("Data tidak ditemukan") #Jika fungsi search mengembalikan False, kita mencetak "Data tidak ditemukan". Dalam kasus ini, karena nilai 40 memang ada dalam BST, maka outputnya akan menampilkan "data ditemukan".
    