from sys import argv

script, namafile = argv
# akan memanggil/membuka file pada argv
file1 = open(namafile)

# menampilkan nama file pada argv
print(f"ini adalah file {namafile}:")
# membaca/menampilkan isi file pada argv
print(file1.read())

#menggunakan close, tapi sampai saat ini masih belum tahu perbedaannya
file1.close()

print("Ketik nama file lagi:")
# ketik file yang akan dibuka, dengan syarat fie masih dalam satu folder
file_baru = input("> ")

# membuka file baru
file2 = open(file_baru)

# membaca/menampilkan isi file baru
print(file2.read())

#menggunakan close, tapi sampai saat ini masih belum tahu perbedaannya
file2.close()