# import adalah salah satu fitur atau modul Python
# argv adalah modul python
# untuk menjalankan script yang ada argv adalah namascript.py nilai1 nilai2 nilai3 nilai4
from sys import argv
# ini adalah variabel yang akan di unpack oleh argv
nama_skrip, pertama, kedua, ketiga, keempat, kelima = argv
# menggabungkan argv dan input
keempat = input("masukkan nilai keempat: ")
kelima = input("masukkan nilai kelima: ")
# input tanpa argv
keenam = input("nilai keenam tanpa masuk argv: ")
ketujuh = input("nilai keenam tanpa masuk argv: ")

# menampilkan nilai dari variabel menggunakan argv
print("Skrip ini bernama:", nama_skrip)
print("Ini adalah varibel pertama:", pertama)
print("Variabel kedua:", kedua)
print("Variabel ketiga:", ketiga)
# menampilkan nilai dari variabel menggabungkan argv dn input
print("Variabel keempat:", keempat)
print("varabel kelima:", kelima)
# menampilkan nilai dari variabel menggunakan input
print("variabel keenam:", keenam)
print("variabel ketujuh:", ketujuh)