import math

#function kalkulasi
def luasSetengahLingkaran(a):
    return(((math.pi * ((a/2)**2))/2))

def luasSegitiga(b):
    return(b**2 / 2)

def luasPersegi(c):
    return(c**2)

def luasTrapesium(d, e):
    return(((d + e)*d)/2)
    
#input request user    
inpName = input('Nama: ')
inpPanjangPersegi = float(input('Panjang persegi nametag (cm): '))
inpPanjangTrapesium = float(input('Panjang trapesium nametag (cm): '))
inpBanyak = int(input("Banyak nametag: "))

#inisialisasi luas
luasSetengahLingkaran = luasSetengahLingkaran(inpPanjangPersegi)
luasSegitiga = luasSegitiga(inpPanjangPersegi)
luasPersegi = luasPersegi(inpPanjangPersegi)
luasTrapesium = luasTrapesium(inpPanjangPersegi, inpPanjangTrapesium)

#kalkulasi luas dan harga
totalLuas = luasSetengahLingkaran + luasSegitiga + luasPersegi + luasTrapesium
luasNametag = totalLuas * inpBanyak
harga = luasNametag * 0.40
totalHarga = math.ceil(harga/1000) * 1000 

#output
print(f"Halo, {inpName}! Berikut informasi terkait nametag kamu:")
print()
print(f"Luas 1 nametag: {round(totalLuas, 2)} cm^2")
print(f"Luas total nametag: {round(luasNametag, 2)} cm^2")
print(f'Uang yang diperlukan: Rp {round(totalHarga)}')

