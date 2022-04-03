stack=[]

# pembatas
def pembatas():
    print("="*50)

print("\n")
pembatas()
print("WELCOME TO STACK".center(50," "))
pembatas()
limitStack = int(input("Masukkan Batas Stack : "))

def menu():
    while True:
        print("\n")
        pembatas()
        print("PROGRAM STACK BARANG".center(50," "))
        pembatas()
        print("DAFTAR MENU".center(50," "))
        print("1. Daftar Barang")
        print("2. Push Barang")
        print("3. Pop Barang")
        print("4. Cek Peek Barang")
        print("5. Cek Size Stack")
        print("6. Empty Stack")
        print("7. Full Stack")
        print("8. Tentang Program")
        print("9. Exit")
        pembatas()
        pilihan = input("Pilih menu:").upper()
        if pilihan == '1' :
            daftarBarang()
        elif pilihan == "2" :
            push()
        elif pilihan == "3" :
            pop()
        elif pilihan == "4" :
            peek()
        elif pilihan == "5" :
            size()
        elif pilihan == "6" :
            empty()
        elif pilihan == "7" :
            full()
        elif pilihan == "8" :
            me()
        elif pilihan == "9" :
            pembatas()
            print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI".center(50,"-"))
            pembatas()
            exit()
        else :
            print("Input Salah. Silahkan Masukkan Pilihan Lagi")
            pass

# untuk menampilkan daftar barang
def daftarBarang():
    print("\n")
    pembatas()
    print(" DAFTAR BARANG ".center(50,"-"))
    pembatas()
    if len(stack) == 0 :
        print("Stack Kosong ! Silahkan Push Barang".center(50," "))
        print(f"Batas Stack :{limitStack} ".center(50," "))
    else :
        for i in stack:
            print(i)
    pembatas()    

# untuk menambahkan elemen, dimana elemen paling atas adalah elemen terakhir
def push():
    print("\n")
    pembatas()
    print(" MENU PUSH ".center(50,"-"))
    pembatas()
    if len (stack) == limitStack :
        print("Stack Penuh !".center(50," "))
        pembatas()
    else:
        barang = str(input("Masukkan Nama Barang : "))
        stack.append(barang)
        print(f'Barang ["{barang}"] Berhasil Ditambahkan')
        pembatas()
        daftarBarang()
        lanjut2 = input('''"Lanjut? Tekan y Jika Ingin Melanjutkan Program, 
        atau Tekan n Untuk Kembali ke Menu" : ''').lower()
        if lanjut2 == "y" :
            push()
        elif lanjut2 == "n" :
            print('"Program Kembali ke Menu"')
            menu()   
        else :
            print('"Input Salah. Program Kembali ke Menu"')
            menu()

# untuk menghapus elemen, dimana elemen paling atas adalah elemen terakhir   
def pop():
    print("\n")
    pembatas()
    print(" MENU POP ".center(50,"-"))
    pembatas()
    if len(stack) == 0:
        print("Stack Kosong !".center(50," "))
        pembatas()
    else:
        barang = stack.pop()
        print(f'Barang ["{barang}"] Berhasil Dihapus')
        pembatas()
        daftarBarang()
        lanjut2 = input('''"Lanjut? Tekan y Jika Ingin Melanjutkan Program, 
        atau Tekan n Untuk Kembali ke Menu" : ''').lower()
        if lanjut2 == "y" :
            pop()
        elif lanjut2 == "n" :
            print('"Program Kembali ke Menu"')
            menu()   
        else :
            print('"Input Salah. Program Kembali ke Menu"')
            menu()

# untuk melihat elemen paling atas
def peek():
    print("\n")
    pembatas()
    print(" MENU PEEK".center(50,"-"))
    pembatas()
    if len(stack) == 0:
        print("Stack Kosong !".center(50," "))
    else:
        barang = stack[-1]
        print("Top Barang : ", barang)
    pembatas()
    
# untuk mengecek ukuran stack
def size():
    print("\n")
    pembatas()
    print(" MENU SIZE ".center(50,"-"))
    pembatas()
    print(f'Jumlah Barang : {len(stack)}')
    pembatas()

# untuk mengecek apakah stack kosong
def empty():
    print("\n")
    pembatas()
    print(" MENU EMPTY ".center(50,"-"))
    pembatas()
    if len(stack) == 0:
        print("True. Stack Kosong !".center(50," "))
        pembatas()
    else:
        print("False. Stack Tidak Kosong !".center(50," "))
    pembatas()

# untuk mengecek apakah stack penuh
def full():
    print("\n")
    pembatas()
    print(" MENU FULL ".center(50,"-"))
    if len(stack) == limitStack:
        print("True. Stack Penuh !".center(50," "))
    else:
        print("False. Stack Tidak Penuh !".center(50," "))
    pembatas()

def me():
    print("\n")
    pembatas()
    print(" MENU ABOUT ME ".center(50,"-"))
    pembatas()
    print("\n")
    print("Program ini dibuat oleh :".center(50," "))
    print("\n")
    print("Hendra Usman".center(50," "))
    print("D0221079".center(50," "))
    print("INF F".center(50," "))
    print("TEKNIK INFORMATIKA USB 2021".center(50," "))
    
menu()
