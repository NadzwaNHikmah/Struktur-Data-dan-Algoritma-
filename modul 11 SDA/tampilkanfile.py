def tampilkan_isi_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            isi_file = file.read()
            print("Isi file {}:\n{}".format(nama_file, isi_file))
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan:", str(e))

def main():
    nama_file = input("Masukkan nama file: ")
    tampilkan_isi_file(nama_file)

if __name__ == "__main__":
    main()
