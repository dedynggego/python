from fa import FA, cetakPapanCatur
import sys
import time

start_time = time.time()

#menentukan dimensi permasalahan yaitu ukuran papan catur
dimensi = input("masukkan nilai queen (10 <= N <= 20): ")

try:
    dimensi = int(dimensi)
except ValueError:
    print('input harus berupa angka')
    sys.exit()

if dimensi < 10 or dimensi > 20:
    print('input harus berupa angka diantara 10 sampai 500')
    sys.exit()

#menentukan jumlah firefly dan iterasi, biasanya sekumpulan firefly beranggotakan 15-40 ekor
jumlahFirefly = 15
jumlahIterasi = 5000

print('Penerapan algoritma firelfy pada kasus n-queens problem ' + '\n')
print('dimensi= ' + '%i' % dimensi)
print('jumlah firefly= ' + '%i' % jumlahFirefly)
print('jumlah iterasi= '+ '%i' % jumlahIterasi)
print('')

print('Memasuki pencarian solusi terbaik menggunakan algoritma FA (Firefly Algorithm)')
#solusiTerbaik, fitnessTerbaik, iterasiTerbaik = FA(dimensi, jumlahFirefly,jumlahIterasi,1)
#start_time1 = time.time()
solusiTerbaik, fitnessTerbaik, iterasiTerbaik = FA(dimensi, jumlahFirefly,jumlahIterasi)
print('perhitungan telah selesai')
#waktu1 = time.time() - start_time1
print('**********************************')

#start_time2 = time.time()
solusiTerbaik2, fitnessTerbaik2, iterasiTerbaik2 = FA(dimensi, jumlahFirefly, jumlahIterasi)
#solusiTerbaik2, fitnessTerbaik2 = FA(dimensi, jumlahFirefly,jumlahIterasi,2)
print('perhitungan telah selesai')
#waktu2 = time.time() - start_time2
print('**********************************')

#start_time3 = time.time()
solusiTerbaik3, fitnessTerbaik3, iterasiTerbaik3 = FA(dimensi, jumlahFirefly, jumlahIterasi)
print('perhitungan telah selesai')
#waktu3 = time.time() - start_time3
print('*****************************')

print('solusi terbaik yang ditemukan adalah: ')
print('Solusi terbaik 1: ', solusiTerbaik)
print('Jumlah iterasi: ', iterasiTerbaik)
print('---------------------------------')
print('Solusi terbaik 2: ', solusiTerbaik2)
print('Jumlah iterasi: ', iterasiTerbaik2)
print('---------------------------------')
print('Solusi terbaik 3: ', solusiTerbaik3)
print('Jumlah iterasi: ', iterasiTerbaik3)
print('---------------------------------')
print('')

print('Dengan nilai fitness: ')
print(fitnessTerbaik)
print(fitnessTerbaik2)
print(fitnessTerbaik3)
print('')

"""
print("Waktu eksekusi: ")
print("waktu eksekusi 1= " + "%.5f" %waktu1)
print("waktu eksekusi 2= " + "%.5f" %waktu2)
print("waktu eksekusi 3= " + "%.5f" %waktu3)
"""

print('Hasil visualisasi papan catur')
cetakPapanCatur(solusiTerbaik, dimensi)
cetakPapanCatur(solusiTerbaik2, dimensi)
cetakPapanCatur(solusiTerbaik3, dimensi)
print('')

waktu = time.time() - start_time
print("waktu eksekusi " + "%.5f" %waktu + " detik")

