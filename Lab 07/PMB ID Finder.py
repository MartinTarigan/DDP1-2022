# Martin Marcelino Tarigan/2206029645

#data
setID = set()
lstID = []
lstName = []
dctMonthName = {}
dctMonthNPM = {}
isRun = True 

def main():
    print("Selamat datang di program Mengenal Angkatan!")
    print("===========================================")
    print("Masukkan identitas mahasiswa: ")
    inpID()
    addToList()
    searchID()
    print('Terima kasih telah menggunakan program ini, semangat PMB-nya!')

#meminta input ke user
def inpID():
    while isRun:
        inpIdentity = input()
        if inpIdentity == "STOP":
            return not isRun
        setID.add(inpIdentity)

def addToList():
    for id in setID:
        lstID.append(id)

    for id in lstID:
        if id.split()[4] in dctMonthName.keys() and id.split()[4] in dctMonthNPM.keys():
            dctMonthName[id.split()[4]].append(id.split()[0])
            dctMonthNPM[id.split()[4]].append(id.split()[1])
        else:
            dctMonthName[id.split()[4]] = [id.split()[0]]
            dctMonthNPM[id.split()[4]] = [id.split()[1]]

def searchID():
    while isRun:
        print()
        inpMonth = input('Cari mahasiswa berdasarkan bulan: ')
        if inpMonth == 'STOP':
            return not isRun
        print('================= Hasil ================')
        if inpMonth in dctMonthName.keys() and inpMonth in dctMonthNPM.keys():
            print(f'Terdapat {len(set(dctMonthName[inpMonth]))} nama yang lahir di bulan {inpMonth}: ')
            for id in set(dctMonthName[inpMonth]):
                print(f'- {id}')
            print()
            print(f'Terdapat {len(set(dctMonthNPM[inpMonth]))} nama yang lahir di bulan {inpMonth}: ')
            for id in set(dctMonthNPM[inpMonth]):
                print(f'- {id}')
        else:
            print(f'Tidak ditemukan mahasiswa dan NPM yang lahir di bulan {inpMonth}.')
if __name__ == "__main__":
    main()

  
