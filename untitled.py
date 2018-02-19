# pengguanaan angka dan string
#ketika inputan tidak ditentukan jenis tipe datanya maka hasilnya beda, dari contoh diatas meski kita input angka tapu dianggap string bukan integer
x = input("Ketikkan angka pertam: ")
y = input("Ketikkan angka kedua: ")
print("Penjumlahan dari", x, ' dan ', y, ' adalah ', x + y, '.', sep='')

# penentuan string
# Konversi string ke int sebelum penambahan
xString = input("Enter a number: ")
x = int(xString)
yString = input("Enter a second number: ")
y = int(yString)
print('The sum of ', x, ' and ', y, ' is ', x+y, '.', sep='')

# Dua input numerik, dengan konversi langsung
x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))
print('The sum of ', x, ' and ', y, ' is ', x+y, '.', sep='')

# Dua input numerik, jumlah eksplisit
x = int(input("Enter an integer: "))
y = int(input("Enter another integer: "))
sum = x+y
print('The sum of ', x, ' and ', y, ' is ', sum, '.', sep='')

# Bandingkan cetak dengan Rangkaian dan dengan format string.
applicant = input("Enter the applicant's name: ")
interviewer = input("Enter the interviewer's name: ")
time = input("Enter the appointment time: ")
print(interviewer + ' will interview ' + applicant + ' at ' + time +'.')
print(interviewer, ' will interview ', applicant, ' at ', time, '.', sep='')
print('{} will interview {} at {}.'.format(interviewer, applicant, time))


# Format string format yang lebih bagus dengan nomor identifikasi parameter - berguna bila beberapa parameter digunakan beberapa kali.
x = int(input('Enter an integer: '))
y = int(input('Enter another integer: '))
formatStr = '{0} + {1} = {2}; {0} * {1} = {3}.'
equations = formatStr.format(x, y, x+y, x*y)
print(equations)