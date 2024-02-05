#####OPERATORLER#####

"""ATAMA OPERATORU

Değişkenşlere veri atamaya yarar.

    değişken_ismi    =   veri

    sağda bulunan veriyi ismi tanımlanmış olan değişkenin içine atar.

    sayı = 10


"""

# sayi = 20
#
# sayi=40
#
# print(sayi)




###ARITMETIK OPERATORLER###

"""
+ , - , * , /(ondalıklı böler) , //(int böler) , %  

"""

# sayi1=100
# sayi2=50
#
# print(sayi1+sayi2)
# print(sayi1-sayi2)
# print(sayi1*sayi2)
# print(type(sayi1/sayi2))
# print(type(sayi1//sayi2))
# print(sayi1%sayi2)

###ATAMALI İŞLEM OPERATÖRLERİ###

# sayi1=50
# sayi2=60
#
# print(sayi1)
# Diğer bütünü işlemler içinde aynı yöntem kullanılır.
# sayi1 = sayi1 + 10
# #sayi1+=10
#
# print(sayi1)

##Karşılaştırma Operatörleri
"""
>(büyük mü?) , <(küçük mü?) , >=(büyük veya eşit mi?) , <=(küçük veya eşit mi?)  , == (eşit mi?) , != (eşit değil mi?)

"""

# sayi1=50
# sayi2=20
#
# print(sayi1>sayi2)
# print(sayi1<sayi2)
# print(sayi1>=sayi2)
# print(sayi1<=sayi2)
# print(sayi1==sayi2)
# print(sayi1!=sayi2)



"""
KULLANICIDAN VERİ ALMA (INPUT) İFADESİ

degisken_ismi=input("Kullanıcıya_veri_girerken_gösterilcek_mesaj")

NOT:input ile okunan bütün veriler çevirme yapılmazsa string olarak okunur.

"""


# isim=input("Lütfen isminizi giriniz:")
# print(type(isim))

# isim=input("Ad:")
# soyad=input("Soyad:")
#
# print(isim+soyad)

# yas1=input("Yaş1:")
# yas2=input("Yaş2:")
#
# print(yas1+yas2)

##BOXING ile girilen değeri veri tipini int'e çevirme

# yas1=input("Yaş1:")
# yas1=int(yas1)
#
# yas2=int(input("Yaş2:"))
#
# print(yas1+yas2)

#Kullanıcının girmiş olduğu 2 yaş değerinin toplamını 10 ile çarp

# sayi1=int(input("Sayi1:"))
# sayi2=int(input("Sayi2:"))
#
# sonuc=sayi1+sayi2
#
# print(sonuc*10)
# print((sayi1+sayi2)*10)

##VERİ TİPİ DÖNÜŞÜMLERİ##

###String to int sadece rakamsal ifadelerde olur
# deger=int(input("Değer giriniz:"))

###INT TO STR
# sayi=20
# print(type(sayi))
# sayi=str(sayi)
# print(type(sayi))

##INT TO FLOAT
# sayi=20
# print(type(sayi))
# sayi=float(sayi)
# print(sayi)
# print(type(sayi))

##FLOAT TO STR
# kilo=70.9
# kilo=str(kilo)
# print(type(kilo))

##FLOAT TO INT
# kilo=70.9
# # kilo=int(kilo)
# # print(type(kilo))
# # print(kilo)

#POW ifadesi ile herhangi bir sayının üssünü alabilirsiniz.
#pow(üssü_alınacak_sayı,üs)
# yas1=20
# yas2=30
# print(pow(yas1+yas2,30))


"""
MANTIKSAL OPERATÖRLER

and or

and bağlacı iki koşulunda doğru olması gerektiği durumdur.
T=>1 F=>0 
and bağlacında iki önerme arasında çarpma işlemi bulunur.
2^N ile toplam sonuç sayısı ortaya çıkar 
kullanıcı adı    and     şifre      sonuç
      T 1         *      F 0          F0
      T                  T            T 1
      F                  T            F
      F                  F            F 

OR
veya önermeler arasında toplama işlemi vardır
T=>1 F=>0
((Eposta/kullanıcı adı/Telefon)    and     şifre)      sonuç
   T         F           F                    T          T
   T         F           F                    F          F
   F         T           F                    T          T
   F         T           F                    F          F
   F         F           T                    T          T
   F         F           T                    F          F
"""

##ÖRNEK:Kullanıcıdan alınan kullanıcıadı ve şifre bilgisini tanımlamış olduğunuz değişkenlerle kontrol ettirerek cevabı gösteriniz.

email="trk"
tel="555"
ka="t"
sfr="1"

veri=input("Kullanıcı adı/Eposta/Telefon")
sifre=input("Şifre:")

print((veri==ka or veri==tel or veri==email) and sifre==sfr)

print("")

print("")






















