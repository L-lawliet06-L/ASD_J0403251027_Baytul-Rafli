#=============================================
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1
# Latihan   6: Struktur Organisasi perusahaan
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

#membuat tree struktur orgaisasi
root= Node("Direktur")

#child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.right = Node("Staff 3")

#menampilak traversal preorder
print("Struktur Organisasi (Preorder): ")
preorder(root)

#Pembahasan : Pada Latihan 6 ini kamu sudah membangun sebuah struktur organisasi perusahaan dengan class Node. Root utama bernilai "Direktur", lalu memiliki dua child di level pertama yaitu "Manajer A" di kiri dan "Manajer B" di kanan. Node "Manajer A" memiliki dua child di level kedua yaitu "Staff 1" dan "Staff 2", sedangkan node "Manajer B" memiliki child kanan "Staff 3". Program kemudian menampilkan struktur organisasi menggunakan traversal preorder, yang mengunjungi node dalam urutan Root, Left, Right. Sehingga hasilnya adalah Direktur Manajer A Staff 1 Staff 2 Manajer B Staff 3.