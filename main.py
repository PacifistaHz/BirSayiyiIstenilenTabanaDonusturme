from random import sample


def tabanDonusum(sayi, taban):
    try:
        sayi=int(sayi)
        taban=int(taban)
        basamak, sonuc, us = 0, 0, 1
        while sayi>=1:
            basamak = sayi%taban
            sayi = int(sayi/taban)
            sonuc+=basamak * us
            us = us * 10
        return sonuc
    except Exception as e:
        return e

sayi=input("Sayıyı giriniz: ")
taban=input("Dönüştürülecek tabanı giriniz: ")
sonuc=tabanDonusum(sayi,taban)
print(sonuc)