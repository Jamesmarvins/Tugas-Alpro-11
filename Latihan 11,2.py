data_diri = ('Matahari Bhakti Nendya', '22064091', 'Bantul, DI Yogyakarta')
nama, nim, alamat = data_diri

print("Data:", data_diri)
print("NIM :", nim)
print("NAMA :", nama)
print("ALAMAT :", alamat)

nim_tuple = tuple(nim)
nama_depan_tuple = tuple(nama.split()[0])
nama_terbalik_tuple = tuple(reversed(nama.split()))

print("NIM:", nim_tuple)
print("NAMA DEPAN:", nama_depan_tuple)
print("NAMA TERBALIK:", nama_terbalik_tuple)