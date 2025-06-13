# Variabel number sebagai string
number = "1234567890"

# a. Menampilkan data terakhir
print("Data terakhir:", number[-1])

# b. Menampilkan data pertama
print("Data pertama:", number[0])

# c. Menampilkan data ke-3 sampai ke-6
print("Data ke-3 sampai ke-6:", number[2:6])
number = "1234567890"

print("Pilih yang ingin ditampilkan:")
print("1. Data terakhir")
print("2. Data pertama")
print("3. Data ke-3 sampai ke-6")

pilihan = input("Masukkan pilihan (1/2/3): ")

if pilihan == "1":
    print("Data terakhir:", number[-1])
elif pilihan == "2":
    print("Data pertama:", number[0])
elif pilihan == "3":
    print("Data ke-3 sampai ke-6:", number[2:6])
else:
    print("Pilihan tidak valid!")

