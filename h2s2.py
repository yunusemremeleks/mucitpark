#Kullanıcıdan alınan iki sayının (pay ve payda) oranını hesaplayan programı
#Payda sıfır girilirse ekrana 'Sıfıra bölüm hatası var ' yazınız.
a=int(input("pay değerini yazınız"))
b=int(input("payda değerini giriniz"))
if b !=0:
    x=a/b
    print('sonuç::',x)
elif b==0:
    print('sıfır hatası var')