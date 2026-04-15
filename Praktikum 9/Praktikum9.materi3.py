#=============================================
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1
# Latihan 3 : Membuaat traversal preorder
#=============================================

# Membuat Node 

#CLass node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #Child kiri
        self.right = None #Child kanan

#Fungsi preorder : Root ==>left ===>right
def preorder (node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

#membuat Root
root = Node("A")

#Membuat child level 1

root.left = Node("B")
root.right= Node("C")

#membuat child level 2

root.left.left = Node("D")
root.left.right = Node("E")

#menampilak traversal preorder
print("Hasil Traversal Preorder: ")
preorder(root)

#lanjutan 
root.right.right = Node("F")
print("Child kanan dari C : ", root.right.right.data)

#penjelasan : Traversal preorder mengunjungi node dalam urutan Root, Left, Right. Pada contoh ini, traversal preorder akan mengunjungi node "A" terlebih dahulu (root), kemudian ke child kiri "B", lalu ke child kiri dari "B" yaitu "D", kembali ke "B" untuk mengunjungi child kanannya "E", dan terakhir ke child kanan dari root yaitu "C". Sehingga hasilnya adalah A B D E C.