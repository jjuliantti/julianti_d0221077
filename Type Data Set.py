#Type Data Set
#{}
#bersifat immutable/tidak dapat diubah
#tidak dapat diakses menggunakan indeks
#random/teracak
#nilai/valuenya tidak boleh sama
set = {"bintang",10,155.2,False}

#perullangan
for i in (set):
    print(i)

#mengupdate nilai/value
#set = {"langit"}
#print(set[0])

#menghapus nilai/value
#remove
#discard
#clear

#remove
set.remove ("bintang")
print(set)

#discard
set.discard (False)
print(set)

#clear
set.clear ()
print(set)

#menambahkan nilai/value
#add
#update

#add
set.add("awan")
print(set)

#update
set.update([True],[27])
print(set)
