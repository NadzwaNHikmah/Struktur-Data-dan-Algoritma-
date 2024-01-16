def baca_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            maks = 80
            buff = file.readline(maks)

            while buff:
                print(buff.strip())  # Output tanpa newline tambahan
                buff = file.readline(maks)

    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan")
    except IOError:
        print(f"Gagal membuka atau membaca file '{nama_file}'")

# Contoh penggunaan
nama_file = input("Masukkan nama file: ")
baca_file(nama_file)
