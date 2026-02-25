#----------------------------------------------#
#Baytul Rafli
#J0403251027
#TPL B1
#----------------------------------------------#

#----------------------------------------------#
# materi rekrusif: faktorial
# recrusive case => 3! = 3 * 2* 1
# base case => 0 berhenti
#----------------------------------------------#

def faktorial(n):
    if n == 0: #base case
        return 1
    else:
        return n * faktorial(n-1) #recursive case

print ("======== Progtam Faktorial ========")    
print ("Hasil faktorial : ", faktorial(3))
