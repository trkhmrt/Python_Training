"""
if koşulu yazarken indentation'a dikkat edilmeli.

IF-ELIF-ELSE

uygulama içerisinde ortaya çıkan ve değişen koşullara göre kodun akış yönünü değiştirmeye yarayan karar yapılarıdır.

if koşul:
    Eğer koşul cevap olarak true dönerse if' in içindeki kodlar çalışır.
elif:
    koşul ifadesi false dönerse varsa alternatif şarta yönlendirme yapılır.Alternatif şartların her biride false dönerse o zaman ;
else:
    varsa/yazıldıysa else gider.


if ve else birkez elif sonsuz kez tanımlanabilir.

"""
# yas=19
# if yas>18:
#     print("Yaşınız 18 den büyüktür")
# elif yas==18:
#     print("Yaş 18 dir.")
# else:
#     print("18 den küçüktür")

##Kullanıcıdan alınan sayının negatif pozitif yada sıfıra eşit olma durumlarını kontrol ettiriniz.Ve herbir durum için ekrana ilgili durumu içeren mesajı yazdırınız.

# sayi=int(input("Sayi giriniz"))
#
# if sayi>0:
#     print("Sayı sıfırdan büyük")
# elif sayi==0:
#     print("Sayi sifira eşittir")
# else:
#     print("Sıfırdan küçüktür")

##Girilen not ortalamasına göre eğer 49 a eşitse kaldı 49 dan büyükse geçti şeklinde ekrana çıktı verin

# puan=50
# if puan>=50:
#     print("Sınıfı Geçti")
# elif puan<=49:
#     print("Sınıfta kaldı")


"""
Ortalamaya göre;
0-49 arası ise => sınıfta kaldı;
50-79 arası ise => sınıfı teşekkürle geçti
80-100 arası ise => sınıfı takdirle geçti,

0'dan küçük ve 100'den büyük olma durumlarını lütfen kontrol ettirip kullanıcının uygun aralıkta değer girmesi gerektiği mesajını iletin.
"""

# ortalama=int(input("Ortalama giriniz:"))
#
# if ortalama<0 or ortalama>100:
#     print("Hatalı not aralığı")
# else:
#     if ortalama>=0 and ortalama<=49:
#         print("Kaldınız")
#     elif ortalama>=50 and ortalama<=79:
#         print("Teşekkürler Geçtiniz")
#     elif ortalama>=80 and ortalama<=100:
#         print("Takdirle Geçtiniz")


"""
Kullanıcıdan çocuk sayısını alınız.
Çocuk sayısı <=3 ise;
Maaş += çocuk sayısı * 200 TL
Çocuk sayisi > 3 
Maaş += Çocuk sayısı * 400 TL

Çocuk sayısı için negatif sayı girilmesin.
Maaş: 17002  
"""
cocuk_sayisi=int(input("Çocuk Sayısını Giriniz"))
maas=17002

# if cocuk_sayisi>=0 and cocuk_sayisi<=3:
#     print(f"Guncel Maaşınız:{maas+(cocuk_sayisi*200)}")
# elif cocuk_sayisi<0:
#     print("Lütfen geçerli bir değer giriniz")
# else:
#     print(f"Guncel Maaşınız:{maas+(cocuk_sayisi*400)}")

# if not cocuk_sayisi<0:
#    if cocuk_sayisi > 3:
#     print(f"Guncel Maaşınız:{maas + (cocuk_sayisi * 400)}")
#    else:
#        print(f"Guncel Maaşınız:{maas + (cocuk_sayisi * 200)}")
# else:
#     print("Lütfen geçerli bir değer giriniz")


if 0<=cocuk_sayisi<=3:
    print(f"Guncel Maaşınız:{maas+(cocuk_sayisi*200)}")
elif cocuk_sayisi<0:
    print("Lütfen geçerli bir değer giriniz")
else:
    print(f"Guncel Maaşınız:{maas+(cocuk_sayisi*400)}")