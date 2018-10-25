#Haftalık 10 saat derse girmek zorunda olan öğretim üyeleri,
# bu zorunlu ders yükü dolduktan sonra ek ders ücreti almaktadır.
# Bu ek derslerin sayıyısı 20 yi aşamamaktadır. Öğretim üyeleri her bir saatlik ek ders başına 8TL almaktadır.
#  Kullanıcıdan aylık ders saatini alıp ekders ücretini hesaplayan programı

saat=int(input('kaç saat ek ders alıyorsunuz'))
if  saat==40:
    print("sabit ücrete tabi tutulmuştur")
elif  saat>40:
      ucret=((saat-40)*8)
      print("ücret:",ucret)