def compare_files(file_path_a, file_path_b):
    try:
        with open(file_path_a, 'r') as file_a, open(file_path_b, 'r') as file_b:
            character_a = file_a.read(1)
            character_b = file_b.read(1)

            while character_a == character_b and character_a != '' and character_b != '':
                character_a = file_a.read(1)
                character_b = file_b.read(1)

            if character_a == character_b:
                print("File identik")
            else:
                print("File berbeda")

    except FileNotFoundError:
        print("Salah satu atau kedua file tidak ditemukan")

# Contoh penggunaan
file_path1 = input("Masukkan path file pertama: ")
file_path2 = input("Masukkan path file kedua: ")

compare_files(file_path1, file_path2)
