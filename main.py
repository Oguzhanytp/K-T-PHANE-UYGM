print("""

**********/nKÜTÜPHANEMİZE HOŞGELDİNİZ/n**********

""")

roman =  { 'kırlangıç çığlığı' : {
    'Yazar' : 'Ahmet Umit',
    'Basim_Yili' : '2005',
    'Raf' : 'A1'
},
    'hayalet' : {
        'Yazar' : 'John Black',
        'Basim Yili' : '1995',
        'Raf' : 'A2'
    }
}

print("""
1.) Kitap almak istiyorum = 1
2.) Kitap eklemek istiyorum = 2
3.) Kitap listesini görmek istiyorum = 3
""")

while True:
    islem = input("Yapmak istediğiniz işlemi seçin = ")

    if (islem == '1'):
        kitapCik = input('Almak istediğiniz kitap ismini girin : ')
        if (kitapCik not in roman):
            print('Bu kitap veritabanınızda yoktur.')
        else:
            KucukKitapCik = kitapCik.islower()
            alinanKitap = roman[kitapCik]
            print('----------Almak istediğiniz kitap bilgileri----------')
            for i in alinanKitap:
                print(i + ' : ' + alinanKitap[i])
            print('Almak istiyorsanız (e) vazgeçmek istiyoranız (h) basın:')
            karar = str(input('İşlem seçin : '))
            cikildi  = roman.pop(kitapCik)
            print("-----KÜTÜPHANEDE KALAN KİTAPLAR-----")
        print(f"-----Kütüphanede olan kitaplar-----\n{roman}")
    elif (islem == '2'):
        kitapEkle = input("Kitap ismini girin : ")
        KucukKitapEkle = kitapEkle.islower()
        yazarismi = input("Yazar ismi giriniz :  ")
        YazarEkleKucuk = yazarismi.islower()
        basimYili = input("Basım yılı girin : ")
        raf = input("Koymak istediğiniz rafı girin : ")
        RafEkleBuyuk = raf.isupper()

        ekle = roman[kitapEkle] = {
            'Yazar İsmi' : yazarismi,
            'Basım Yılı' : basimYili,
            'raf ' : raf
        }
    elif (islem == '3'):
        print("""
        ---------- KÜTÜPHANEDEKİ TÜM KİTAPLAR ----------
        """)
        print(roman)
