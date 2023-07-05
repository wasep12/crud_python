import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_sistemkomputer"
        )
        print("Koneksi ke database berhasil")
        return connection
    except mysql.connector.Error as error:
        print("Koneksi ke database gagal: {}".format(error))

def close_connection(connection):
    connection.close()
    print("Koneksi ke database ditutup")
