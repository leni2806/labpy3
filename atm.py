saldo = 1000000
riwayat_transaksi = []

while True:
    print(f"Saldo saat ini: Rp {saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")
    pilihan = int(input("Pilih menu (1/2): "))

    if pilihan == 1:
        jumlah_tarik = int(input("Masukkan jumlah penarikan: "))
        if jumlah_tarik <= saldo:
            saldo -= jumlah_tarik
            riwayat_transaksi.append(f"Penarikan: Rp {jumlah_tarik}")
            print("Penarikan berhasil!")
        else:
            print("Saldo tidak mencukupi!")
    elif pilihan == 2:
        print("Terima kasih telah menggunakan ATM!")
        print("Riwayat Transaksi:")
        for transaksi in riwayat_transaksi:
            print(transaksi)
        break
    else:
        print("Pilihan tidak valid.")