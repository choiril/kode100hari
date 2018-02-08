# membuat variabel sementara menggunakan tanda {}
variabel = "{} {} {} {}"
# jika mengggunakan tanda () maka saat di primt hanya akan menampilkan () buka nilai pengganti dari variabel
variabel2 = "() () () ()"

# mengganti nilai varibel awal dengan nilai baru
print(variabel.format(1, 2, 3, 4))
print(variabel.format("satu", "dua", "tiga", "empat"))
# meski nilainya false ataupun true akan menampilkan nilai yang sama
print(variabel.format(True, False, False, True))
# akan memanggil atau mencetak nilai awal/sebenarnya
print(variabel.format(variabel, variabel, variabel, variabel))
# tanda koma (,) akan memberikan keluaran berupa spasi
print(variabel.format(
"Ini teks pertama",
"Dan masih lanjut ke-dua",
"Ketiga juga tercetak",
"Ini akhir",
#ini tidak bisa dicetak jika pada nilai variabel awal masih 4
"Tidak bisa dicetak"
))

# jika menggunakan tanda ()
print(variabel2.format("tes", "satu", "dua"))
print(variabel2.format(5, 6, 7, 8))