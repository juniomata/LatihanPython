1.
# Input : masukan Kalimat 
# "nama saya joni"
# Output : "aman ayas inoj"

while True:
    kalimat = str(input('\nMasukan kalimat: '))
    
    if all(x.isalpha() or x.isspace() for x in kalimat): # kalimat hanya terdiri dari alfabet dan spasi
        kalimat = kalimat.split(" ")

        if len(kalimat) > 1:
            for i in range(0, len(kalimat)):
                for j in kalimat[i]:
                    dibalik = kalimat[i][::-1]
                print(dibalik, end=' ')

        elif len(kalimat) == 1:
            print('Hanya menerima kalimat. Bukan hanya kata.')

    else:
        print('Format input salah')
        



2. 
# Buat Algoritma
# Buat List (masukan List inputan dari user)
# -- Angka - Alfa
# -- Numerik 
# Pilihan :
# 1. Ascending
# 2. Descending
# 3. Min - Max
# Output sesuai pilihan 
# 1. Angka akan di sort dari terkecil ke terbesar
# 2. Angka akan di sort dari terbesar ke terkcecil
# 3. Nilai Minimum dan Nilai Maximum

# Tidak boleh menggunakan Fungsi Sort atau [::-1] atau min() atau max()
# gunakan algoritma


### -----------------------------------------------------------------------------
while True:
    print('Masukan angka acak dengan spasi sebagai pemisah antar angka')
    print('Contoh: 12 8 19 23')
    input1 = input('=> ')
    list_awal = input1.split()
    ## print("List:  ", list_awal)

    while True:
        print('''
        Pilihan:
        a. Ascending
        b. Descending
        c. Min - Max
        ''')
        input_pilihan = input('Pilihan: ')
        
        if input_pilihan == 'a':
            list_berurut = []

            while list_awal:
                minimal = list_awal[0]
                for i in list_awal:
                    if int(i) < int(minimal):
                        minimal = i
                list_berurut.append(int(minimal))
                list_awal.remove(minimal)
            print(f'Ascending = {list_berurut}')
                
        elif input_pilihan == 'b':
            list_berurut = []

            while list_awal:
                maximal = list_awal[0]
                for i in list_awal:
                    if int(i) > int(maximal):
                        maximal = i
                list_berurut.append(int(maximal))
                list_awal.remove(maximal)
            print(f'Descending = {list_berurut}')

        elif input_pilihan == 'c':
            list_berurut = []

            while list_awal:
                minimal = list_awal[0]
                for i in list_awal:
                    if int(i) < int(minimal):
                        minimal = i
                list_berurut.append(int(minimal))
                list_awal.remove(minimal)
                minmax = list_berurut[0]-list_berurut[-1]
            print(f'Min-Max = {minmax}')

        else:
            print('Hanya menerima a, b, c')


3.
# -Buat Algoritma Stats-
# Buat List 
# - Cari Nilai 
# Modus : Nilai yg paling sering muncul 
# Median : Nilai tengah
# Mean : Rata-rata 
# Q1 - Quartil 1 - 25%
# Q3 - Quartil 3 - 75%
# Outliers 

# --------------------------------------------------------------------
List = [12, 7, 9, 26, 7, 6, 5, 1, 18, 14, 20, 12, 11, 19, 17, 15]
total = int()


for i in List:
    total += i
    mean = total/len(List) 
print(f'Mean: {mean}')

