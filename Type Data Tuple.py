#Type Data Tuple
#()
#Immutable
tuple = ("hijau",83,5.97,False)

#perulangan
for i in (tuple):
    print (i)

#perulangan while loop
while i < len(tuple):
    print (tuple[i])
    i += 1

#mengupdate nilai/value
#konversi tuple ke list
tupl = list(tuple)
tupl[1] = 27
print (tupl)

#menghapus nilai/value
#remove
#pop

#remove
tupl.remove("hijau")
print(tupl)

#pop
tupl.pop()
print(tupl)

#menambahkan nilai/value
#append
#extend
#insert

#append
tupl.append (True)
print(tupl)

#extend
tupl.extend (["merah"])
print(tupl)

#insert
tupl.insert (1, 3.7)
print(tupl)
