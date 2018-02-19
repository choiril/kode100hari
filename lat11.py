# menampilkan pertanyaan berapa usiamu
print("Berapa usiamu?", end=' ')
# memberikan inout dengan keyboard
umur = input()
print("Berapa tinggimu?", end=' ')
tinggi = input()
print("Berapa berat badanmu?", end=' ')
berat = input()

# format string dari hasil inputan
print(f"Jadi, umurmu adalah {umur}, tinggi {tinggi}, dan beratmu {berat}")

# study drills

# akan menampilkan pertanyaan siapa namamu dan kita akan memberikan inputan setalah pertanyaan tampil
nama = input("Ketik namamu: ")
# akan menampilkan hasil inputan
print("Hai", nama)
# penggunaan paramater sep, sep sendiri kepanjangan dari separator yang artinya pemisah
tetangga = input("Ketik nama tetangga sebelah kananmu: ")
print("Tetangga sebelah kananmu bernama ", tetangga, '!', sep='')
# jika tidak menggunakan separator
tetangga1 = input("Ketik nama tetanggamu sebelah kirimu: ")
print("Tetangga sebelah kirimu bernama ", tetangga1,'!')
# menggunakan tipe data integer 
# jika kita tidak menentukan tipe datanya maka hasilnya juga berbeda 
x = int(input("Masukkan angka pertama: "))
y = int(input("Masukkan angka kedua: "))
print("Hasil penjumlahan dari ", x, ' dan ', y, ' adalah ', x+y, '.', sep='')
# ini ketika tipe data tidak ditentukan maka otomatis dianggap string
x = input("Ketikkan angka pertama: ")
y = input("Ketikkan angka kedua: ")
print("Penjumlahan dari", x, ' dan ', y, ' adalah ', x + y, '.', sep='')