list_urut = sorted(List)
if len(List) % 2 == 0:
    median1 = list_urut[len(List)//2] 
    median2 = list_urut[len(List)//2-1]
    median = (median1 + median2)/2
else:
    median = list_urut[len(List)//2] 
print(f'Median: {median}')

# #print(list_urut)
if len(List) % 2 != 0:
    q1 = list_urut[(len(List)+1)//4]
    print((len(List)+1)//4) 
    q3 = list_urut[(len(List)+1)*3//4-1]
    print((len(List)+1)*3//4)
else:
    q1_1 = list_urut[(len(List)+1)//4]
    q1_2 = list_urut[(len(List)+1)//4-1] 
    q1 = (q1_1+q1_2)/2
    q3_1 = list_urut[(len(List)+1)*3//4]
    q3_2 = list_urut[(len(List)+1)*3//4-1]
    q3 = (q3_1+q3_2)/2
print(f'Q1: {q1}')
print(f'Q3: {q3}')


# print(f'Mean: {mean(List)}')
# print(f'Median: {median}')
# print(f'Q1: {q1}')
# print(f'Q3: {q3}')


4.
# Buat Return Function 
# Kalkulator: (+, -, /, *)
# Inputan 
# input angka 1: 8
# input angka 2: 10
# masukan operator : +

# Output : Hasil Penjumlahan dari 8 + 10 = 18

# ----------------------------------------------------
def Kalkulator():
    try:
        print('\nKalkulator +, -, /, *')
        input1 = int(input('Masukan angka 1: '))
        input2 = int(input('Masukan angka 2: '))     
        operator = input('Masukan operator: ')

        if operator == '+':
            hasil = input1 + input2
        elif operator == '-':
            hasil = input1 - input2
        elif operator == '/':
            hasil = input1 / input2
        elif operator == '*':
            hasil = input1 * input2
        else:
            print('Hanya menerima operator +, -, /, *')
        return hasil
    except:
        print('Hanya menerima integer')

while True:
    print(Kalkulator())

5.
# Buat Def Function 
# Fizz Buzz 

# Input : Masukkan Angka :
# Output :
# ANgka dari input user akan menjadi range dari 1 - inputan tersebut 
# Output nya
# akan dicek seluruh angka tersebut 
# kemudian akan di print 
# angka yg habis dibagi 3 diubah menjadi Fizz 
# angka yg habis dibagi 5 diubah menjadi Buzz 
# angka yg habis dibagi 3 dan 5 menjadi FizzBuzz
# angka lain akan dicetak normal 


# --------------------------------------------------
def FizzBuzz(rentang):
    List = []
    for i in range(1, rentang + 1):
        if i % 3 == 0 and i % 5 == 0:
            List.append('FizzBuzz')
        elif i % 3 == 0:
            List.append('Fizz')
        elif i % 5 == 0:
            List.append('Buzz')
        else:
            List.append(i)
    return List 

while True:
    angka = int(input('Masukkan Angka: '))
    print(FizzBuzz(angka))


6. 
#  Buat Def Function 
#  Caesar Cipher 
#  masukan kata : Joni 
#  masukan angka : 2
#  Output nya : lqpk
#  j + 2 = l 
#  o + 2 = q
#  n + 2 = p 
#  i + 2 = k 

#  masukan kata : Joni 
#  masukan angka : -2
#  Output : imlg 


# ---------------------------------------------------------
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def CaesarCipher():
    mod_angka = inputangka%len(alfabet)

    for i in inputkata:
        indexi = alfabet.index(str(i))
        jml_alfa = indexi + mod_angka
        cc = alfabet[jml_alfa-len(alfabet)]
        print(cc, end='')
    
    print()

while True:
    try:
        inputkata = str(input('Masukan kata: '))
        inputangka = int(input('Masukan angka: '))

        if inputkata.isalpha() == True:
            CaesarCipher()
        else:
            print('Hanya bisa memasukan 1 kata')

    except:
            print('Format input salah')
    




7. 
# Konversi Romawi 
# Buat Return Function 
# Gunakan Dict    
# Batasan Maksimal 4000
# Keluar notif : Angka diluar jangkauan 
# Encoder - Decoder Angka Romawi 

# Silakan Masukkan Angka : 2018
# Output nya :MMXVIII

# Silakan Masukkan angka : MMXVIII
# Output nya : 2018


# -----------------------------------------------------------------------
DictRomInt = {"M" : 1000, "CM" : 900, "D": 500, "CD": 400, "C" : 100, "XC" : 90, "L": 50, "XL":40,"X": 10, "IX": 9, "V": 5, "IV":4, "I": 1}

def romawi_int(angka):
        i = 0
        hasil = 0

        while i < len(angka):
            if i + 1 < len(angka) and angka[i:i+2] in DictRomInt:
                hasil += DictRomInt[angka[i:i+2]]
                i += 2
            else:
                hasil += DictRomInt[angka[i]]  
                i += 1
        return hasil

# Karena dari Dict tdk bisa langsung akses key brdskn valuenya, jadi Dict nya dibuat jadi List biar gampang        
def int_romawi(angka):
    hasil = ''
    a = 0
    rom = []
    Int = []

    # #Konversi Dict ke list
    for x, y in DictRomInt.items():
        rom.append(x)
        Int.append(y)
    # #print(rom)
    # #print(Int)

    # #Program konversi integer ke romawi
    if angka < 4000 and angka > 0:
        while angka > 0:
            for i in range(angka // Int[a]):
                hasil += rom[a]
                angka -= Int[a]
            a += 1
        return hasil
    elif angka < 0:
        print('Tidak menerima angka negatif')
    else: 
        print('Angka di luar jangkauan')


while True:
    print()
    print('Pilih:')
    print('a. Integer ke romawi')
    print('b. Romawi ke Integer')
    pilihan = input('(a/b): ')

    print()
    if pilihan == 'a':
        try:
            inputangka = int(input('Masukan angka: '))
            print(int_romawi(inputangka))
        except:
            print('Format input salah')
    elif pilihan == 'b':
        inputangka = input('Masukan angka romawi: ')
        inputangka = inputangka.upper()
        print(romawi_int(inputangka))
    else:
        print('Hanya menerima a dan b')
