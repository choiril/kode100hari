#variable dan nilai
nama = 'Choiril'
umur = 23
berat = 50 #kilogram
tinggi = 162 #centimeter
mata = 'hitam'
rambut = 'hitam'
kulit = 'sawo matang'

#penggunaan format string
print(f"Nama saya {nama}.")
print(f"Tinggi badan {tinggi}.")
print(f"Berat badan {berat}.")
print(f"Umur sekarang adalah {umur} tahun.")

#pengguanaan operator matematika dan format string
total = umur + berat + tinggi
print(f"Ketika umur, berat badan dan tinggi badan dijumlahkan akan menghasilkan {total}.")
#konversi ukuran
#disini akan merubah berat badan ke gram dan tinggi badan ke meter
konversi_berat = berat * 1000
konversi_tinggi = tinggi / 100
#penggunaan format string sesuai studi drill
print(f"Berat badan jika dikonversi ke gram adalah {konversi_berat} gram.")
print(f"Tinggi badan jika dikonversi ke meter adalah {konversi_tinggi} meter")