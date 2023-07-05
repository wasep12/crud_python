import koneksi

def create_data(nama, alamat):
    connection = koneksi.create_connection()
    cursor = connection.cursor()

    sql = "INSERT INTO siswa (nama, alamat) VALUES (%s, %s)"
    values = (nama, alamat)

    try:
        cursor.execute(sql, values)
        connection.commit()
        print("Data berhasil ditambahkan")
    except koneksi.mysql.connector.Error as error:
        print("Gagal menambahkan data: {}".format(error))

    cursor.close()
    koneksi.close_connection(connection)
