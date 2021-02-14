# LATIHAN

# 1.
# Input: Masukkan Jumlah Hari:
# Output: Nyatakan jumlah hari tersebut dalam
# ... Tahun .... Bulan ... Hari
# angka harus dua digit

try:
    jumlah_hari = int(input("Masukkan Jumlah Hari: "))

    if jumlah_hari<0:
        print("Tidak menerima angka negatif")
    else:
        tahun = 365
        bulan = 30
        minggu = 7

        x_tahun = jumlah_hari//tahun
        sisa_hari = jumlah_hari%tahun

        x_bulan = sisa_hari//bulan
        sisa_hari = sisa_hari%bulan

        x_minggu = sisa_hari//minggu
        sisa_hari = sisa_hari%minggu

        if len(str(x_tahun)) == 1:
            if len(str(x_bulan)) == 1:
                print(f"0{x_tahun} Tahun 0{x_bulan} Bulan 0{x_minggu} Minggu 0{sisa_hari} Hari")
            else:
                print(f"0{x_tahun} Tahun {x_bulan} Bulan 0{x_minggu} Minggu 0{sisa_hari} Hari")                
        else:
            if len(str(x_bulan)) == 1:
                print(f"{x_tahun} Tahun 0{x_bulan} Bulan 0{x_minggu} Minggu 0{sisa_hari} Hari")
            else:
                print(f"{x_tahun} Tahun {x_bulan} Bulan 0{x_minggu} Minggu {sisa_hari} Hari")

except:
    print("Angka yang Anda masukkan salah")

# 2. 
# Input:
# Masukkan kalimat:
# Masukkan karakter:

# Output:
# Jumlah karakter ... di dalam kalimat ... adalah ...

kalimat = input("Masukkan kalimat: ")
karakter = input("Masukkan karakter: ")
kalimat_lower = kalimat.lower()
karakter_lower = karakter.lower()

jml_karakter = kalimat_lower.count(karakter_lower)

print(f"Jumlah karakter {karakter} di dalam kalimat {kalimat} adalah {jml_karakter}")

# 3. 
# Input:
# Masukkan Text: Hari ini adalah hari Rabu
# Masukkan huruf vokal: O

# Output: 
# Horo ono odoloh horo robo

input_teks = input("Masukkan teks: ")
input_vokal = input("Masukkan huruf vokal: ")

gantivokal = input_teks.replace("a",input_vokal)
gantivokal = gantivokal.replace("i",input_vokal)
gantivokal = gantivokal.replace("u",input_vokal)
gantivokal = gantivokal.replace("e",input_vokal)
gantivokal = gantivokal.replace("o",input_vokal)
gantivokal = gantivokal.replace("A",input_vokal.upper())
gantivokal = gantivokal.replace("I",input_vokal.upper())
gantivokal = gantivokal.replace("U",input_vokal.upper())
gantivokal = gantivokal.replace("E",input_vokal.upper())
gantivokal = gantivokal.replace("O",input_vokal.upper())

print(gantivokal)


# 4.
# Hitung Body Mass Index
# Rumus BMI: massa (kg)/tinggi (dalam m) pangkat 2

# Input:
# Masukkan Tinggi Badan (dalam cm):
# Masukkan massa (dalam kg):

# Kondisi:
# - Nilai tinggi dan massa tidak boleh negatif -> keluar notif: "Tidak menerima angka negatif"
# - Nilai tinggi dan massa tidak boleh string atau desimal -> "Angka yang anda masukkan salah"
# - Batas maks massa: 200 kg dan tinggi 300 cm -> Notif "Tinggi/Massa yang anda masukkan di luar batas"

# Output:
# Sesuaikan dgn hasil
# BMI < 18.5 -> Berat Badan Kurang
# 18.5 - 24.9 -> Berat Badan Ideal
# 25 - 29.9 -> Berat Badan Berlebih
# 30 - 39.9 -> Berat Badan Sangat Berlebih
# BMI >= 40 -> Obesitas

# Tinggi badan anda {} m dan Massa anda {} kg, BMI anda {} dan anda termasuk {kondisi}

try:
    tinggi = int(input("Masukkan tinggi badan (dalam cm): "))
    massa = int(input("Masukkan massa (dalam kg): "))
    if tinggi < 0 or massa < 0:
            print("Tidak menerima angka negatif")
    elif tinggi > 300 or massa > 200:
            print("Tinggi/Massa yang anda masukkan di luar batas")
    else:
            bmi = int(massa/((tinggi/100)**2))
            if bmi < 18.5:
                kategori = "Berat Badan Kurang"                
            elif bmi > 18.5 and bmi < 24.9: 
                kategori = "Berat Badan Ideal"
            elif bmi > 26 and bmi < 29.9: 
                kategori = "Berat Badan Berlebih"
            elif bmi > 30 and bmi < 39.9: 
                kategori = "Berat Badan Sangat Berlebih"
            else:
                kategori = "Obesitas"
            print(f"Tinggi badan anda {tinggi} m dan Massa anda {massa} kg, BMI anda {bmi} dan anda termasuk {kategori}")

except:
    print("Angka yang anda masukkan salah")

# 5. 
# Input:
# Masukkan nilai:

# Kondisi:
# 90 ke atas: Grade A
# 85 ke atas: Grade A-
# 80 ke atas: Grade B
# 75 ke atas: Grade B-
# 70 ke atas: Grade C
# 65 ke atas: Grade D
# Dibawah 65: Anda tidak lulus perlu remedial

# Kondisi:
# - Nilai max 100, nilai min 0
# - Jika nilai di atas 100: Nilai di luar jangkauan
# - Jika nilai di bawah 0: Tidak menerima nilai negatif
# - Jika inputan bukan angka: Angka yang anda masukkan salah
# - Bisa menerima desimal

# nilai = input("Masukkan nilai: ")

try:
    nilai = float(input("Masukkan nilai: "))
    if nilai > 100:
            print("Nilai di luar jangkauan")
    elif nilai < 0:
            print("Tidak menerima nilai negatif")
    else:
            if nilai > 90:
                print("Grade A")
            elif nilai > 85:
                print("Grade A-")
            elif nilai > 80:
                print("Grade B")
            elif nilai > 75:
                print("Grade B-")
            elif nilai > 70:
                print("Grade C")
            elif nilai > 65:
                print("Grade D")
            else:
                print("Anda tidak lulus. Perlu remedial.")
except:
    print("Angka yang anda masukkan salah")