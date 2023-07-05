import koneksi

def update_data(id_siswa, nama, alamat):
    connection = koneksi.create_connection()
    cursor = connection.cursor()

    sql = "UPDATE siswa SET nama = %s, alamat = %s WHERE id_siswa = %s"
    values = (nama, alamat, id_siswa)

    try:
        cursor.execute(sql, values)
        connection.commit()
        print("Data berhasil diperbarui")
    except koneksi.mysql.connector.Error as error:
        print("Gagal memperbarui data: {}".format(error))

    cursor.close()
    koneksi.close_connection(connection)
