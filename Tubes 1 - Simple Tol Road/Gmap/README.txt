PEMBUAT:
    Kelompok 10
    -> 16522098 - Muhammad Farhan
    -> 16522208 - Hafidz Yasifa Patty
    -> 19622078 - Raden Francisco Trianto Bratadiningrat
    -> 19622188 - Mattheuw Suciadi Wijaya

ASUMSI :
    - input kartu digital yang seharusnya discan disimulasikan dengan menginput secara 
    manual data (kode kartu, saldo) yang dianggap jika format kode kartu sudah valid maka 
    anggap selalu benar tanpa perlu diverifikasi kodenya
    - anggap kendaraan sudah masuk tol dan sedang berada di pintu keluar tol sehingga langsung terkena biaya tol

KAMUS :
    kode_kartu, bantuan, selesai : string
    saldo, harga, saldoakhir : int
    simulasi, palang_pintu_gerbang, pembayaran, masukkankartu, input_akhir : bool
    input_kendaraan, input_gerbang : array string

LIBRARY:
    openpyxl
    datetime