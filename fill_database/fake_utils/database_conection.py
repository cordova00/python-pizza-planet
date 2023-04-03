def insert_order(cursor, order, total_price):
    cursor.execute("""
        INSERT INTO `order` (`client_name`, `client_dni`, `client_address`, `client_phone`, `date`, `total_price`, `size_id`)
        VALUES (?, ?, ?, ?, ?, ?, ?)
     """, (order['client_name'], order['client_dni'], order['client_address'],
                 order['client_phone'], order['date'], total_price, order['size_id']['_id']))

def insert_size(cursor, size):
    # Primero, se verifica si el valor '_id' ya existe en la tabla
    cursor.execute("SELECT _id FROM size WHERE _id = ?", (size[0],))
    result = cursor.fetchone()
    if result:
        # Si el valor ya existe, se imprime un mensaje de error y no se realiza la inserción
        print(f"Error: El valor '{size[0]}' ya existe en la tabla size.")
    else:
        # Si el valor no existe, se realiza la inserción
        cursor.execute('''
            INSERT INTO size (_id, name, price)
            VALUES (?, ?, ?)
        ''', size)

def insert_ingredient(cursor, ingredient):
    cursor.execute('''
        SELECT COUNT(*) FROM ingredient WHERE _id=?
    ''', (ingredient[0],))
    count = cursor.fetchone()
    if count:
        print(f"El ingrediente con id {ingredient[0]} ya existe en la tabla.")
    else:
        cursor.execute('''
            INSERT INTO ingredient (_id, name, price)
            VALUES (?, ?, ?)
        ''', ingredient)
        print(f"El ingrediente con id {ingredient[0]} ha sido insertado exitosamente.")


def insert_beverage(cursor, beverage):
    cursor.execute('''
        SELECT COUNT(*) FROM beverage WHERE _id=?
    ''', (beverage[0],))
    count = cursor.fetchone()
    if count:
        print(f"La bebida con id {beverage[0]} ya existe en la tabla.")
    else:
        cursor.execute('''
            INSERT INTO beverage (_id, name, price, size)
            VALUES (?, ?, ?, ?)
        ''', beverage)
        print(f"La bebida con id {beverage[0]} ha sido insertada exitosamente.")