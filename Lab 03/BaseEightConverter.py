# Martin Marcelino Tarigan/2206029645

def main():
    print("Selamat Datang di Bunker Hacker!")
    covertion()
    print('Terima kasih telah menggunakan Bunker Hacker!')

def covertion():
    print()
    inpConvertion = int(input("Masukkan berapa kali konversi yang ingin dilakukan: "))
    print()

    for i in range (inpConvertion):
        inpInteger = int(input("Masukkan angka ke-" + str(i+1) + " yang ingin dikonversikan (dalam desimal): "))
        resultBin = "" #menginisialisasi variabel kosong untuk hasil akhir
        while inpInteger:
            sisa = inpInteger % 8 
            resultBin = str(sisa) + resultBin #memasukkan sisa bagi ke variabel kosong
            inpInteger = inpInteger // 8 #memasukkan hasil bagi
        result(resultBin)

def result(resultBin):   
    print(f'Hasil konversi desimal ke basis 8: {resultBin}')
    print()

main()
