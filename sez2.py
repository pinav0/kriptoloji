def duzeltilmis_turkce_karakterleri(metin):
    turkce_harfler = "çÇğĞıİöÖşŞüÜ"
    ingilizce_harfler = "cCgGiIoOsSuU"
    ceviri_tablosu = str.maketrans(turkce_harfler, ingilizce_harfler)
    duzeltilmis_metin = metin.translate(ceviri_tablosu)
    return duzeltilmis_metin

def cezar_sifrele(metin):
    duzeltilmis_metin = duzeltilmis_turkce_karakterleri(metin)
    sifreli_metin = ""
    kaydirma_listesi = [2, -2, 2, -2]  # Her karakter için kaydırma

    for indis, karakter in enumerate(duzeltilmis_metin):
        if karakter.isalpha():
            alfabe = 'abcdefghijklmnopqrstuvwxyz' if karakter.islower() else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            karakter_indis = alfabe.index(karakter)
            kaydirma = kaydirma_listesi[indis % 4]
            yeni_indis = (karakter_indis + kaydirma) % 26
            sifrelenmis_karakter = alfabe[yeni_indis]
            sifreli_metin += sifrelenmis_karakter
        elif karakter.isdigit():
            rakam = int(karakter)
            kaydirma = kaydirma_listesi[indis % 4]
            yeni_rakam = (rakam + kaydirma) % 10
            sifreli_metin += str(yeni_rakam)
        else:
            sifreli_metin += karakter

    return sifreli_metin

def cezar_coz(metin):
    duzeltilmis_metin = duzeltilmis_turkce_karakterleri(metin)
    cozulmus_metin = ""
    kaydirma_listesi = [-2, 2, -2, 2]  # Şifrelenmiş her karakter için ters kaydırma

    for indis, karakter in enumerate(duzeltilmis_metin):
        if karakter.isalpha():
            alfabe = 'abcdefghijklmnopqrstuvwxyz' if karakter.islower() else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            karakter_indis = alfabe.index(karakter)
            kaydirma = kaydirma_listesi[indis % 4]
            yeni_indis = (karakter_indis + kaydirma) % 26
            cozulmus_karakter = alfabe[yeni_indis]
            cozulmus_metin += cozulmus_karakter
        elif karakter.isdigit():
            rakam = int(karakter)
            kaydirma = kaydirma_listesi[indis % 4]
            yeni_rakam = (rakam + kaydirma) % 10
            cozulmus_metin += str(yeni_rakam)
        else:
            cozulmus_metin += karakter

    return cozulmus_metin

# Örnek kullanım
metin = "abcd efgh"
sifrelenmis_metin = cezar_sifrele(metin)
print("Şifrelenmiş Metin:", sifrelenmis_metin)

cozulmus_metin = cezar_coz(sifrelenmis_metin)
print("Çözülmüş Metin:", cozulmus_metin)
