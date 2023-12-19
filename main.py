from Controller import *

database_makanan = [
    {"id": 1, "type" :"makanan", "nama": "Nasi Goreng", "harga": 25000, "stock": 10},
    {"id": 2, "type" :"makanan", "nama": "Mie Ayam",  "harga": 20000, "stock": 15},
]

database_minuman = [
    {"id": 1, "type" :"minuman", "nama": "Teh Manis", "harga": 25000, "stock": 10},
    {"id": 2, "type" :"minuman","nama": "Es Jeruk", "harga": 20000, "stock": 15},
]




print("\n===== SELAMAT DATANG DI FOOD ORDERING APP =====")
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
                print("\n===== MENU ADMIN =====")
                try:
                    print("1. Tampilkan Semua Data \n2. Tambah Data \n3. Ubah Data \n4. Hapus Data \n5. Keluar Menu Admin \n")
                    pilih_admin = int(input("pilih menu: "))
                    if pilih_admin == 1:
                        # print("1. Makanan \n2. Minuman ")
                        # item_type = int(input("Masukkan Jenis Item"))
                        # show_data(database_makanan,database_minuman,item_type)
                        show_data(database_makanan,database_minuman)
                    elif pilih_admin == 2:
                        while True:
                            try:
                                print("PILIH DATA YANG INGIN DI BUAT")
                                print("1. Data Makanan \n2. Data Minuman \n 3. Kembali")
                                pilih_data = int(input("Pilih no (1 - 3): "))
                                if pilih_data == 1:
                                    makanan = input("Makanan    : ")
                                    harga = input("harga        : ")
                                    stock = input("stock        : ")
                                    create_item_makanan(makanan, harga, stock, database_makanan)
                                    print("data berhasil dibuat")
                                elif pilih_data == 2:  
                                    minuman = input("minuman    : ")
                                    harga = input("harga        : ")
                                    stock = input("stock        : ")
                                    create_item_minuman(minuman, harga, stock, database_minuman)
                                    print("data berhasil dibuat")
                                elif pilih_data == 4:
                                    break
                                else:
                                    print("Pilih Nomor 1 - 4")
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
                                    id = int(input("Pilih Id data yang ingin diubah : "))
                                    harga = input("harga        : ")
                                    stock = input("stock        : ")
                                    response = update_item(id, {"harga": harga, "stock": stock}, database_makanan)
                                    print(response)
                                    print("===== DATA SETELAH UPDATE =====")
                                    read_items(database_makanan)
                                elif pilih_update == 2:
                                    read_items(database_minuman)
                                    id = int(input("Pilih Id data yang ingin diubah : "))
                                    harga = input("harga        : ")
                                    stock = input("stock        : ")
                                    response = update_item(id, {"harga": harga, "stock": stock}, database_minuman)
                                    print(response)
                                    print("===== DATA SETELAH UPDATE =====")
                                    read_items(database_minuman)
                                elif pilih_update == 3:
                                    break
                                else:
                                    print("Pilih Nomor 1 - 3") 
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
                                    response = delete_item(id, database_makanan)
                                    print(response)
                                    print("===== DATA SETELAH DI HAPUS =====")
                                    read_items(database_makanan)
                                elif pilih_hapus == 2:
                                    read_items(database_minuman)
                                    id = int(input("Pilih Id data yang ingin di hapus : "))
                                    response = delete_item(id, database_minuman)
                                    print(response)
                                    print("===== DATA SETELAH DI HAPUS =====")
                                    read_items(database_minuman)
                                elif pilih_hapus == 3:
                                    break
                                else:
                                    print("Pilih Nomor 1 - 3") 
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
            print("="*50)
            print("Selamat Datang Customer")
            cart = []
            total = 0
            while True:
                print("\n===== MENU =====")
                try:
                    print("Kerangjang Anda : ")
                    for row in cart:
                        print(row)
                    print("\nAksi : \n1. Beli Item \n2. Hapus Item \n3. Ubah Item \n4. Checkout \n6. Keluar \n")
                    cust_menu = int(input("Pilih Menu (1-6) : "))
                    if cust_menu == 1:
                        print("\nAksi : \n1. Makanan \n2. Minuman \n3. Keluar \n")
                        cust_menu = int(input("Pilih Menu (1-3) : "))
                        if cust_menu == 1: 
                            add_item(database_makanan,database_minuman,cust_menu,cart)
                                
                        elif cust_menu == 2:
                            add_item(database_makanan,database_minuman,cust_menu,cart)
                        elif cust_menu == 3:
                            continue
                        
                    elif cust_menu == 2:
                        pass
                    elif cust_menu == 3:
                        pass
                    elif cust_menu == 4:
                        if len(cart)<1:
                            print("Anda Belum Menambahkan Item")
                            continue
                        for row in cart:
                            total += row['harga']*row['jumlah']
                        print(f"Total Harga = Rp {total},00")
                        print("TERIMA KASIH SUDAH MEMESAN")
                        break
                    elif cust_menu == 5:
                        break
                except ValueError:
                    print("Program Hanya Memproses inputan angka, silahkan pilih lagi (1 - 6)")
        elif akses == 3:
            print("TERIMA KASIH SUDAH MENGGUNAKAN FOOD ORDERING APP")
            break
        else:
            print("Masukan pilihan hanya dari 1 - 3")
    except ValueError:
        print("Program Hanya Memproses inputan angka, silahkan pilih lagi (1 - 3)")

        
    