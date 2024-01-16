def tambah_data_ke_file(nama_file, data):
    try:
        with open(nama_file, 'a') as file:
            file.write(data + "\n")
            print("Penulisan selesai...")
    except IOError:
        print("Gagal membuka atau menulis ke file")

# Contoh penggunaan
nama_file = input("Masukkan nama file: ")
data = input("Masukkan data yang akan ditambahkan: ")

tambah_data_ke_file(nama_file, data)
