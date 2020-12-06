def urai (kataUrai):
    hasil = ''
    for row in range (len(kataUrai)):
        for col in range (row + 1):
            hasil += kataUrai[col]
            hasil += ""
    hasil += ""
    return hasil
    
def rajut (kataRajut):
    syarat = [1]
    awal = 1
    for i in range (2, len(kataRajut)):
        awal += i
        syarat.append(awal)
    panjang = syarat.index(len(kataRajut)) + 1
    panjang *= -1
    hasil2 = kataRajut [panjang: len(kataRajut)]
    return hasil2

# kata = input('Masukkan Kata : ')
# pilihan = input('Masukkan pilihan menu (Rajut/Urai) : ').lower()
# if pilihan == 'rajut':
#     print(rajut(kata))
# elif pilihan == 'urai':
#     print(urai(kata))
# else:
#     print('Pilihan anda tidak ada')

print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))