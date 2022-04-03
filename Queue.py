Queue = []

# pembatas
def pembatas():
    print("="*50)

print("\n")
pembatas()
print("WELCOME TO QUEUE".center(50," "))
pembatas()
limitQueue = int(input("Masukkan Batas Antrian : "))

def menu():
    while True:
        print("\n")
        pembatas()
        print("PROGRAM ANTRIAN (QUEUE)".center(50," "))
        pembatas()
        print("--- DAFTAR MENU ---".center(50," "))
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Full")
        print("4. Size")
        print("5. View")
        print("6. Exit")
        pembatas()
        pilihan = input("Pilih menu:").upper()
        if pilihan == '1' :
            enqueue()
        elif pilihan == "2" :
            dequeue()
        elif pilihan == "3" :
            full()
        elif pilihan == "4" :
            size()
        elif pilihan == "5" :
            view()
        elif pilihan == "6" :
            pembatas()
            print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI".center(50,"-"))
            pembatas()
            exit()
        else :
            print("Input Salah. Silahkan Masukkan Pilihan Lagi")
            pass

def view():
    print("\n")
    pembatas()
    print(" MENU VIEW ".center(50,"-"))
    pembatas()
    if len(Queue) == 0 :
        print(f"Batas Antrian :{limitQueue}")
        print("--- Antrian Kosong ! ---".center(50," "))
    else:
        print(f"Batas Antrian :{limitQueue}".center(50," "))
        for i in Queue:
            print(i)
    pembatas()
    
def enqueue():
    print("\n")
    pembatas()
    print(" MENU ENQUEUE ".center(50,"-"))
    pembatas()
    if len(Queue) == limitQueue :
        print("--- Antrian Penuh ! ---".center(50," "))
        pembatas()
    else:
        data=input("Masukkan Data : ")
        Queue.append(data)
        print(f'{data} telah ditambahkan ke antrian')
        pembatas()
        view()
        lanjut = input("Enqueue lagi ? (y/n) : ").lower()
        if lanjut == 'y':
            enqueue()
        elif lanjut == 'n':
            menu()
        else:
            print("Input Salah. Silahkan Masukkan Pilihan Lagi")
            pass    

def dequeue():
    print("\n")
    pembatas()
    print(" MENU DEQUEUE ".center(50,"-"))
    pembatas()
    if len(Queue) == 0 :
        print("--- Antrian Kosong ! ---".center(50," "))
        pembatas()
    else:
        print(f"{Queue[0]} telah Keluar dari Antrian")
        del Queue[0]
        pembatas()
        view()
        lanjut = input("Dequeue lagi ? (y/n) : ").lower()
        if lanjut == 'y':
            dequeue()
        elif lanjut == 'n':
            menu()
        else:
            print("Input Salah. Silahkan Masukkan Pilihan Lagi")
            pass

def full():
    print("\n")
    pembatas()
    print(" MENU FULL ".center(50,"-"))
    pembatas()
    if len(Queue) == limitQueue :
        print("--- Antrian Penuh ! ---".center(50," "))
        pembatas()
    else:
        print("--- Antrian Belum Penuh ! ---".center(50," "))
        pembatas()
    
def size():
    print("\n")
    pembatas()
    print(" MENU SIZE ".center(50,"-"))
    pembatas()
    print(f"Batas Antrian :{limitQueue}")
    print(f"Jumlah Dalam Antrian : {len(Queue)}")
    pembatas()
