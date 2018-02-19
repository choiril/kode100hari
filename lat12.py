# latihan ke-12 hampir sama dengan latihan ke-11
# pengguanaan angka dan string
#ketika inputan tidak ditentukan jenis tipe datanya maka hasilnya beda, dari contoh diatas meski kita input angka tapu dianggap string bukan integer
x = input("Ketikkan angka pertama: ")
y = input("Ketikkan angka kedua: ")
print("Penjumlahan dari", x, ' dan ', y, ' adalah ', x + y, '.', sep='')

# penentuan string
# Konversi string ke int sebelum penambahan
xString = input("Masukkan angka: ")
x = int(xString)
yString = input("Masukkan angka lagi: ")
y = int(yString)
print('Jumlah dari ', x, ' dan ', y, ' adalah ', x+y, '.', sep='')

# Dua input numerik, dengan konversi langsung
x = int(input("Masukkan angka: "))
y = int(input("Masukkan angka kedua: "))
print('Hasil penjumlahan dari ', x, ' dan ', y, ' adalah ', x+y, '.', sep='')

# Bandingkan cetak dengan Rangkaian dan dengan format string.
pelamar = input("Masukkan nama pelamar kerja: ")
pewancara = input("Masukkan nama pewancara: ")
waktu = input("Masukkan waktu wawancara: ")
print(pewancara + ' akan menginterview ' + pelamar + ' pada ' + waktu +'.')
print(pewancara, ' akan menginterview', pelamar, ' pada ', time, '.', sep='')
print('{} akan menginterview {} pada {}.'.format(pewancara, pelamar, waktu))


# Format string format yang lebih bagus dengan nomor identifikasi parameter - berguna bila beberapa parameter digunakan beberapa kali.
x = int(input('Masukkan integer: '))
y = int(input('Masukkan integer lainnya: '))
formatStr = '{0} + {1} = {2}; {0} * {1} = {3}.'
equations = formatStr.format(x, y, x+y, x*y)
print(equations)