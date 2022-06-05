print("********************\nATM SİSTEMİNE HOŞGELDİNİZ\n********************")

print("""
İŞLEMLER:
1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Çıkış için '0'tuşuna basınız.
""")

bakiye = 1000

while True:
    islem = int(input('Lütfen işlem seçiniz : '))

    if (islem == 0):
        print('Güle Güle :)')
        break
    elif (islem == 1):
         print(f"Bakiyeniz {bakiye} TL")
    elif (islem == 2):
        yatirilacak_miktar = int(input("Yatırmak istediğiniz tutarı girin :"))
        bakiye += yatirilacak_miktar
    elif (islem == 3):
        cekilecek_miktar = int(input('Çekmek istediğiniz tutarı girin : '))
        if (bakiye < cekilecek_miktar):
            print("BAKİYENİZ YETERSİZ.")
            print(f"Bakiyeniz {bakiye} TL")
            continue
        bakiye -= cekilecek_miktar
        print(f"Kalan miktar {bakiye} TL")
    else:
        print("LÜTFEN GEÇERLİ BİR İŞLEM GİRİN!")

