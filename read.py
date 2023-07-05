import koneksi

def read_data():
    connection = koneksi.create_connection()
    cursor = connection.cursor()

    sql = "SELECT * FROM siswa"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print("Daftar siswa:")
        for row in results:
            print("ID: {}, Nama: {}, Alamat: {}".format(row[0], row[1], row[2]))
    except koneksi.mysql.connector.Error as error:
        print("Gagal membaca data: {}".format(error))

    cursor.close()
    koneksi.close_connection(connection)
