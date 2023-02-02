isRun = True
totalRating = 0
currenBestRating = 0
banyakWisata = 0
happinessScale = 0
favWisata = ''

def main():
    print("Selamat datang ke Dek Depe Holiday Tracker!")
    mainInput()
    inputWisata()
    happinessCalculation()
    summary()

def mainInput():
    global banyakWisata
    print()
    while isRun: #meminta input banyak wisata
        inpBanyakWisata = int(input("Masukkan banyak tempat wisata yang kamu kunjungi: "))
        if inpBanyakWisata <= 0:
            print("Input tidak valid. Silahkan masukkan input kembali!\n")
        else:
            banyakWisata += inpBanyakWisata
            return not isRun

def inputWisata():
    global totalRating
    global currenBestRating
    global favWisata
    for i in range(banyakWisata):
        inpWisata = input(f'Perjalanan {i+1}: ')
        inpRating = int(input(f'Rating perjalanan kamu ke {inpWisata} (indeks 1-10): '))
        totalRating += inpRating

        #menentukan wisata paling mengesankan
        if inpRating >= currenBestRating:
            currenBestRating = inpRating
            favWisata = inpWisata


def happinessCalculation():
    global happinessScale
    happinessScale += totalRating/banyakWisata

def summary():
    print("---Summary---")
    print(f'Perjalanan paling mengesankan adalah ketika pergi ke {favWisata}')
    print(f"Skala kebahagiaan Dek Depe adalah {round(happinessScale, 2)}")

    #skala kebahagian untuk menetapkan pengalaman berwisata
    if(8 <=happinessScale <= 10):
        print("Dek Depe bahagia karena pengalamannya menyenangkan.") 
    elif(5 <=happinessScale < 8):
        print("Dek Depe senang karena pengalamannya cukup baik.")
    elif(happinessScale < 5):
        print("Dek Depe sedih karena pengalamannya buruk.")

    print()
    print("Terimakasih telah menggunakan Dek Depe Holiday Tracker!")

if __name__ == "__main__":
    main()
