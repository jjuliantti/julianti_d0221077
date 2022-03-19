#type data list
list = ["juli",78,96.3,True]
#perulangan
for i in (list):
    print (i)
    
#perulangan while loop
i = 0
while i < len(list):
    print(list[i])
    i += 1
    
#mengapdate nilai/value
list [0] = "juni"
print(list)
list [3] = False
print(list)

#menghapus nilai/value
#remove
#del
#pop

#remove
list.remove("juni")
print(list)

#del
del list [2]
print(list)

#pop
list.pop()
print(list)

#menambahkan nilai/value
#append
#extend
#insert

#append
list.append("april")
print(list)

#extend
list.extend([56.2])
print(list)

#insert
list.insert(2, True)
print(list)
