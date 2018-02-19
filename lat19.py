# membuat fungsi pisang_dan_keju
def pisang_dan_keju(jml_pisang, jml_keju):
	print(f"Kita punya pisang sebanyak {jml_pisang} buah.")
	print(f"Dan keju sebanyak {jml_keju} buah.")
	print("Jumlah yang cukup untuk membuat pisang keju")
	print("\n")


# memanggil fungsi secara langsung
print("Menggunakan fungsi scara langsung")
pisang_dan_keju(20, 30)


# memberikan variabel sendiri
print("Memberikan variabel dari skrip")
total_pisang = 20
total_keju = 70
# memanggil fungsi
pisang_dan_keju(total_pisang, total_keju)


# menggunakan operator matematika di fungsi
print("Menggunakan operasi matematika")
pisang_dan_keju(40 + 35, 23 + 6)


# penggunaan variabel dan matematika
print("Menggunakan variabel dan amtematika")
pisang_dan_keju(total_pisang + 5, total_keju + 30)


# penggunaan input dan fungsi
print("Menggunakan input")
prompt = "> "
print("Berapa sisa pisang")
sisa_pisang = input(prompt)
print("Berapa sisa keju")
sisa_keju = input(prompt)
pisang_dan_keju(sisa_pisang, sisa_keju)