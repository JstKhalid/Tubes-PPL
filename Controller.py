#FUNCTION CRUD ADMIN
def create_item(makanan, minuman, harga, stock, database):
    new_id = max(item['id'] for item in database) + 1 if database else 1
    new_item = {"id": new_id, "makanan": makanan, "minuman": minuman, "harga": harga, "stock": stock}
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

