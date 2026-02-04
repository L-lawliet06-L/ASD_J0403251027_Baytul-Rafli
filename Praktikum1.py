#-----------------------------------
# Praktikum 1 : konsep ADT dan file handling
# Latihan Dasar 1 : Membaca seluruh file 
#-----------------------------------

#membuka file dengan mode read ("r")

#membuka file dalam satu string
with open("mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()#membaca keseluruhan isi dalam satu string
print(isi_file)

print("===Hasil Read===")
print("Tipe data:", type(isi_file))
print("jumlah karakter", len(isi_file))
print("jumlah baris", isi_file.count("\n")+1)

#membuka file per baris
print("===membaca per file===")
jumlah_baris= 0
with open("mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()#menghilangkan garis baru \n
        print("baris ke-", jumlah_baris)
        print("isinya:", baris)


#-----------------------------------
# Praktikum 1 : konsep ADT dan file handling
# Latihan Dasar 2 : parsing baris menjadi kolom
#-----------------------------------
with open("mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")#ketika ada koma "," akan di ambil
        print("NIM :", nim, "| Nama :", nama, "|Nilai", nilai)

#-----------------------------------
# Praktikum 1 : konsep ADT dan file handling
# Latihan Dasar 3 : membaca file dengan menyimpan ke list
#-----------------------------------

data_list = [] # list untuk menampung data mahasiswa
with open("mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        nim, nama, nilai = baris.split(",")
        #simpan sebagai list "[nim,nama.nilai]"
        data_list.append([nim,nama,int(nilai)])

print("==== Data Mahasiswa dalam LIST====")
print (data_list)

print("==== jumlah reecord dalam LIST====")
print ("jumlah record", len(data_list))

print("==== menampilkan data reecord tertentu====")
print("contoh record pertama: ", data_list[0])#array mulai dari 0

#-----------------------------------
# Praktikum 1 : konsep ADT dan file handling
# Latihan Dasar 4 : membaca file dengan menyimpan ke dictionary
#-----------------------------------

data_dict = {} # baut variabel untuk dictionary
with open("mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        nim, nama, nilai = baris.split(",")
        
        #simpan unuk data mahasisw ke dictionary dengan key NIM
        data_dict[nim] = {            #Key
            "nama": nama,             #Values
            "nila": int(nilai)        #values
        }
print("=== data mahasiwa dalam dictionary")
print(data_dict)

