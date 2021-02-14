# PIRAMID ANGKA

# SOAL 1
## Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

print("-"*20+"SOAL 1"+"-"*20)            #Divider antar soal

angka = 1
while angka <= 5:
    print((str(angka)+" ")*angka)
    angka +=1


# SOAL 2
## Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
print("-"*20+"SOAL 2"+"-"*20)           #Divider antar soal

baris = 5
for i in range(1, baris + 1):
    for j in range(1, i+1):
        print(j, end=" ")   #menggabungkan hasil suatu print dengan print berikutnya dalam satu baris
    print()                 #print newline

# SOAL 3
## Output:
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1 

print("-"*20+"SOAL 3"+"-"*20)           #Divider antar soal

baris = 5
for i in range(baris, 0, -1):  #decrement
    for j in range(baris, i-1, -1):
        print(j, end=" ")   #menggabungkan hasil suatu print dengan print berikutnya dalam satu baris
    print()   


# SOAL 4
## Output:
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

print("-"*20+"SOAL 4"+"-"*20)            #Divider antar soal

angka = 1
baris = 1
while angka <= 5:
    print((str(angka)+" ")*(baris+4))
    angka +=1
    baris -=1


#SOAL 5
## Output:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

print("-"*20+"SOAL 5"+"-"*20)            #Divider antar soal

baris = 5
for i in range(baris, 0, -1):           #decrement
    for j in range(1, i+1):
        print(j, end=" ")   #menggabungkan hasil suatu print dengan print berikutnya dalam satu baris
    print()                 #print newline


# SOAL 6
## Output:
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5
print("-"*20+"SOAL 6"+"-"*20)           #Divider antar soal

baris = 5
for i in range(baris, 0, -1):
    for j in range(baris, baris-i, -1):
        print(j, end=" ")   #menggabungkan hasil suatu print dengan print berikutnya dalam satu baris
    print()                 #print newline

# SOAL 7
## Output:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         * 


print("-"*20+"SOAL 7"+"-"*20)            #Divider antar soal

baris = 10
for i in range(baris):
    if i%2 == 0:
        continue
    print(" "*(baris-i-1)+"* "*(i))   
for j in range(baris, 0, -1):
    if j%2 == 0: 
        continue
    print(" "*(baris-j-1)+"* "*(j))

