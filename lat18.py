# belajar membuat fungsi pada Python

# membuat fungsi1 yang berisikan argeumen "kata", def kepanjangan dari define. yang artinya menentukan sebuah fungsi
# setiap pembuatan fungsi diakhiri dengan :, setelah : kode selanjutnya akan menjorok kedalam
# fungsi1 adalah nama sebuah fungsi
def fungsi1(*kata):
# ini adalah isi dari fungsi
	kata1, kata2 = kata
	print(f"Kata pertama: {kata1}, kata kedua: {kata2}")

# membuat fungsi1_lagi yang mana pada fungsi ini argumen lebih dibuat simpel
def fungsi1_lagi(kata1, kata2):
# ini adalah isi dari fungsi
	print(f"Kata pertama: {kata1}, kata kedua: {kata2}")

# membuat fungsi2 dengan satu argumen
def fungsi2(kata1):
# ini adalah isi dari fungsi
	print(f"kata pertama: {kata1}")

# membuat fungsi3 tanpa argumen
def fungsi3():
# ini adalah isi dari fungsi
	print("Tidak ada kata")

# memanggil fungsi 
fungsi1("variabel satu", "variabel dua")
fungsi1_lagi("variabel tiga", "variabel empat")
fungsi2("variabel lima")
fungsi3()