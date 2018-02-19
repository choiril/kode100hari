from sys import argv
# modul exist berfungsi untuk mengecek apakah file sudah ada atau belu, jika belum aka mengahsilkan FALSE
from os.path import exists

# nama file yang akan dipanggil dan yang akan diisi
script, file1, file2 = argv

print(f"Menyalin isi dari {file1} ke {file2}")

# membuka file awal
file_awal = open(file1)
# membaca isi file
data_awal = file_awal.read()

# menghitung panjang dari string menggunakan len 
print(f"besar file yang akan disalin adalah {len(data_awal)} bytes")

# penggunaaan modul exist
print(f"apakah {file2} sudah tersedia? {exists(file2)}")
print("tekan enter jika ingin melanjutkan proses, dan tekan ctrl+c untuk membatalkan")
input()

# membuka file yang akan diisi
file_dua = open(file2, 'w')
# menulis isi file
file_dua.write(data_awal)

print("Penyalinan isi file telah selesai")

# menutup semua file
file_awal.close()
file_dua.close()