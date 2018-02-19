#membuat nama variabel dan nilai
#mobil adalah nama variable dan 100 adalah nilai dari mobil
mobil = 100
#jika nilai tempat duduk diisi 4 bukan 4.0 maka jumlah penumpang akan menghasilkan nilai flloating atau desimal
tempat_duduk = 4.0
sopir = 30
penumpang = 90
#penggunaan operator matematika antar variabel
#jika nilai variabel adalh angka maka bisa kita gunakan operator matematika
mobil_yang_tidak_digunakan = mobil - sopir
mobil_yang_digunakan = sopir
jumlah_penumpang = mobil_yang_digunakan * tempat_duduk
rata_rata_penumpang = penumpang / mobil_yang_digunakan

#memanggil nilai variable
#untuk memanggil nilai variabel cukup dengan menuliskan dari nama variablenya 
print("Terdapat", mobil, "buah mobil hari ini.")
print("Ada ", sopir, " yang akan mengendarai.")
print("Jadi ada ", mobil_yang_tidak_digunakan, "buah hari ini.")
print("Hari ini hanya dapat mengantarkan ", jumlah_penumpang, " penumpang.")
print("Dan saat ini ada ", penumpang, " orang yang akan diantarkan.")
print("Rata-rata terdapat ", rata_rata_penumpang,
" penumpang setiap mobil.")