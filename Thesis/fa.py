import random
import math
from pprint import pprint

class Firefly:
    def __init__(self, posisi, fitness, intensitas):
        self.posisi = posisi
        self.fitness = fitness
        self.intensitas = intensitas

def FA(dimensi, jumlahFirefly, jumlahIterasi):
    #inisialisasi parameter
    #random.seed(seed)
    B0 = 1.0
    g = 1.0
    a = 2

    posisiTerbaik = []
    fitnessTerbaik = float('inf')
    daftarFirefly = []

    print('Inisialisasi firefly pada posisi acak')
    idxPosisiTerbaik = -1

    #inisialisasi data pada masing2 firefly
    for i in range(jumlahFirefly):
        posisi = random.sample(range(dimensi),dimensi)
        
        #hitung fitness
        fitness = HitungFitness(posisi, dimensi)

        #hitung intensitas
        if fitness > 0 :
            intensitas = 1/fitness
        else:
            intensitas = 1

        daftarFirefly.append(Firefly(posisi, fitness, intensitas))
        cetakPapanCatur(posisi, dimensi)
        print('Firefly '+ str(i + 1) + ' memiliki nilai fitness = ' + '%i' % fitness)

        #cek posisi terbaik sementara kunang-kunang
        if daftarFirefly[i].fitness < fitnessTerbaik:
            fitnessTerbaik = daftarFirefly[i].fitness
            posisiTerbaik = daftarFirefly[i].posisi
            idxPosisiTerbaik = i
    
    print('')
    print('posisi terbaik sementara')
    print('Firefly ' + str(idxPosisiTerbaik + 1) + ' dengan nilai fitness = ' + '%i' % fitnessTerbaik)
    print('')

    print('Mulai proses pencarian posisi firefly terbaik')
    #pencarian posisi terbaik berdasarkan intensitas cahaya
    #jumlahTidakDitemukanSolusiBaru = 0
    iterasi = 0
    while iterasi < jumlahIterasi:
        iterasi += 1
        pprint(iterasi)

        for i in range(jumlahFirefly):
            for j in range(jumlahFirefly):
                if daftarFirefly[i].intensitas < daftarFirefly[j].intensitas:
                    #print(daftarFirefly[j].posisi)
                    #hitung jarak posisi antar firefly
                    r = 0.0
                    for k in range(dimensi):
                        r += math.pow(daftarFirefly[i].posisi[k] - daftarFirefly[j].posisi[k], 2)
                    r = math.sqrt(r)

                    #hitung nilai beta / actractivness
                    beta = B0 * math.exp(-g * r * r)
                    for k in range(dimensi):
                        #pindahkan firefly ke posisi yg baru
                        p = daftarFirefly[i].posisi[k] + beta * (daftarFirefly[j].posisi[k] - daftarFirefly[i].posisi[k])
                        p += a * (random.uniform(0,1) - 0.5)
                        p = round(p)

                        #mengembalikan nilai posisi jika posisi melebihi batas minimal dan maksimal dimensi
                        while p < 0:
                            p += dimensi

                        while p >= dimensi:
                            p -= dimensi

                        #cari index dimana posisi sebelumnya ditemukan dan tukar posisinya dgn posisi yg baru
                        idx = daftarFirefly[i].posisi.index(p)
                        daftarFirefly[i].posisi[idx] = daftarFirefly[i].posisi[k]
                        daftarFirefly[i].posisi[k] = p

                        #hitung nilai fitness dan intensitas utk firefly ini pd posisi yg baru
                        daftarFirefly[i].fitness = HitungFitness(daftarFirefly[i].posisi, dimensi)
                        if daftarFirefly[i].fitness > 0:
                            daftarFirefly[i].intensitas = 1/daftarFirefly[i].fitness
                        else:
                            daftarFirefly[i].intensitas = 1

                        #jika nilai intensitas baru ternyata lebih baik dari nilai fitness umum, maka ambil posisi yg baru
                        #sebagai posisi terbaik secara umum
                        if daftarFirefly[i].fitness < fitnessTerbaik: #posisiTerbaik ditentukan oleh fitness terbaik
                            posisiTerbaik = daftarFirefly[i].posisi
                            fitnessTerbaik = daftarFirefly[i].fitness

                            cetakPapanCatur(posisiTerbaik, dimensi)
                            print('Iterasi ' + str(iterasi) + ', firefly ' + str(i+1) + ' ditemukan nilai fitness terbaik = ' + '%i' % fitnessTerbaik)
                            #jumlahTidakDitemukanSolusiBaru = 0
                            
                            #hentikan perhitungan jika sudah ditemukan nilai fitness terbaik
                            if fitnessTerbaik == 0:
                                return posisiTerbaik, fitnessTerbaik, iterasi
        #urutkan firefly dari nilai fungsi terbaik ke terburuk. semakin kecil semakin baik
        daftarFirefly.sort(key=lambda x: x.fitness, reverse=False)
    return posisiTerbaik, fitnessTerbaik, iterasi
   

def HitungFitness(posisi, dimensi):
    #bangkitkan papan catur sebesar dimensi*dimensi
    papanCatur = [[0 for i in range(dimensi)] for j in range(dimensi)]

    #letakkan bidak queen pada posisi2 yg sudah ditentukan sebelumnya
    for i in range(len(posisi)):
        papanCatur[i][posisi[i]] = 1

    #inisialisasi nilai fitness
    fitness = 0
    #perulangan pada setiap posisi pada papan catur
    for i in range(len(papanCatur)):
        for j in range(len(papanCatur[i])):
            #jika ditemukan queen
            if papanCatur[i][j] == 1:
                #perulangan pd setiap posisi papan catur setelah queen tersebut berada
                for k in range(1, dimensi):
                    #tambahkan 1 ke var fitness jika ditemukan queen lain yg berada pada satu garis lurus
                    #horizontal
                    if (j + k) < dimensi:
                        if papanCatur[i][j + k] == 1:
                            fitness += 1

                    #vertical
                    if (i + k) < dimensi:
                        if papanCatur[i + k][j] == 1:
                            fitness += 1

                    #diagonal kanan bawah
                    if ((i + k) < dimensi) and ((j + k) < dimensi):
                        if papanCatur[i + k][j + k] == 1:
                            fitness += 1

                    #diagonal kiri bawah
                    if ((i + k) < dimensi) and ((j - k) >= 0):
                        if papanCatur[i + k][j - k] == 1:
                            fitness += 1
    return fitness
    
def cetakPapanCatur(posisi, dimensi):
    for i in range(dimensi):
        s1 = ''
        s2 = ''
        for j in range(dimensi):
            if posisi[i] == j:
                s1 += '----'
                s2 += '| Q '
            else:
                s1 += '----'
                s2 += '|   '
        print(s1 + '-')
        print(s2 + '|')

    s1 = ''
    for i in range(dimensi):
        s1 += '----'
    print(s1 + '-')
    