#menambah list
#menghapus list
#mengedit list
#mencari list beserta indeksnya
#menampilkan indeks

barang = []

perintah = 0

while perintah != 7:
    print(''' 1. menambah
2. menghapus
3. mengedit
4. menampilkan
5. cari barang
6. cari indeks
7. keluar''')
    perintah = int(input("masukkan perintah: "))

    if perintah == 1:
        elemen = input("masukkan barang: ")
        barang.append(elemen)

    elif perintah == 2:
        hapus = int(input("masukkan indeks yang akan dihapus: "))
        barang.pop(hapus)

    elif perintah == 3:
        edit = int(input("masukkan indeks yang akan di edit: "))
        barang[edit] = input("masukkan barang yang baru: ")

    elif perintah == 4:
        for i in range(len(barang)):
            print(barang[i])

    elif perintah == 5:
        cari = input("masukkan barang dicek: ")

        for i in range(len(barang)):
            if barang [i]== cari:
                print("barang ada dalam list")
            else:
                print("barang tidak ditemukan")

    elif perintah == 6:
        cari2 = input("masukkan barang yang dicari: ")
        
        print(barang.index(cari2))

print(barang)
