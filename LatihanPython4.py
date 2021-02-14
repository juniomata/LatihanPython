# # SOAL 1

#----------------------------------------------------------------------------------
hari = ['senin', 'selasa', 'rabu', 'kamis', "jum'at", 'sabtu', 'minggu']
 
while True:
    try:
        input_hari = input("\nMasukkan nama Hari : ")
        input_hari = input_hari.lower()

        for i in hari:
            if i == input_hari:
                jumlah = int(input('Masukkan Jumlah : '))
                mod_jumlah = jumlah%7

                if jumlah >= 0:
                    index_hari = hari.index(input_hari)
                    penjumlahan_hari = index_hari + mod_jumlah
                    hasil_hari = hari[penjumlahan_hari-7]
                    print(f'{jumlah} hari dari hari {input_hari} adalah hari {hasil_hari}')
                    break
                else:
                    index_hari = hari.index(input_hari)
                    pengurangan_hari = index_hari + mod_jumlah
                    hasil_hari = hari[pengurangan_hari]
                    print(f'{jumlah} hari dari hari {input_hari} adalah hari {hasil_hari}')
                    break
                
            elif i != input_hari and i == hari[len(hari)-1]:
                print('Hari tidak ditemukan')
    except:
        print('Hanya menerima integer untuk Jumlah')


# # SOAL 2 -- Palindrome

#----------------------------------------------------------------------------------
while True:
        kata = str(input("\nMasukkan kata: "))
        kata = kata.lower()
        kata_dibalik = ''

        if len(kata) >= 3 and kata.isalpha() == True:
            for i in kata:
                kata_dibalik = i + kata_dibalik

            if (kata == kata_dibalik):
                print(f"Kata {kata} TERMASUK Palindrome")
            else:
                print(f"Kata {kata} TIDAK TERMASUK Palindrome")
        else:
            print('Input yang Anda masukkan salah.')





# # SOAL 3
# input_angka = int(input('Masukkan 4 digit angka: '))
# Input : Masukkan 4 digit angka : 5493
# Output nya :
# 9354

#----------------------------------------------------------------------------------
while True:
    try:
        input_angka = int(input('Masukkan 4 digit angka : '))
        angka_dibalik = 0
        
        if 9999 > input_angka > 999:
            while input_angka > 0:
                if input_angka != 0:
                    angka_dibalik = angka_dibalik * 100 + input_angka%100
                    input_angka //= 100
            print(angka_dibalik)
        elif input_angka < 0:
            print('Tidak menerima angka negatif')
        else:
            print('Hanya menerima angka 4 digit')
    except:
        print('Hanya menerima integer') 

# Penjelasan
# # # iterasi 1
# angka_dibalik = 0*100 + 4567%100 = 0 + 67 = 67
# input_angka = 4567 // 100 = 45

# # # iterasi 2
# angka_dibalik = 67*100 + 45%100 = 6700 + 45 = 6745
# input_angka = 45 // 100 = 0

# # iterasi 3
# angka_dibalik = 6745*100 + 0%100 = 674500 + 0 = 674500
# input_angka = 45 // 100 = 0





# # SOAL 4
# Output : 6387
# (Gunakan Hanya Fungsi-Metode Numerik-Aritmatik)
# Input :
# Masukkan 2 digit angka : 63
# Masukkan 2 digit angka kedua : 87 


#----------------------------------------------------------------------------------
while True:
    try:
        input_1 = int(input('\nMasukkan 2 digit angka : '))
        input_2 = int(input('Masukkan 2 digit angka kedua: '))        
        
        if 99 > input_1 > 9 and 99 > input_2 > 9:
            input_1 = input_1*100
            hasil = input_1 + input_2
            print(hasil)
        elif input_1 < 0 or input_2 < 0:
            print('Tidak menerima angka negatif')
        else:
            print('Hanya menerima angka 2 digit')
    except:
        print('Hanya menerima integer')







