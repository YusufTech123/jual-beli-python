#sistem jual beli buah menggunakan python 
#Programmer Yusuf Ghazali

#kode dibawah akan menampilkan daftar buah yang tersedia dan harganya
print('=' * 25)
print('Sistem jual beli barang menggunakan python')
print('Programmer : Yusuf Ghazali')
print('=' * 25)
print('Barang yang tersedia: ')
print('1.Apel    = Rp.5000')
print('2.Mangga  = Rp.7000')
print('3.Pisang  = Rp.6000')
print('4.Nanas   = Rp.8000')
print('5.Anggur  = Rp.10000')
print('6.Jeruk   = Rp.4000')
print('7.Pepaya  = Rp.9000')
print('=' * 25)

#kode dibawah adalah integer harga dari masing-masing buah 

apel = 5000
mangga = 7000
pisang = 6000
nanas = 8000
anggur = 10000
jeruk = 4000
pepaya = 9000

#kode ini adalah gambaran uang yang akan digunakan untuk membeli buah 

money_apel    = 500000
money_mangga  = 500000
money_pisang  = 500000
money_nanas   = 500000
money_anggur  = 500000
money_jeruk   = 500000
money_pepaya  = 500000
money         = 500000

print(f'Uangmu ada Rp.{money}')

print('=' * 25)

#kode ini akan meminta si pembeli untuk memasukkan angka berdasarkan buah yang ingin dibeli

memilih = input('Silahkan pilih buah yang ingin dibeli dengan memasukkan angka buah tersebut 1/2/3/4/5/6/7: ')

if memilih == '1':
    print(f'Anda memilih buah apel dengan harga Rp.{apel}')

elif memilih == '2':
    print(f'Anda memilih buah mangga dengan harga Rp.{mangga}')

elif memilih == '3':
    print(f'Anda memilih buah pisang dengan harga Rp.{pisang}')

elif memilih == '4':
    print(f'Anda memilih buah nanas dengan harga Rp.{nanas}')

elif memilih == '5':
    print(f'Anda memilih buah anggur dengan harga Rp.{anggur}')

elif memilih == '6':
    print(f'Anda memilih buah jeruk dengan harga Rp.{jeruk}')

elif memilih == '7':
    print(f'Anda memilih buah pepaya dengan harga Rp.{pepaya}')

else: 
    print('Angka yang anda masukkan tidak valid')

#kode dibawah akan menghitung hasil dari buah yang dipilih dan berapa banyak yang ingin dibeli

if (memilih == '1'):
    total_apel = input('Anda ingin membeli berapa apel?: ')
    count_apel = int(total_apel)
    hasil_apel = count_apel * apel
    print(f'Total harga apel yang anda beli adalah Rp.{hasil_apel}')

    #kode ini untuk menyatakan jika uang kurang dan jika uang lebih dibagian apel

    if (money_apel > hasil_apel):
         print('Anda telah berhasil membeli ' + str(total_apel) + ' apel')
         print('Dan uang Anda tersisa Rp.' + str(money_apel - hasil_apel))
         print('=' * 25)
         print('Pembelian telah selesai')
         print('=' * 25)
    
    elif (money_apel == hasil_apel):
         print('Uang Anda masih cukup untuk membeli ' + str(total_apel) + ' apel')
         print('Anda telah berhasil membeli apel, Dan uang Anda tersisa Rp.' + str(money_apel - hasil_apel))
         print('=' * 25)
         print('Pembelian telah selesai')
         print('=' * 25)

    else: 
         print('Uang Anda tidak mencukupi untuk membeli apel sebanyak itu')
    

elif (memilih == '2'):
    total_mangga = input('Anda ingin membeli berapa mangga?: ')
    count_mangga = int(total_mangga)
    hasil_mangga = count_mangga * mangga
    print(f'Total harga mangga yang anda beli adalah Rp.{hasil_mangga}')

    #kode ini untuk menyatakan jika uang kurang dan jika uang lebih dibagian mangga

    if (money_mangga > hasil_mangga):
         print('Anda telah berhasil membeli ' + str(total_mangga) + ' mangga')
         print('Dan uang Anda tersisa Rp.' + str(money_mangga - hasil_mangga))
         print('=' * 25)
         print('Pembelian telah selesai')
         print('=' * 25)
    
    elif (money_mangga == hasil_mangga):
         print('Uang Anda masih cukup untuk membeli ' + str(total_mangga) + ' mangga')
         print('Anda telah berhasil membeli mangga, Dan uang Anda tersisa Rp.' + str(money_mangga - hasil_mangga))
         print('=' * 25)
         print('Pembelian telah selesai')
         print('=' * 25)

    else: 
         print('Uang Anda tidak mencukupi untuk membeli mangga sebanyak itu')

elif (memilih == '3'):
    total_pisang = input('Anda ingin membeli berapa pisang?: ')
    count_pisang = int(total_pisang)
    hasil_pisang = count_pisang * pisang
    print(f'Total harga pisang yang anda beli adalah Rp.{hasil_pisang}')

    #kode ini untuk menyatakan jika uang kurang dan jika uang lebih dibagian pisang
    
    if (money_pisang > hasil_pisang):
         print('Anda telah berhasil membeli ' + str(total_pisang) + ' pisang')
         print('Dan uang Anda tersisa Rp.' + str(money_pisang - hasil_pisang))
         print('=' * 25)
         print('Pembelian telah selesai')
         print('=' * 25)
    
    elif (money_pisang == hasil_pisang):
         print('Uang Anda masih cukup untuk membeli ' + str(total_pisang) + ' pisang')
         print('Anda telah berhasil membeli pisang, Dan uang Anda tersisa Rp.' + str(money_pisang - hasil_pisang))
         print('=' * 25)
         print('Pembelian telah selesai')
         print('=' * 25)

    else: 
         print('Uang Anda tidak mencukupi untuk membeli pisang sebanyak itu')

