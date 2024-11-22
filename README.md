# ÇOKLU VERİ ELEMANLARI

Tek bir değişkende birden fazla farklı türde ya da aynı türde veri depolamamızı sağlar.


Başlıcaları:


1-Listeleme


2-Diziler


3-Demetler


4-Sözlükler


# LİSTE KAVRAMI


Köşeli parantezle oluşur.


Verileri tanımladıktan sonra liste elemanlarına ulaşmak için indeks kullanılır.


Liste elemanlarına ulaşmak için virgül kullanılır.


Listelere bazı işlemler yapılabilir.


EKLEME:
liste[1,2,3,4,5]
liste+=["gorkem".32]


BİRLEŞTİRME:
a=[10,20,30]
b=[1,2,3,]








# İNDEKS KAVRAMI
Çoklu verilerdeki her bir elemanın konumu indeks ile temsil edilir. İndeks her daim 0 dan başlar ve toplam eleman sayısının bir eksiği kadardır.
a=[1,2,3,4,]
print(a[3]) # 3 çıktısını verir


# DİLİMLEME YAPISI 
Özel aralıklarla çoklu verilen elemanlara ulaşmamızı sağlar.Başlangıç indeksi dahildir , bitiş indeksi dahil değildir.
p=[0,0,0,1,1,1,0,0]
dilim(3:6]

# ARTIŞ MİKTARI
çoklu  verideki artış miktarına göre alınmak isteyen verileri almak için kullanılan yöntem
kullanımı:


liste=[baslangic:bitis:artis_miktari]



# DEMET KAVRAMI
Listeler gibi çoklu veri depolamamızı sağlar.



Değişmeyen veriler tanımlanır.(Elemanları değişmez)



Parantez kullanılır.



Elamanlara ulaşmak için indeks kullanılır.



# SÖZLÜK KAVRAMI
Anahtar-Değer ilişkisine göre yapı oluşturmamızı sağlayan yapılardır.


Süslü parantez kullanılır.


Değer herhangi bir türden olabilir


Anahtarla değer arasına ":" konur.


Sözlük anahtarına ulaşma:


a={"username":"eralp","password":"12345"

print(a["username"]) # eralp çıktısını verir.


Değiştirme:

a["password"]="54321"

print(a) # {'username': 'ellap', 'password': '54321'} çıktısını verir
