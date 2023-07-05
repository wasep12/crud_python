import koneksi

def delete_data(id_siswa):
    connection = koneksi.create_connection()
    cursor = connection.cursor()

    sql = "DELETE FROM siswa WHERE id_siswa = %s"
    values = (id_siswa,)

    try:
        cursor.execute(sql, values)
        connection.commit()
        print("Data berhasil dihapus")
    except koneksi.mysql.connector.Error as error:
        print("Gagal menghapus data: {}".format(error))

    cursor.close()
    koneksi.close_connection(connection)
