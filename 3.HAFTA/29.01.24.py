###DÖNGÜLER####
"""
Döngü Nedir ?

1-)Birden fazla kez tekrar etmesi gereken kod bloklarını istenilen tekrar sayısı kadar çalıştıran yapılardır.

2-)Herhangi bir koleksiyon yapısı(dizi,liste,sözlük,tuple) içerisindeki elemanlara erişebilmek için kullanılabilir.


Döngü Türleri;

1-While
bir koşula bağlı olarak çalışır.

while koşul:
    koşul true cevabını döndürüğü sürece bu döngü çalışacak.


2-For

"""

# sayi=2
#
# while sayi<=5:
#    print(sayi)
#    sayi += 1

##2-100 arasındaki sayıları ekrana yazdırın
# baslangic=2
#
# while baslangic<100:
#    baslangic += 1
#    print(baslangic)


##1-100 arasındaki çift ve tek sayıları ekrana yazdırın
"""
bir sayının çift olması sayinin 2 ye tam bölünmesiyle anlaşılır.
10 % 2 == 0 ise bu sayı çifttir. 
değilse
tektir.
"""
# sayi=1
#
# while sayi<=100:
#     if sayi%2==0:
#         print(f"Sayı çifttir:{sayi}")
#     else:
#         print(f"Sayı Tektir {sayi}")
#     sayi+=1


# sayi1=10
# sayi2=20
#
# print("Sayi1:",sayi1,"Sayi2:",sayi2)
# print(f"Sayi1 : {sayi1+10} Sayi2: {sayi2+20}")
#
# sayi1+=10  # sayi1 = sayi1 +10
# print(sayi1)


##Başlangıç ve bitiş değerlerinin kullanıcıdan alınarak belirlendiği bir while döngüsü tasarlayın

baslangic=int(input("Başlangıç Değeri"))
bitis=int(input("Bitiş Değeri"))
#1.YÖNTEM
# if baslangic>bitis:
#     baslangic,bitis=bitis,baslangic
#     while baslangic<=bitis:
#         print(baslangic)
#         baslangic+=1
# else:
#     while baslangic<=bitis:
#         print(baslangic)
#         baslangic+=1

#2.YÖNTEM
# if baslangic>bitis:
#     while baslangic>=bitis:
#         print(bitis)
#         bitis+=1
# else:
#     while baslangic<=bitis:
#         print(baslangic)
#         baslangic+=1
#3.YÖNTEM
# if baslangic>bitis:
#     while bitis<=baslangic:
#         print(baslangic)
#         baslangic-=1
# else:
#     while baslangic<=bitis:
#         print(baslangic)
#         baslangic+=1

##Birden fazla değişkene değer atama ve Değişken değeri switch etme
# sayi1,sayi2,sayi3 = 100,23,56
# print(f"Sayi1:{sayi1} Sayi2:{sayi2} Sayi3:{sayi3}")
# print(sayi2)
# sayi2,sayi1,sayi3=sayi3,sayi2,sayi1
#
# print(sayi2)
# print(f"Sayi1:{sayi1} Sayi2:{sayi2} Sayi3:{sayi3}")

##Eğer pythonda bu özellik sağlanmasaydı nasıl bir yol izlenmesi gerekirdi.
# sayi1=20
# sayi2=30
# sayi3=0
# print(f"Sayi1:{sayi1} Sayi2:{sayi2}")
# sayi3=sayi1 ##Artık sayi3 içinde sayi1 var 20
# sayi1=sayi2 ## Artık sayi1 de sayi2 değeri var 30
# sayi2=sayi3
# print(f"Sayi1:{sayi1} Sayi2:{sayi2}")
#
# #sayi1,sayi2=sayi2,sayi1






