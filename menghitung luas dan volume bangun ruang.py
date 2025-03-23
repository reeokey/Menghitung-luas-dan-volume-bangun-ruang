import math

# fungsi untuk menghitung luas permukaaan dan volume kubus
def hitung_kubus(sisi):
    luas_permukaan = 6 * sisi**2
    volume =  sisi**3
    return luas_permukaan, volume

# fungsi untuk menghitung luas permukaan dan volume balok
def hitung_balok(panjang,lebar,tinggi):
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    volume = panjang * lebar * tinggi
    return luas_permukaan, volume

# fungsi untuk menghitung luas permukaan dan volume lingkaran
def hitung_lingkaran(jari_jari):
    luas_permukaan = 4 * math.pi * jari_jari **2
    volume = (4/3) * math.pi * jari_jari**3
    return luas_permukaan, volume

# fungsi untuk menghitung luas permukaan dan volume tabung
def hitung_tabung(jari_jari, tinggi):
    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    volume =  math.pi * jari_jari**2 * tinggi
    return luas_permukaan, volume

# fungsi untuk menghitung luas permukaan dan volume prisma
def hitung_prisma(luas_alas, keliling_alas, tinggi):
    luas_permukaan = 2 * luas_alas + keliling_alas * tinggi
    volume = luas_alas * tinggi
    return luas_permukaan, volume

# fungsi untuk menghitung luas permukaan dan volume kerucut
def hitung_kerucut(jari_jari, tinggi):
    sisi_miring = math.sqrt(jari_jari**2 + tinggi**2)
    luas_permukaan = math.pi * jari_jari * (jari_jari + sisi_miring)
    volume = (1/3) * math.pi * jari_jari**2 * tinggi
    return luas_permukaan, volume

# fungsi untuk menghitung luas permukaan dan volume limas
def hitung_limas(luas_alas, tinggi):
    # asumsi limas dengan alas persegi
    sisi_alas = math.sqrt(luas_alas)
    luas_segitiga = 0.5 * sisi_alas * tinggi
    luas_permukaan =  luas_alas + 4 * luas_segitiga
    volume = (1/3) * luas_alas * tinggi
    return luas_permukaan, volume

# nama user
nama_user = input("Masukkan Nama Anda: ")

# menu pilihan
print("\nSelamat Datang, " + nama_user + "!")
print("Di Program Kami")
print("Pilih Bangun Ruang:")
print("1. Kubus")
print("2. Balok")
print("3. Lingkaran")
print("4. Tabung")
print("5. Prisma")
print("6. Kerucut")
print("7. Limas")
print()
pilihan = int(input("Masukkan Nomor Pilihan: "))

# memproses pilihan pengguna
if pilihan == 1:
    sisi = float(input("Masukkan Panjang Sisi Kubus: "))
    luas_permukaan, volume = hitung_kubus(sisi)
elif pilihan == 2:
    panjang = float(input("Masukkan Panjang Balok: "))
    lebar = float(input("Masukkan Lebar Balok: "))
    tinggi = float(input("Masukkan Tinggi Balok: "))
    luas_permukaan, volume =  hitung_balok(panjang, lebar, tinggi)
elif pilihan == 3:
    jari_jari = float(input("Masukkan Jari-Jari Lingkaran: "))
    luas_permukaan, volume = hitung_lingkaran(jari_jari)
elif pilihan == 4:
    jari_jari = float(input("Masukkan Jari-Jari Tabung: "))
    tinggi = float(input("Masukkan Tinggi Tabung: "))
    luas_permukaan, volume = hitung_tabung(jari_jari, tinggi)
elif pilihan == 5:
    luas_alas = float(input("Masukkan Luas Alas Prisma: "))
    keliling_alas = float(input("Masukkan Keliling Alas Prisma: "))
    tinggi = float(input("Masukkan Tinggi Prisma: "))
    luas_permukaan = hitung_prisma(luas_alas, keliling_alas, tinggi)
elif pilihan == 6:
    jari_jari = float(input("Masukkan Jari-Jari Kerucut: "))
    tinggi = float(input("Masukkan Tinggi Kerucut: "))
    luas_permukaan = hitung_kerucut(jari_jari, tinggi)
elif pilihan == 7:
    luas_alas = float(input("Masukkan Luas Alas Limas: "))
    tinggi = float(input("Masukkan Tinggi Limas: "))
    luas_permukaan = hitung_limas(luas_alas, tinggi)
else:
    print("Pilihan Tidak Valid!!")

# menampilkan hasil perhitungan
if pilihan >= 1 and pilihan <= 7:
    print("\nLuas Permukaan:", luas_permukaan)
    print("Volume:", volume)

