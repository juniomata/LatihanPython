1.
### PERTANYAAN
# Jumlah ayam dan kambing joni 13
# jumlah kaki ayam dan kambing joni 32
# Berapa jumlah ayam dan kambing joni?

# Input : 
# - Masukkan jumlah ayam dan kambing
# - Masukkan jumlah kaki ayam dan kambing

# Output :
# - Jumlah Ayam Joni ... ekor dan jumlah kambing Joni ... ekor

# ANSWER:
total_hewan = int(input("Masukkan jumlah ayam dan kambing: "))
total_kaki = int(input("Masukkan jumlah kaki ayam dan kambing: "))
kaki_ayam = 2
kaki_kambing = 4
kambing = int((total_kaki - kaki_ayam*total_hewan)/(kaki_kambing-kaki_ayam))
ayam = total_hewan - kambing

print(f"Jumlah Ayam Joni {ayam} ekor dan jumlah kambing Joni {kambing} ekor")

2. 
### PERTANYAAN
# Sembilan belas tahun lalu, umur anak setengah tahun lebih muda dari seperempat umur ibunya.
# Umur anak sekarang 19 taun lebih tua dari sepertujuh umur ibunya
# Berapa umur Ibu saat melahirkan anaknya?

# Output: Usia Ibu ketika melahirkan anaknya adalah ... tahun

# ANSWER
# Pers 1: A - 19 = 1/4*(I-19)-1/2
# Pers 2: A = 19 + 1/7*I

#Substitusi A pada pers 2 ke pers 1
    # A - 19         = 1/4*(I-19)-1/2
    # 19 + 1/7*I -19 = 1/4*(I-19)-1/2
    # 1/7*I          = 1/4*I - 19/4 - 1/2
    # 1/4*I - 1/7*I  = 19/4 + 1/2
    # I              = (19/4 + 1/2)/(1/4-1/7)
    
sekian_tahun_lalu = 19
lebih_muda        = 1/2
rasio1            = 1/4
rasio2            = 1/7

I = (sekian_tahun_lalu*rasio1 + lebih_muda)/(rasio1-rasio2)
A = sekian_tahun_lalu + rasio2*I
umur_ibu_melahirkan = round(I-A)

print(f"Usia Ibu ketika melahirkan anaknya adalah {umur_ibu_melahirkan} tahun")

3. 
### PERTANYAAN
# Jumlah usia budi dan ayah sekarang adalah 50 taun 
# Empat taun lalu usia ayah 6x usia budi
# Berapa usia ayah dan budi saat ini?

# Output: Usia ayah saat ini adalah ... tahun dan usia Budi saat ini adalah ... tahun

# ANSWER
# Pers 1: usia_ayah + usia_budi = total_usia -> usia_budi = total_usia - usia_ayah
# Pers 2: usia_ayah - 4 = 6*(usia_budi-4)

#Substitusi usia_budi pada pers 1 ke pers 2
    # usia_ayah - 4           = 6*(total_usia - usia_ayah - 4)
    # usia_ayah               = 6*total_usia - 6*usia_ayah - 24 + 4
    # usia_ayah + 6usia_ayah  = 6*total_usia - 24 + 4
    # 7usia_ayah              = 6(total_usia - 4) + 4
    # usia_ayah               = (6*(total_usia - 4) + 4)/7

total_usia = int(input("Masukkan jumlah usia Ayah dan Budi: "))
kelipatan_usia_ayah = 6
kelipatan_usia_andi = 1
sekian_tahun_lalu = 4

usia_ayah = (kelipatan_usia_ayah*(total_usia - sekian_tahun_lalu) + sekian_tahun_lalu)/(kelipatan_usia_ayah+kelipatan_usia_andi)
usia_budi = total_usia - usia_ayah

print(f"Usia Ayah saat ini adalah {usia_ayah} tahun dan usia Budi saat ini adalah {usia_budi} tahun")