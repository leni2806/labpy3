## labpy03
## LATIHAN1

Program Menampilkan N Bilangan Acak Yang Lebih Kecil Dari 0.5

### Algoritmanya
1. import random memanggil file random.
2. n = int(input("Masukan nilai N : ")) input variabel n, tipe data integer.
3. for c in range(n) : looping for index c dengan jumlah perulangan sebanyak n.
4. b = random.uniform(.0,.5) variabel a berisikan random angka dari 0.0 sampai 0.5.
5. print ("Data ke : ",a,"==>",b) print data ke : a = index looping b = angka random sesuai syarat nomor 4.
6. print("-----FINISH-----") print Selesai di luar looping.
7. Run program latihan1.

### Flowchart
  
![](<latihan1.png>)

### Screenshot
![](<code11.png>)



1. Ketikan Program print ("Bilangan Acak yang Lebih Kecil Dari 0.5")
=>print ('Bilangan Acak yang Lebih Kecil Dari 0.5') Untuk Menampilkan atau Mencetak kalimat *Bilangan Acak yang Lebih Kecil Dari 0.5
2. Ketikan Program import random
=> import random memanggil file random.
3. ketikan program n = int(input("Masukan nilai N : "))
=> n = int(input("Masukan nilai N : ")) input variabel n, tipe data integer.
4. Ketikan Program a=0
5. ketikan program for c in range(n) :
=> for c in range(n) : looping for index c dengan jumlah perulangan sebanyak n.
6. ketikan program a+=1
=> a+=1, setiap looping nilai akan bertambah 1
7. ketikan program b = random.uniform(.0,.5
= > b = random.uniform(.0,.5) variabel a berisikan random angka dari 0.0 sampai 0.5.
8. ketikan program print ("Data ke : ",a,"==>",b)
=> print ("Data ke : ",a,"==>",b) print data ke : a = index looping b = angka random sesuai syarat nomor 4.
9. ketikan program print("-----FINISH-----")

### Hasilnya
![](<hasil11.png>)


## LATIHAN2

Program Sederhana Pengulangan Dengan Menghitung Laba Pengusaha

### Algoritma
1. x=100000000 modal 100.000.000, variable x.
2. summer=0 variable untuk menjumlah total laba.
3. y=0 variable untuk masa bulan.
4. lb = [int(0), int(0), int(a) * .1, int(a) * .1, int(a) * .5, int(a) * .5, int(a) * .5, int(a) * .2] variable untuk jumlah laba perbulan, dipisahkan dengan koma dan tipe data integer.
5. for i in lb : looping for index i dengan mengambil data dari lb.
6. sum=sum+i rumus untuk menghitung total laba perbulan.
7. y+=1 masa bulan, tiap looping menambah 1.
8. print('Laba Bulan Ke-', y ,'Sebesar :',y) print : y = ambil masa bulan, i = ambil dari data yang ada di dalam lb.
9. print('TOTAL LABA YANG DI DAPAT ADALAH :',sum) print total laba.
10. Run Program2.

- Flowchart
![](<flowchrt2.jpg>)



### Screenshot
![](<coke-2.png>)



1. Ketikan program
=> x=100000000 modal 100.000.000, variable x.
2. Ketikan program sum=0
=> sum=0 kode sum disini untuk menentukan jumlah total laba
3. ketikan program
=> y=0 y= untuk variable masa bulan
4. ketikan program lb = [int(0), int(0), int(x) * .1, int(x) * .1, int(x) * .5, int(x) * .5, int(x)* .5, int(x) * .2]
=> lb = [int(0), int(0), int(x) * .1, int(x) * .1, int(x) * .5, int(x) * .5, int(x)* .5, int(x) * .2] Untuk Mendeklarasikan presentase laba tiap bulan dan di kali dengan x atau data inputan modal investasi yaitu 100000000
5. ketikan program print(" Modal Awal Seorang Pengusaha :',x")
=> print(" Modal Awal Seorang Pengusaha :',x") Menampilkan kalimat *Modal Awal : dan data yang berisi di x yaitu 100000000
6. ketikan program for i in lb :
=> for i in lb : looping for index i dengan mengambil data dari lb.
7. ketikan program sum=sum+i
sum=sum+i rumus untuk menghitung total laba perbulan.
8. ketikan program y+1
=> y+=1, masa bulan tiap looping menambah 1.
9. print('Laba Bulan Ke-', y ,'Sebesar :',i)
=> print('Laba Bulan Ke-', y ,'Sebesar :',i) print : y = ambil masa bulan, i = ambil dari data yang ada di dalam lb.
10. print('TOTAL LABA YANG DI DAPAT ADALAH :',sum)
=> print('TOTAL LABA YANG DI DAPAT ADALAH :',sum) print total laba.

### Hasilnya
![](<hasil-2.png>)

## LATIHAN3
program sederhana mensimulasikan mesin ATM. 

### Algoritmanya
Tetapkan variabel saldo dengan nilai awal 1000000 (Rp 1.000.000).
Buat variabel pilihan untuk menyimpan pilihan pengguna.
Selama saldo lebih besar dari 0, ulangi langkah-langkah berikut:
Tampilkan menu pilihan:
1. Tarik Uang
2. Keluar
Minta pengguna untuk memilih salah satu opsi.
Jika pilihan adalah 1 (Tarik Uang):
Minta pengguna memasukkan jumlah yang ingin ditarik.
Jika jumlah penarikan lebih kecil dari atau sama dengan saldo:
Kurangi saldo dengan jumlah yang ditarik.
Tampilkan pesan "Penarikan berhasil!" dan saldo baru.
Jika tidak:
Tampilkan pesan "Saldo tidak mencukupi."
Jika pilihan adalah 2 (Keluar):
Akhiri program dengan menampilkan pesan "Terima kasih telah menggunakan ATM!"

### Flowchart
![](<latihanbank.png>)



### Screenshot
![](<kodeatm.png>)


1. ketikan program
=> saldo = 1000000: Membuat variabel saldo
2. ketikan program riwayat_transaksi
=> riwayat_transaksi = []: Membuat list kosong bernama riwayat_transaksi untuk menyimpan catatan setiap transaksi yang dilakukan.
3. ketikan while True
=> while True:: Membuat loop tak terbatas.
4. tampilkan menu
=> print(f"Saldo saat ini: Rp {saldo}"): Menampilkan saldo terkini pengguna.
=> print("1. Tarik Uang"): Menampilkan opsi pertama, yaitu menarik uang.
=> print("2. Keluar"): Menampilkan opsi kedua, yaitu keluar dari program.
5. ketikan input pengguna
=> pilihan = int(input("Pilih menu (1/2): ")): Meminta pengguna untuk memilih salah satu opsi (1 atau 2) dan menyimpan pilihan tersebut dalam variabel pilihan.
6. masukkan logika prnarikan
=> if pilihan == 1:: Jika pengguna memilih opsi 1 (Tarik Uang):
=> jumlah_tarik = int(input("Masukkan jumlah penarikan: "))
=> if jumlah_tarik <= saldo:: Memeriksa apakah jumlah yang ingin ditarik tidak melebihi saldo yang ada.
7. ika saldo mencukupi:
=> saldo -= jumlah_tarik: Mengurangi saldo dengan jumlah yang ditarik.
8. iwayat_transaksi.append(f"Penarikan: Rp {jumlah_tarik}"): Menambahkan catatan transaksi ke dalam list riwayat_transaksi.
=> print("Penarikan berhasil!"): Menampilkan pesan keberhasilan penarikan.
9. Jika saldo tidak mencukupi:
=> print("Saldo tidak mencukupi!"): Menampilkan pesan bahwa saldo tidak cukup.
10. keluar dari program
=> elif pilihan == 2:: Jika pengguna memilih opsi 2 (Keluar):
print("Terima kasih telah menggunakan ATM!"): Menampilkan pesan terima kasih.
print("Riwayat Transaksi:"): Menampilkan judul "Riwayat Transaksi".
for transaksi in riwayat_transaksi:: Melakukan perulangan untuk setiap transaksi dalam list riwayat_transaksi.
print(transaksi): Mencetak setiap transaksi yang telah dilakukan.
break: Menghentikan loop. 
11.pilihan tidak valid
=> else:: Jika pengguna memilih angka selain 1 atau 2, akan muncul pesan "Pilihan tidak valid."


### Hasilnya
![](<Screenshot 2024-11-02 123146.png>)


