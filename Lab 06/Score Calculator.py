import math #untuk nilai floor

#list kosong dan variabel kosong
lstKunci = []
lstJawaban = []
countBenar = 0
nilai = 0
isRun = True

def main(): #function memulai program
    print("Selamat mencoba Program Pemeriksa Nilai Dek Depe!")
    print("=================================================")
    insertKunciJawaban()
    insertJawaban()
    cekJawaban()
    koreksi()

    #respons ekspresi
    if 55 <= nilai < 85:
        print("semangat :)")
    elif nilai < 55:
        print("nt")
    elif nilai >= 85:
        print("semangat :D")
    

    #hasil
    print(f"Total jawaban benar adalah {countBenar} dari {len(lstKunci)} soal")
    print(f"Nilai yang kamu peroleh adalah {nilai}")


def insertKunciJawaban(): #function masukin kunci jawaban
    print("Masukkan kunci jawaban: ")
    while isRun:
        input_kunci_jawaban = input("").upper()
        if input_kunci_jawaban == 'STOP':
            return not isRun
        lstKunci.append(input_kunci_jawaban)

def insertJawaban(): #function masukin jawaban
    print("Masukkan jawaban kamu:")
    while isRun:
        inputJawaban = input("").upper()
        if inputJawaban == 'STOP':
            return not isRun
        lstJawaban.append(inputJawaban)
    
def cekJawaban(): #function cek kebenaran
    global countBenar
    for i in range(len(lstJawaban)):
        if lstJawaban[i] == lstKunci[i]:
            countBenar +=1

def koreksi(): #function hitung skor nilai
    global nilai
    nilai = math.floor((countBenar / len(lstJawaban)) * 100)

main()

