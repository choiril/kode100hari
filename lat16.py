from sys import argv

script, namafile = argv

print(f"Script akan menghapus isi dari {namafile}")
print("Jika tidak ingin menghapus silahkan tekan ctrl+c")
print("Jika lanjut silahkan tekan enter")
input("?")
print("Membuka file....")
# akan membuka file dan akan menghapus isi file pertama, w untuk menghapus isi file
file = open(namafile, 'w')

print(f"Menghapus isi dari {namafile}")
file.truncate()

print(f"Sekarang tulis ulang isi dari {namafile}")

baris1 = input("baris pertama: ")
baris2 = input("baris kedua: ")
baris3 = input("baris ketiga: ")

file.write(str(baris1) + "\n" + str(baris2) + "\n" + str(baris3) + "\n")
print(f"penulisan isi {namafile} telah selesai")
file.close()

file2 = open(namafile)
print(file2.read())
file2.close()

# modul open punya mode dengan perwakilan sebuah huruf, seperti 
# w untuk menghapus isi file awal
# r untuk membaca isi
# x untuk membuat file baru dan untuk menulis isi file
# a untuk membuka file yang telah ada dan menambah isi file