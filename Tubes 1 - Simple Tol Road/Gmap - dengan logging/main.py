# PROGRAM SIMULASI PINTU TOL BERBASIS KARTU E-MONEY
# membuat simulasi pintu tol yang berbasis kartu e-money dengan tujuan memahami struktur proses yang dilakukan pintu tol otomatis

"""
PEMBUAT:
    Kelompok 10
    -> 16522098 - Muhammad Farhan
    -> 16522208 - Hafidz Yasifa Patty
    -> 19622078 - Raden Francisco Trianto B.
    -> 19622188 - Mattheuw Suciadi Wijaya

ASUMSI :
    - input kartu digital yang seharusnya discan disimulasikan dengan
      menginput secara manual data (kode kartu, saldo) yang dianggap 
      jika format kode kartu sudah valid maka anggap selalu benar tanpa
      perlu diverifikasi kodenya
"""

#ALGORITMA

# menggunakan import
import datetime
import logging
# membuat configurasi logging
logging.basicConfig(level=logging.DEBUG, filename="templog.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

# insialisasi fungsi
def inpkendaraan():
    # mendapatkan golongan kendaraan yang valid
    input_kendaraan = False
    while input_kendaraan == False:
        print("Pilih jenis golongan kendaraan:")
        print("~ golongan 1 (rp5.000) -> sedan, jip, truk kecil, dan bus")
        print("~ golongan 2 (rp8.000) -> truk dengan 2 gandar")
        print("~ golongan 3 (rp11.000)-> truk dengan 3 gandar")
        print("Masukkan golongan kendaraan: ")
        jenis_kendaraan = input(">>> ")
        if(jenis_kendaraan.isdigit()):
            jenis_kendaraan = int(jenis_kendaraan)
            if(any(jenis_kendaraan==num for num in [1,2,3])):
                input_kendaraan = True
                biaya_kendaraan = 5000+(jenis_kendaraan-1)*3000
            else:
                print("Input golongan kendaran hanya antara 1 / 2 / 3")
        else:
            print("Input dalam bentuk angka saja")
    return [biaya_kendaraan, jenis_kendaraan]

def inpkodekartu():
    # mendapatkan kodekartu yang valid
    input_kodekartu = False
    while input_kodekartu == False:
        print("Masukan kode kartu: XXXX-XXXX-XXXX-XXXX")
        kode_kartu = input(">>> ")
        if(len(kode_kartu) == 19):
            arrdigit_4 = kode_kartu.split("-")
            for digit_4 in arrdigit_4:
                if(not digit_4.isdigit()):
                    print("Kode kartu salah, contoh format yang benar XXXX-XXXX-XXXX-XXXX")
                    break
            else:
                input_kodekartu = True
                kode_kartu = ""
                for digit_4 in arrdigit_4:
                    kode_kartu += digit_4
        elif(len(kode_kartu) == 16):
            for digit in kode_kartu:
                if(digit.isdigit() == False):
                    break
            else:
                input_kodekartu = True
        else:
            print("Kode kartu salah, contoh format yang benar XXXX-XXXX-XXXX-XXXX")
    return kode_kartu

def inpsaldo():
    # mendapatkan saldo kartu yang valid
    input_saldo = False
    while input_saldo == False:
        print("Masukkan saldo kartu: ")
        saldo = input(">>> ")
        try:
            saldo = float(saldo)
        except:
            print("Format saldo salah, titik hanya sebagai penanda desimal")
        else:
            input_saldo = True
    return saldo

def inpgerbang():
    # mendapatkan biaya gerbang, gerbang masuk, dan gerbang keluar yang valid
        # Menampilkan data biaya tambahan pada setiap gerbang
        # Dibuat secara hardcoded yang dapat dilihat sebagai tabel berikut:
    print("Tabel harga dari gerbang ke gerbang dalam ribu rupiah (tidak termasuk biaya jenis kendaraan)")
    print("  A  B  C  D  E")
    print("A X  10 14 21 26")
    print("B 10 X  12 18 22")
    print("C 14 12 X  11 16")
    print("D 21 18 11 X  21")    
    print("E 26 22 16 21 X") # X diganti dengan 0 dalam matriksnya
    biaya = [[0, 10, 14, 21, 26], [10, 0, 12, 18, 22], [14, 12, 0, 11, 16], [21, 18, 11, 0,  21], [26, 22, 16, 21, 0]] 
    input_gerbangmasuk = False
    while input_gerbangmasuk == False:
        masuk = input("Masukkan gerbang masuk: ")
        if(any(masuk == cek for cek in ["A","B","C","D","E"])):
            input_gerbangmasuk = True
        else:
            print("Masukkan gerbang hanya diantara: A/B/C/D/E")
    input_gerbangkeluar = False
    while input_gerbangkeluar == False:
        keluar = input("Masukkan gerbang keluar: ")
        if(any(masuk == cek for cek in ["A","B","C","D","E"])):
            if(masuk == keluar):
                print("Gerbang masuk tidak boleh sama dengan gerbang keluar")
            else:
                input_gerbangkeluar = True
        else:
            print("Masukkan gerbang hanya diantara: A/B/C/D/E")
    biaya_gerbang = biaya[ord(masuk)-65][ord(keluar)-65]*1000
    return [biaya_gerbang,masuk,keluar]

# PEMBUKA PROGRAM
print("\n")
print("".center(60,"="))
print("Simulasi Gerbang Jalan Tol".center(60))

# mencatat mulainya simulasi
logging.critical("Simulasi Dimulai")

# LOOP SIMULASI
simulasi = True
while simulasi:
    logging.debug("Kendaraan terdeteksi")
    # palang pintu gerbang, false jika tertutup, true jika sudah terbuka
    palang_pintu_gerbang = False

    logging.warning("Input semua data mulai")
    # Input jenis kendaraan = [golongan, biaya]
    input_kendaraan = inpkendaraan()
    logging.debug("Input jenis kendaraan berhasil")
    print()

    # Input kode kartu (16 angka string)
    kode_kartu = inpkodekartu()
    logging.debug("Input kode kartu berhasil")    
    print()

    # Input saldo kartu
    saldo = inpsaldo()
    logging.debug("Input saldo kendaraan berhasil")
    print()

    # Input Gerbang = [biaya_gerbang, masuk, keluar]
    input_gerbang = inpgerbang()
    logging.debug("Input gerbang berhasil")
    logging.warning("Input semua data berhasil")
    print()

    # Mendapat harga dari gerbang masuk dan keluar serta tambahan dari jenis mobil
    harga = (input_gerbang[0] + input_kendaraan[1])
    pembayaran = False
    print(f"Biaya total gerbang: {harga}")
    # jika tidak bayar atau saldo kurang dari harga
    if((saldoakhir := saldo - harga) < 0):
        # saldoakhir = saldo - harga
        logging.warning("Pembayaran gagal")
        print("Pembayaran gagal, saldo tidak cukup")
        print("Masukkan kartu lainnya atau pencet tombol bantuan\n")            
        # pencet tombol bantuan atau tidak
        input_tombol = False
        masukankartu = False
        while input_tombol == False:
            print("Pencet tombol bantuan? [ya/tidak] ")
            bantuan = input(">>> ")
            if(any(bantuan==char for char in ["y","Y","ya","Ya"])):
                print("Bantuan telah dipanggil")
                input_tombol = True
            elif(any(bantuan==char for char in ["t","T","tidak","Tidak"])):
                print("Bantuan tidak dipanggil")
                masukankartu = True
                input_tombol = True
            else:
                print("input antara y(iya) atau t(tidak)")
        if(masukankartu == True):
            # kembali ke input jenis kendaraan
            continue
    else: # jika bisa bayar
        pembayaran = True
        logging.warning("Pembayaran berhasil")
        print("Pembayaran telah berhasil, palang telah dibuka")
        print(f"Sisa saldo Anda: {saldoakhir:.2f} rupiah")
        palang_pintu_gerbang = True
        # mencatat di log.txt sebagai sejarah
        with open("log.txt","a") as file:
            file.write(f"\n{datetime.datetime.now().strftime('%c')}: {kode_kartu}; {saldo}; {saldoakhir}; {input_kendaraan[1]}; {input_gerbang[1]}; {input_gerbang[2]}")
        
    print()
    # apakah lanjut simulasi atau tidak 
    input_akhir = False
    while input_akhir == False:
        print("lanjutkan simulasi? [ya/tidak]")
        bantuan = input(">>> ")
        if(any(bantuan==char for char in ["y","Y","ya","Ya"])):
            input_akhir = True
        elif(any(bantuan==char for char in ["t","T","tidak","Tidak"])):
            logging.critical("Simulasi Selesai")
            print("Simulasi berakhir")
            input_akhir = True
            simulasi = False
        else:
            print("input antara y(iya) atau t(tidak)")