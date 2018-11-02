#Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulan programı

sayı = int(input("Sayı giriniz"))
i = 1
toplam = 0
while (i < sayı):
    if (sayı % i == 0):
        toplam += i
    i += 1
if (toplam == sayı):
    print(sayı, "mükemmel bir sayıdır.")
else:
    print(sayı, "mükemmel bir sayı değildir.")