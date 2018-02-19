# membuat tab pada teks
teks_tab = "\tIni akan membuat tab pada teks"
# membuat baris baru
teks_pisah = "Ini akan membuat\nbaris baru"
#membuat slash
teks_garing = "membuat \\ slash \\ pada teks"

# membuat list atau daftar teks
list_teks = """
Ini akan membuat list atau daftar
\t* list pertama
\t* list kedua
\t* list ketiga
"""

print(teks_tab)
print(teks_pisah)
print(teks_garing)
print(list_teks)
# membuat tanda petik satu
petik_satu = "Ini akan membuat\'tanda petik satu\'"
# membuat tanda petik dua
petik_dua = "Membuat\"tanda petik dua\""
# membuat suara beep saat kode dijalankan
ascii_bel = "Akan mengeluarkan suara beep\a"
# membuat tab dan baris baru secara otomatis
ascii_formfeed = "Membuat\fformfeed"
# menghapus satu karakter sebelah kiri
ascii_backspace = "Menghapus satu karakter \b sebelah kiri pada teks"
# menghilangkan kata pertama dan menempatkan kata terakhir di awal
ascii_carriagereturn = "ini_akan_hilang\rini yang akan tampil"
# membuat vertical tab
ascii_vertical_tab = "memuat vertical\vtab"
# membuat karakter nilai octal
ascii_nilai_octal = "nilai octal \100 "
# membuat nilai hex
ascii_nilai_hex = "nilai hex \x40"
#membuat karakter 16 bit dengan nilai hex, 2764 akan membuat bentuk hati
ascii_16_bit = "Ini adalah karakter 16bit \u2764"
#membut karakter 32 bit dengan nilai hex, 1F605 akan membuat emoticon senyum
ascii_32_bit = "Ini adalah karakter 32bit \U0001F605"
a = "\x49"
b = "\u2764"
c = "\x75"

print(petik_satu)
print(petik_dua)
print(ascii_bel)
print(ascii_formfeed)
print(ascii_backspace)
print(ascii_carriagereturn)
print(ascii_vertical_tab)
print(ascii_nilai_octal)
print(ascii_nilai_hex)
print(ascii_16_bit)
print(ascii_32_bit)
# tambahan
print(a, b, c)

