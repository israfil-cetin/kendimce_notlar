

"""
Selam

Normade class yazmadan önce variable ve function adında kullandığımız özelliklerimiz vardı.
Neydi bir variable?
variable (Değişken): Adı üstünde atadığımız veriyi değiştirebiliyoruz. İstediğimiz tipte veriyi saklayabiliyoruz.
Neydi bir function?
function (Fonkisiyon): Matematikdeki fonksiyona benzer bir fonksiyon Girdi veriyoruz bize bir sıra işlem yapıyor ve
bir sonuç döndürüyor.

Peki Class'larda variable ve function nasıl çalışıyor?

"""
class NumberOneClass:
    var1 = 10 # Burada bir variable oluşturduk. Artık bunun adı "Attribute"


"""

Bu class attribute'ı artık bu class'a ait bir attribute.
Nasıl yani?
var1 attribute'u NumberOneClass'ı nesneleri için global bir değişkenmiş gibi çalışacaktır.

"""
a = NumberOneClass
a.var1 += 1
print(a.var1)  # 11 çıktısını aldık

b = NumberOneClass
b.var1 += 1
print(b.var1) # 12 çıktısını aldık.

"""
Gördüğünüz gibi farklı nesneler oluşturmuş olsak dahi her nesneden oluşturulduğu classın Attribute'üne erişebiliyor
aynı zamanda da bir yerde değişince diğer nesneler için de bu değer değişmiş oluyor.

Burada oluşturduğumuz var1 adındaki attribute nesnelere özel değil oluşturulduğu sınıfa özel ortak bir attribute'tür.
"""
