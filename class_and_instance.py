

"""
Selam

Normade class yazmadan önce variable ve function adında kullandığımız özelliklerimiz vardı.
Neydi bir variable?
variable (Değişken): Adı üstünde atadığımız veriyi değiştirebiliyoruz. İstediğimiz tipte veriyi saklayabiliyoruz.
Neydi bir function?
function (Fonkisiyon): Matematikteki  fonksiyona benzer bir fonksiyon Girdi veriyoruz bize bir sıra işlem yapıyor ve
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
a_nesnesi = NumberOneClass
a_nesnesi.var1 += 1
print(a_nesnesi.var1)  # 11 çıktısını aldık

b_nesnesi = NumberOneClass
b_nesnesi.var1 += 1
print(b_nesnesi.var1) # 12 çıktısını aldık.

# Hatta bir nesne oluşturmadan da kullanabiliyoruz.
NumberOneClass.var1 += 5
print(NumberOneClass.var1) # 17 çıktısını altık

"""
Gördüğünüz gibi farklı nesneler oluşturmuş olsak dahi her nesneden oluşturulduğu classın Attribute'üne erişebiliyor
aynı zamanda da bir yerde değişince diğer nesneler için de bu değer değişmiş oluyor.

Burada oluşturduğumuz var1 adındaki attribute nesnelere özel değil oluşturulduğu sınıfa özel ortak bir attribute'tür.

Peki fonksiyonlar nasıl çalışıyor?
"""

class NumberTwoClass:
    test = 10
    def func1(): return 10

c_nesnesi = NumberTwoClass
print(c_nesnesi.func1()) # 10 çıktısını alıyoruz.

"""
Evet burada NumberTwoClass'ına ait bir fonksiyon oluşturduk ve oluşturduğumuz nesneden buna eriştik. 
Buna da class metodu diyeceğiz fakat Class attribute'u bu oluşturduğumuz metotdan erişemiyor kullanamıyoruz.

Peki ne yapacağız?

Bir Class attribute'u değerleri tutmada işer yarıyor olsa da bu ortak değer tutma işini pek yapmıyoruz. 
Ya da en azından ben yapmıyorum. Ama en azından attribute düzgün çalışıyor gibi duruyordu neden class metodu çalışmadı 
ya da başka bir yol mu var? Evet burayı unutmayalım bu konuya geri döneceğim. 
Şimdi biraz Classlardan ve nesnelerden bahsedelim.

Class'lar bir şablon gibidir. Bir şablonun birçok örneğini çıkarırız. Örneklere instance deniyor.
Yukarıda a_nesnesi olarak oluşturduğumuz bu değişkene bir class atayınca 
o atandığı class'ın bir instance'ı (örneği) olmuş oldu.

Peki ne farkı var bu nesnelerin?

Classların bir attributu vardı demi. Bu attribute ortak bir değişken gibi davranıyordu. Artık classlardan oluşturduğumuz
nesnelerimiz var. Bu nesnelerin kendine ait attribute'ları olacaktır. Sadece kendine özel. Şimdi başka bir class yazalım.

"""
class NumberThreeClass:
    def __init__(self):
        pass
# d_nesnesi bir instance. Atanan bir class

d_nesnesi = NumberThreeClass()

"""
Şimdi bazı sorular var.

S1- Nedir bu __init__ metodu?
S2- __ bu ne demek?
S3- Nedir bu self değişkeni?
S4- Nedir bu NumberThreeClass()'ın yanındaki parantez?

C1- __init__ init, initialize'ın kısalmasıdır. initialize çevrildiği gibi bir başlatma metodu, 
bir constructor (yapıcı) metottur. Nesne ilk oluşturulduğunda çalışan metottur.

C2- Magic ya da dunder metodu nedir. Bazı özel amaçlar için kullanırız. Şimdilik böyle açıklayayım.

C3- Self oluşturduğumuz nesnedir aslında. Self yazdığına bakmayın, bir gelenek olduğu için "self" yazılmıştır. 
İstenilirse değiştirebilir. Self kavramını yazarken açıklayacağım.

C4- d_nesnesi = NumberThreeClass() <--bu parantez init metodunun kendisidir. ilk önce init metodu çalıştığını söylemiştik.

"""