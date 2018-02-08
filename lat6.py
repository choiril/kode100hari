#variabel
tipe_orang = 10
#penggunaan string didalam string dengan format string
x = f"ada {tipe_orang} orang disini."

#variabel
binari = "binari"
tidak_tahu = "tidak tahu"
#penggunaan string didalam string dengan format string
y = f"sebagian ada yang tahu {binari} dan ada yang sebagian {tidak_tahu}."

print(x)
print(y)

#penggunaan string didalam string dengan format string
print(f"Dia berkata : {x}")
#penggunaan string didalam string dengan format string
print(f"Dia juga berkata: '{y}'")

#variabel
respon = False
pertanyaan = "Apakah lelucon ini lucu? {}"

#penggunaan string didalam string dengan format string
#format string dapat ditulis dengan .format()
print(pertanyaan.format(respon))

#variabel
w = "Ini adalah string sebelah kiri "
e = "dan ini adalah string sebelah kanan."

#penjumlahan dengan variabel berupa teks
print(w + e)