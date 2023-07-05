import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_sistemkomputer"
)

cursor = db.cursor()
sql = """CREATE TABLE siswa (
id_siswa INT PRIMARY KEY AUTO_INCREMENT,
    nama VARCHAR(50) NOT NULL,
    alamat VARCHAR(100) NOT NULL
)"""
cursor.execute(sql)
print("Tabel 'siswa' berhasil dibuat")