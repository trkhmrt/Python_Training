"""DEĞİŞKEN KAVRAMI

Değişken(Variables) Nedir ?

Uygulama içerisinde kullanıcıdan gelen yada herhangi bir işlem sonucu ortaya çıkan veriyi saklayan temel yapılardır.

isim="TARIK"
yas=27

Değişken İsmi Tanımlama Kuralları Nelerdir ?

Yanlış :
1yas Rakamla başlayamaz.
_ alt tre hariç hiçbir özel karkter kullanılamaz.
İki kelimeden oluşuyorsa arada boşluk olamaz Isim Soyisim

Doğru:
yas1 rakamla bitebilir.
Sadece _ ifadesi kullanılabilir _yas  yas_   isim_soyisim

Değişken ismi tanımlama tarzı ;

isimSoyisim  => camelCase

isim_soyisim => snake_case

isimsoyisim => lowercase

ISIMSOYISIM => UPPERCASE

IsimSoyisim => PascalCase
"""


"""
Veri Tipleri

METİNSEL VERİ TİPİ

character (char) => 'a'  'b'  'c'

string (str) => Her bir karakterin bir araya gelip karakter dizisi oluşturmasıyla string yapıları ortaya çıkar.

adres="Mecidiyeköy Şişli"

SAYISAL VERİ TİPİ

int => Tam sayı verileri saklar(Negatif ve Pozitif Sonsuz).  10 , 20 , 30 , 40 

float => Ondalıklı sayıları saklar.(Negatif ve Pozitif sonsuz)  -20.1  -19.56


MANTIKSAL VERİ TİPİ

boolean(bool)=> true ve false saklar sadece 

"""

#DEĞİŞKENLERİN VERİ TİPİNİ ÖĞRENME YÖNTEMİ

# isim="Tarık"
# print("İsim değişkeninin veri tipi:",type(isim))
# yas=27
# print("Yas değişkeninin veri tipi:",type(yas))
# kilo=70.5
# print("Kilo değişkeninin veri tipi:",type(kilo))
# boy=1.85
# print("Boy değişkeninin veri tipi:",type(boy))
# evlilikDurumu=False
# print("EvlilikDurumu değişkeninin veri tipi:",type(evlilikDurumu))


#PRINT İLE EKRANA YAZDIRMA TİPLERİ

#1.Yöntem
# isim="Mevlüt"
# yas=20
# kilo=100
# boy=1.90
# print("İsminiz:",isim,"Yaşınız:",yas,"Kilonuz:",kilo,"Boyunuz:",boy)

#2.Yöntem
# isim="Mevlüt"
# yas=20
# kilo=100
# boy=1.90
# print(f"İsminiz:{isim} Yaşınız:{yas}  Kilonuz:{kilo}  Boyunuz:{boy} ")



###String KAÇIŞ(STRING ESCAPE) ifadeleri
#\n kendinsen sonraki karakterleri bir alt satıra geçirir
# isim="Mevlüt"
# yas=20
# kilo=100
# boy=1.91
# #Eğer ondalıklı sayının virgülden sonra istenilen basamak sayısını ekrana yazdırmak için :.adetf kullanılır.
# print(f"İsminiz:{isim}\nYaşınız:{yas}\nKilonuz:{kilo}\nBoyunuz:{boy:.1f} ")


#\t kendinden sonraki karakterle arasında boşluk bırakır.
#print("Merhaba Dünya\t\tBurası mecidiyeköy\tBurdan çıkış yok")


#End
#print ifadesinde her mesajın sonunda default olarak \n vardır.Biz end ile birlikte string ifadenin sonuna ne geleceğini belirlemiş oluruz.Cümle bitimine end ile birlikte verilen karakterler yerleştirilir.
#Default olarak \n vardır.
#
# print("Merhaba Dünya Burası mecidiyeköy Burdan çıkış yok",end="-------\n")
# print("Merhaba Dünya Burası mecidiyeköy Burdan çıkış yok")

#Sep
print("Merhaba Dünya","Burası mecidiyeköy","Burdan çıkış yok",sep="\n")