elif (memilih == '4'):
    total_nanas = input('Anda ingin membeli berapa nanas?: ')
    count_nanas = int(total_nanas)
    hasil_nanas = count_nanas * nanas
    print(f'Total harga nanas yang anda beli adalah Rp.{hasil_nanas}')

    #kode ini untuk menyatakan jika uang kurang dan jika uang lebih dibagian nanas

    if (money_nanas > hasil_nanas):
         print('Anda telah berhasil membeli ' + str(total_nanas) + ' nanas')
         print('Dan uang Anda tersisa Rp.' + str(money_nanas - hasil_nanas))
         print('=' * 25)
         print('Pembelian telah selesai')
         print('=' * 25)
    
    elif (money_nanas == hasil_nanas):
         print('Uang Anda masih cukup untuk membeli ' + str(total_nanas) + ' nanas')
         print('Anda telah berhasil membeli nanas, Dan uang Anda tersisa Rp.' + str(money_nanas - hasil_nanas))
         print('=' * 25)
         print('Pembelian telah selesai')
         print('=' * 25)

    else: 
         print('Uang Anda tidak mencukupi untuk membeli nanas sebanyak itu')

elif (memilih == '5'):
    total_anggur = input('Anda ingin membeli berapa anggur?: ')
    count_anggur = int(total_anggur)
    hasil_anggur = count_anggur * anggur
    print(f'Total harga anggur yang anda beli adalah Rp.{hasil_anggur}')

    #kode ini untuk menyatakan jika uang kurang dan jika uang lebih dibagian anggur

    if (money_anggur > hasil_anggur):
         print('Anda telah berhasil membeli ' + str(total_anggur) + ' anggur')
         print('Dan uang Anda tersisa Rp.' + str(money_anggur - hasil_anggur))
         print('=' * 25)
         print('Pembelian telah selesai')
         print('=' * 25)
    
    elif (money_anggur == hasil_anggur):
         print('Uang Anda masih cukup untuk membeli ' + str(total_anggur) + ' anggur')
         print('Anda telah berhasil membeli anggur, Dan uang Anda tersisa Rp.' + str(money_anggur - hasil_anggur))
         print('=' * 25)
         print('Pembelian telah selesai')
         print('=' * 25)

    else: 
         print('Uang Anda tidak mencukupi untuk membeli anggur sebanyak itu')

elif (memilih == '6'):
    total_jeruk = input('Anda ingin membeli berapa jeruk?: ')
    count_jeruk = int(total_jeruk)
    hasil_jeruk = count_jeruk * jeruk
    print(f'Total harga jeruk yang anda beli adalah Rp.{hasil_jeruk}')

    #kode ini untuk menyatakan jika uang kurang dan jika uang lebih dibagian jeruk

    if (money_jeruk > hasil_jeruk):
         print('Anda telah berhasil membeli ' + str(total_jeruk) + ' jeruk')
         print('Dan uang Anda tersisa Rp.' + str(money_jeruk - hasil_jeruk))
         print('=' * 25)
         print('Pembelian telah selesai')
         print('=' * 25)
    
    elif (money_jeruk == hasil_jeruk):
         print('Uang Anda masih cukup untuk membeli ' + str(total_jeruk) + ' jeruk')
         print('Anda telah berhasil membeli jeruk, Dan uang Anda tersisa Rp.' + str(money_jeruk - hasil_jeruk))
         print('=' * 25)
         print('Pembelian telah selesai')
         print('=' * 25)

    else: 
         print('Uang Anda tidak mencukupi untuk membeli jeruk sebanyak itu')

elif (memilih == '7'):
    total_pepaya = input('Anda ingin membeli berapa pepaya?: ')
    count_pepaya = int(total_pepaya)
    hasil_pepaya = count_pepaya * pepaya
    print(f'Total harga pepaya yang anda beli adalah Rp.{hasil_pepaya}')

    #kode ini untuk menyatakan jika uang kurang dan jika uang lebih dibagian pepaya

    if (money_pepaya > hasil_pepaya):
         print('Anda telah berhasil membeli ' + str(total_pepaya) + ' pepaya')
         print('Dan uang Anda tersisa Rp.' + str(money_pepaya - hasil_pepaya))
         print('=' * 25)
         print('Pembelian telah selesai')
         print('=' * 25)
         
    elif (money_pepaya == hasil_pepaya):
         print('Uang Anda masih cukup untuk membeli ' + str(total_pepaya) + ' pepaya')
         print('Anda telah berhasil membeli pepaya, Dan uang Anda tersisa Rp.' + str(money_pepaya - hasil_pepaya))
         print('=' * 25)
         print('Pembelian telah selesai')
         print('=' * 25)

    else: 
         print('Uang Anda tidak mencukupi untuk membeli pepaya sebanyak itu')

    #kode ini untuk menyatakan jika tidak ada nilai yang valid 

else: 
    print('Tidak valid')

keluar = input('tekan enter sekali untuk keluar: ')
