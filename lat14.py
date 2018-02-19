# membuat game zork and adventure sederhana
# penggunaannya script ini adalah: python lat14.py argumen1 argumen2
from sys import argv
# script disni adalah nama script jadi nilainya tetap
script, nama, level = argv
# membuat nilai dari prompt menjadi >
prompt = '>'

# penggunaan format string
print(f"Hai, {nama}! Ini adalah simulasi permainan Zork and Adventure pada latihan {script} level {level}")
print("Sebelum memulai saya akan menanyakan beberapa pertanyaan dan selamat menikmati")
print("Siapakah namamu?")
# membuat prompt untuk jawaban
namamu = input(prompt)

# print pertanyaan
print("Pertanayaan kedua, sekolah terakhir apa?")
# membuat prompt untuk jawaban
lulusan = input(prompt)

print("Apa cita-citamu?")
# membuat prompt untuk jawaban
cita2 = input(prompt)

print("Pertanyaan terakhir, tulis pesan dan kesanmu tentang program ini")
# penggunaan format string dan membuat baris baru dengan tanda (""")
print(f"""
Permaianan telah usai, dari permainan tadi dapat disimpulkan bahwa namamu adalah {namamu}.
Kamu lulusan {lulusan}.
Cita-citamu adalah {cita2}
Untuk pesan dan kesanmu tentang pprogram ini adalah {kesan}
""")

print("ketik ya untuk berhenti atau tidak maka program selesai")
# membuat prompt untuk jawaban
henti = input(prompt)

