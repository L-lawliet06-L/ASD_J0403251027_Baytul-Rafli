#----------------------------------------------#
#Baytul Rafli
#J0403251027
#TPL B1
#----------------------------------------------#

#----------------------------------------------#
# materi rekrusif: menjumlahkan elemen list
#---------------------------#

def jumlah_list(data,index=0):
    #base case
    if index == len(data):
        return 0
    


    #recrusive case
    return data[index] + jumlah_list(data, index+1)

print ("======== Progtam Jumlah List ========")
print ("Hasil jumlah list : ", jumlah_list([2,4,5]))

