def tampilkan_isi_file(nama_file, baris_per_iterasi=10):
    try:
        with open(nama_file, 'r') as file:
            lines = file.readlines()
            total_baris = len(lines)
            index = 0

            while index < total_baris:
                for i in range(index, min(index + baris_per_iterasi, total_baris)):
                    print(lines[i].strip())

                index += baris_per_iterasi

                pilihan = input("Pilih perintah (Q untuk keluar, R untuk melanjutkan): ").upper()
                if pilihan == 'Q':
                    break
                elif pilihan != 'R':
                    print("Perintah tidak valid. Program berhenti.")
                    break

    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan:", str(e))

def main():
    nama_file = input("Masukkan nama file: ")
    tampilkan_isi_file(nama_file)

if __name__ == "__main__":
    main()
