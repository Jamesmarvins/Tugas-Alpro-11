nama_file = input("Masukkan nama file: ")

try:
    with open(nama_file, 'r') as file:
        distribusi_jam = {}

        for baris in file:
            if baris.startswith('From '):
                kata = baris.split()
                waktu = kata[5].split(':')
                jam = waktu[0]
                distribusi_jam[jam] = distribusi_jam.get(jam, 0) + 1

        for jam, jumlah in sorted(distribusi_jam.items()):
            print(jam, jumlah)

except FileNotFoundError:
    print("File tidak ditemukan.")
except Exception as e:
    print("Terjadi kesalahan:", e)