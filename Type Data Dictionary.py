#Type Data Dictionary
#{}
#anordered/tidak berurut
#Changeable/bisa berubah-ubah
#unique/tidak dapat menerima 2 key yang sama
dictionary = {"makanan":"roti","minuman":"susu"}

#perulangan
for key in (dictionary):
    print(key, dictionary[key])

#mengupdate nilai
dictionary ["makanan"] = "kue"
print(dictionary)

#menghapus nilai
#pop
dictionary.pop("minuman")
print(dictionary)

#menambahkan nilai
dictionary ["buah"] = "apel"
print(dictionary)
