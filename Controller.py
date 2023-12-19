#FUNCTION CRUD ADMIN
def create_item_makanan( makanan, harga, stock, database):
    new_id = max(item['id'] for item in database) + 1 if database else 1
    new_item = {"id": new_id, "type":"makanan","nama": makanan, "harga": harga, "stock": stock}
    database.append(new_item)

def create_item_minuman( minuman, harga, stock, database):
    new_id = max(item['id'] for item in database) + 1 if database else 1
    new_item = {"id": new_id,"type":"minumam","nama": minuman, "harga": harga, "stock": stock}
    database.append(new_item)

  
def read_items(database):
    for item in database:
        print(item)
  
def update_item(item_id, new_data, database):
    for item in database:
        if item['id'] == item_id:
            item.update(new_data)
            return "Item updated successfully"
    
    return "Item not found"

def delete_item(item_id, database):
    for i, item in enumerate(database):
        if item['id'] == item_id:
            del database[i]
            return "Item deleted successfully"
    return "Item not found"

def show_data(db_makanan, db_minuman,item_type=0):

    if item_type == 1:
        print("\n===== MAKANAN =====")
        for row in db_makanan:
            print(f"{row['id']}. {row['nama']} | Harga : Rp {row['harga']},00 | Stok : {row['stock']}")
    elif item_type == 2:
        print(" \n===== MINUMAN =====")
        for row in db_minuman:
            print(f"{row['id']}. {row['nama']} | Harga : Rp {row['harga']},00 | Stok : {row['stock']}")
    elif item_type == 0:
        print("\n===== MAKANAN =====")
        for row in db_makanan:
            print(f"{row['id']}. {row['nama']} | Harga : Rp {row['harga']},00 | Stok : {row['stock']}")
        print(" \n===== MINUMAN =====")
        for row in db_minuman:
            print(f"{row['id']}. {row['nama']} | Harga : Rp {row['harga']},00 | Stok : {row['stock']}")

def add_item (db_makanan, db_minuman,item_type,cart):
        try:
            show_data(db_makanan,db_minuman,item_type)

            if item_type == 1:
                type = "makanan"
                database = db_makanan
            elif item_type == 2:
                type = "minuman"
                database = db_minuman
            item_no = int(input(f"Pilih {type} (Nomor):"))
            selected_item = [item for item in database if item['id'] == item_no][0]
            item_id =  selected_item['id'] 

            item_name = selected_item['nama']
            item_price = selected_item['harga']
            item_stock = selected_item['stock']
            jumlah_item = int(input("Masukkan Jumlah : "))
            if jumlah_item > item_stock :
                print("\nGagal Menambahkan (Stok Habis)")
            cart_item = {"item_no":item_id,"type":type,"nama":item_name,"harga":item_price,"jumlah":jumlah_item}
            cart.append(cart_item)
        except IndexError:
            print("\nItem Tidak Terdaftar")  
