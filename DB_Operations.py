import pymysql
import pymysql.cursors

def connect():
    return pymysql.connect(host="localhost",
                           user="root",
                           password="",
                           database="barang",
                           cursorclass=pymysql.cursors.DictCursor)

def fetch_all_items():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM produk")
            rows = cursor.fetchall()
        return rows
    finally:
        connection.close()

def insert_item(nama, harga, ketersediaan):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO produk (nama, harga, ketersediaan) VALUES (%s, %s, %s)", 
                           (nama, harga, ketersediaan))
            connection.commit()
            return 1
    finally:
        connection.close()

def fetch_item_by_id(id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM produk WHERE id = %s", (id,))
            item = cursor.fetchone()
        return item
    finally:
        connection.close()

def update_item(id, nama, harga, ketersediaan):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE produk
                SET nama = %s, harga = %s, ketersediaan = %s
                WHERE id = %s
            """, (nama, harga, ketersediaan, id))
            connection.commit()
    finally:
        connection.close()

def delete_item(item_id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM produk WHERE id = %s", (item_id,))
            connection.commit()
            return 1
    finally:
        connection.close()
