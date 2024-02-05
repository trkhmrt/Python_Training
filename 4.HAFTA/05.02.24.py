

###FOR DÖNGÜSÜ###
"""
for i in range(çalışma_aralığı):
    döngü şartları içerisinde çalıştırılacak kodlar buraya yazılır.


"""
#0 dan başla 3 e kadar çalış 3 dahil değil
# for i in range(3):
#     print("MERHABA")
#     print(i)


#Başlangıç-Bitiş değeri verilmesi (Son değer dahil değil)
# for i in range(3,10):
#     print("MERHABA")
#     print(i)
#


# for indeks_numarasi in range(7):
#     print(f"MERHABA:{indeks_numarasi}")



# for indeks_numarasi in range(0,10,2):
#     print(f"MERHABA:{indeks_numarasi}")

#for indeks_numarasi in range(0,10,2):
#     print(f"MERHABA:{indeks_numarasi}")


#for i in range(10,0,-1):
    #print(i)

#For döngüsü ile 0-100 arasındaki çift sayıları bulun.

# for i in range(0,100):
#     if i%2==0:
#         print(i,"Çift sayidir.")


#for döngüsü ile 0 dan 10 a kadar olan sayıların karesini alınız.
# for i in range(0,10):
#     #print(i*i)
#     #print(pow(i,2))
#     print(i**2)


#Başlangıç ve bitiş değerlerini kullanıcıdan alınan bir for döngüsü yazınız.Eğer başlşangıç bitişten büyükse döngüyü bir şekilde çalıştırın.

baslangic=int(input("Başlangıç Değeri giriniz."))
bitis=int(input("Bitiş değeri giriniz."))

if baslangic>bitis:
    for i in range(baslangic,bitis,-1):
        print(i)
else:
    for i in range(baslangic,bitis):
        print(i)
       

