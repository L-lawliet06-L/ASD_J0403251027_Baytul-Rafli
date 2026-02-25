#----------------------------------------------#
#Baytul Rafli
#J0403251027
#TPL B1
#----------------------------------------------#

#----------------------------------------------#
# materi rekrusif: call stack
# tracing bilangan (masuk-keluar)
# input 3 
# 3-2-1 | 1-2-3
# masuk 3-2-1
# keluar 1-2-3
# ----------------------------------------------#

def hitung(n):
    #base case
    if n == 0:
        print("Selesai menghitung!")
        return
    print(f"Masuk {n}") #menunjukkan saat masuk fungsi dengan nilai n
    hitung(n-1) #recursive case, memanggil fungsi dengan n-1
    print(f"Keluar{n}") #menunjukkan saat keluar fungsi dengan nilai n

print ("======== Progtam Call Stack ========")    
hitung(3)