from Controller import *

database = [
    {"id": 1, "makanan": "Nasi Goreng", "minuman": "Teh Manis", "harga": 25000, "stock": 10},
    {"id": 2, "makanan": "Mie Ayam", "minuman": "Es Jeruk", "harga": 20000, "stock": 15},
]

print("===== SELAMAT DATANG DI FOOD ORDERING APP =====")
while(True):
    print("="*50)
    print("AKSES APLIKASI")
    try:
        print("1. Admin \n2. Customer \n3. Keluar ")
        akses = int(input("pilih akses anda: "))
        if akses == 1:
            print("="*50)
            print("Signed in as Admin")
            while(True):
                print("===== MENU ADMIN =====")
                try:
                    print("1. Tampilkan Semua Data \n2. Tambah Data \n3. Ubah Data \n4. Hapus Data \n 5.Keluar Menu Admin \n")
                    pilih_admin = int(input("pilih menu: "))
                    if pilih_admin == 1:
                        read_items(database)
                    elif pilih_admin == 2:
                        print("Masukan data yang ingin di tambahkan")
                        makanan = input("Makanan    : ")
                        minuman = input("minuman    : ")
                        harga = input("harga        : ")
                        stock = input("stock        : ")
                        create_item(makanan, minuman, harga, stock, database)
                    else:
                        break 
                except ValueError:
                    print("Program Hanya Memproses inputan angka, silahkan pilih lagi (1 - 4)")
        elif akses == 2:
            print("Masuk as customer")
        elif akses == 3:
            print("TERIMA KASIH SUDAH MENGGUNAKAN FOOD ORDERING APP")
            break
        else:
            print("Masukan pilihan hanya dari 1 - 3")
    except ValueError:
        print("Program Hanya Memproses inputan angka, silahkan pilih lagi (1 - 3)")

        
    