#=============================================
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1
# Latihan 4 : Membuaat traversal inorder
#=============================================

# Membuat Node 

#CLass node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #Child kiri
        self.right = None #Child kanan

#membuat fungsi inorder : left ==> root==> right
def inorder (node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


#membuat Tree
root = Node("A")

#Membuat child level 1

root.left = Node("B")
root.right= Node("C")

#membuat child level 2

root.left.left = Node("D")
root.left.right = Node("E")

#menampilak traversal preorder
print("Hasil Traversal inorder: ")
inorder(root)

#lanjutan 
root.right.right = Node("F")
print("Child kanan dari C : ", root.right.right.data)

#penjelasan : Traversal inorder mengunjungi node dalam urutan Left, Root, Right. Pada contoh ini, traversal inorder akan mengunjungi child kiri dari root yaitu "B" terlebih dahulu, kemudian ke child kiri dari "B" yaitu "D", kembali ke "B" untuk mengunjungi dirinya sendiri, lalu ke child kanan dari "B" yaitu "E", kembali ke root untuk mengunjungi dirinya sendiri yaitu "A", dan terakhir ke child kanan dari root yaitu "C". Sehingga hasilnya adalah D B E A C.
