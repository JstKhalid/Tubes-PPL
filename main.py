from Controller import *

database_makanan = [
    {"id": 1, "makanan": "Nasi Goreng", "harga": 25000, "stock": 10},
    {"id": 2, "makanan": "Mie Ayam",  "harga": 20000, "stock": 15},
]

database_minuman = [
    {"id": 1, "minuman": "Teh Manis", "harga": 25000, "stock": 10},
    {"id": 2, "minuman": "Es Jeruk", "harga": 20000, "stock": 15},
]


print("===== SELAMAT DATANG DI FOOD ORDERING APP =====")
while True:
    print("="*50)
    print("AKSES APLIKASI")
    try:
        print("1. Admin \n2. Customer \n3. Keluar \n")
        akses = int(input("pilih akses anda: "))
        if akses == 1:
            print("="*50)
            print("Signed in as Admin")
            while True:
                print("===== MENU ADMIN =====")
                try:
                    print("1. Tampilkan Semua Data \n2. Tambah Data \n3. Ubah Data \n4. Hapus Data \n 5.Keluar Menu Admin \n")
                    pilih_admin = int(input("pilih menu: "))
                    if pilih_admin == 1:
                        print("===== DATA MAKANAN =====")
                        read_items(database_makanan)
                        print("===== DATA MINUMAN =====")
                        read_items(database_minuman)
                    elif pilih_admin == 2:
                        while True:
                            try:
                                print("PILIH DATA YANG INGIN DI BUAT")
                                print("1. Data Makanan \n2. Data Minuman \n3. kembali")
                                pilih_data = int(input("Pilih no (1 - 3): "))
                                if pilih_data == 1:
                                    makanan = input("Makanan    : ")
                                    harga = input("harga        : ")
                                    stock = input("stock        : ")
                                    create_item(makanan, harga, stock, database_makanan)
                                elif pilih_data == 2:  
                                    minuman = input("minuman    : ")
                                    harga = input("harga        : ")
                                    stock = input("stock        : ")
                                    create_item(minuman, harga, stock, database_minuman)
                                elif pilih_data == 3:
                                    break
                                else:
                                    print("Pilih Database dengan nomor 1 - 3")
                                    False
                            except ValueError:
                                print("Program Hanya Memproses inputan angka, silahkan pilih lagi (1 - 4)")
                    elif pilih_admin == 3:
                        while True:
                            try:
                                print("PILIH DATA YANG INGIN DI UBAH")
                                print("1. Data Makanan \n2. Data Minuman \n3. kembali")
                                pilih_update = int(input("Pilih no (1 - 3): "))
                                if pilih_update == 1:     
                                    read_items(database_makanan)
                                    id = int(input("Pilih Id data yang ingin diubah"))
                                    minuman = input("minuman    : ")
                                    harga = input("harga        : ")
                                    stock = input("stock        : ")
                                    update_item(id, {"harga": harga, "stock": stock}, database_makanan)
                                    print("===== DATA SETELAH UPDATE =====")
                                    read_items(database_makanan)
                                elif pilih_update == 2:
                                    read_items(database_minuman)
                                    id = int(input("Pilih Id data yang ingin diubah"))
                                    minuman = input("minuman    : ")
                                    harga = input("harga        : ")
                                    stock = input("stock        : ")
                                    update_item(id, {"harga": harga, "stock": stock}, database_minuman)
                                    print("===== DATA SETELAH UPDATE =====")
                                    read_items(database_minuman)
                                elif pilih_update == 3:
                                    break
                                else:
                                    print("Pilih Database dengan nomor 1 - 3") 
                                    False
                            except ValueError:
                                print("Program Hanya Memproses inputan angka, silahkan pilih lagi (1 - 4)")
                    elif pilih_admin == 4:
                        while True:
                            try:
                                print("PILIH DATA YANG INGIN DI HAPUS")
                                print("1. Data Makanan \n2. Data Minuman \n3. kembali")
                                pilih_hapus = int(input("Pilih no (1 - 3): "))
                                if pilih_hapus == 1:
                                    read_items(database_makanan)
                                    id = int(input("Pilih Id data yang ingin di hapus : "))
                                    delete_item(id, database_makanan)
                                    print("===== DATA SETELAH DI HAPUS =====")
                                    read_items(database_makanan)
                                elif pilih_hapus == 2:
                                    read_items(database_minuman)
                                    id = int(input("Pilih Id data yang ingin di hapus : "))
                                    delete_item(id, database_minuman)
                                    print("===== DATA SETELAH DI HAPUS =====")
                                    read_items(database_minuman)
                                elif pilih_hapus == 3:
                                    break
                                else:
                                    print("Pilih Database dengan nomor 1 - 3") 
                                    False
                            except ValueError:
                                print("Program Hanya Memproses inputan angka, silahkan pilih lagi (1 - 4)")
                    elif pilih_admin == 5:
                        break 
                    else:
                        print("Masukan pilihan hanya dari 1 - 4")
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

        
    