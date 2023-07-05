import create
import read
import update
import delete

def main():
    while True:
        print("Pilih operasi:")
        print("1. Tambah data")
        print("2. Baca data")
        print("3. Perbarui data")
        print("4. Hapus data")
        print("5. Keluar")

        choice = input("Masukkan pilihan (1-5): ")

        if choice == "1":
            nama = input("Masukkan nama siswa: ")
            alamat = input("Masukkan alamat siswa: ")
            create.create_data(nama, alamat)
        elif choice == "2":
            read.read_data()
        elif choice == "3":
            id_siswa = input("Masukkan ID siswa yang ingin diperbarui: ")
            nama = input("Masukkan nama baru: ")
            alamat = input("Masukkan alamat baru: ")
            update.update_data(id_siswa, nama, alamat)
        elif choice == "4":
            id_siswa = input("Masukkan ID siswa yang ingin dihapus: ")
            delete.delete_data(id_siswa)
        elif choice == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1-5.")

if __name__ == "__main__":
    main()
