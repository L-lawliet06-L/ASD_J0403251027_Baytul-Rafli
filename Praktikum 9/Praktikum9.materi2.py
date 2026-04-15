#=============================================
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1
# Latihan 2 : Membuat Binary Search Tree
#=============================================

# Membuat Node 

#CLass node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #Child kiri
        self.right = None #Child kanan

#membuat Root
root = Node("A")

#Membuat child level 1

root.left = Node("B")
root.right= Node("C")

#membuat child level 2

root.left.left = Node("D")
root.left.right = Node("E")

#menampilkan isi node
print("Data pada root", root.data)
print("Child kiri root", root.left.data)
print("Child kanan root", root.right.data)
print("Child kiri dari B : ", root.left.left.data)
print("Child kanan dari B : ", root.left.right.data)

#lanjutan 
root.right.right = Node("F")
print("Child kanan dari C : ", root.right.right.data)

#Pembahasan : Pada Latihan 2 ini kamu sudah membangun sebuah binary search tree sederhana dengan class Node. Root utama bernilai "A", lalu memiliki dua child di level pertama yaitu "B" di kiri dan "C" di kanan. Node "B" memiliki dua child di level kedua yaitu "D" dan "E", sedangkan node "C" memiliki child kanan "F". Program kemudian menampilkan isi root, anak kiri, anak kanan, serta anak-anak dari node "B" dan node "C".