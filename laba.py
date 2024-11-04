modal_awal = 100000000
laba_setiap_bulan = [
    0, 0, 
    modal_awal * 0.1, modal_awal * 0.1, 
    modal_awal * 0.5, modal_awal * 0.5, modal_awal * 0.5, 
    modal_awal * 0.2
    ]
total_laba = 0
for laba in laba_setiap_bulan:
    total_laba += laba
print("Modal Awal Seorang Pengusaha:", modal_awal)
for bulan, laba in enumerate(laba_setiap_bulan, start=1):
    print(f"Laba Bulan Ke-{bulan} Sebesar: {laba}")
print("TOTAL LABA YANG DIDAPAT ADALAH:", total_laba)