#=============================================
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1
# Latihan  5 : Membuaat traversal postorder
#=============================================

# Membuat Node 

#CLass node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #Child kiri
        self.right = None #Child kanan

#membuat fungsi traversal postorder : left ==> right ==> root
def postorder (node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


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
postorder(root)

#menampilak traversal preorder
print("Hasil Traversal Preorder: ")
postorder(root)

#lanjutan 
root.right.right = Node("F")
print("Child kanan dari C : ", root.right.right.data)

#pembahsan : Traversal postorder mengunjungi node dalam urutan Left, Right, Root. Pada contoh ini, traversal postorder akan mengunjungi child kiri dari root yaitu "B" terlebih dahulu, kemudian ke child kiri dari "B" yaitu "D", kembali ke "B" untuk mengunjungi child kanannya "E", kembali ke root untuk mengunjungi child kanan yaitu "C", dan terakhir ke root untuk mengunjungi dirinya sendiri yaitu "A". Sehingga hasilnya adalah D E B C A.
