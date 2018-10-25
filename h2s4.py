#Bir araba kiralama firması, bir haftaya kadar olan kiralamalar için 65 tl almaktadır.
#  Bir haftayı geçen sürelerde ise %16 iskonto uygulamaktadır.
# Kılavye yolu ile alınan gün cinsinden araba kiralama süresini kullanarak müşterinin ödemesi gereken tutarı hesaplayan programı
gun=int(input('kaç gün kiralayacaksınız'))
if gun<=7:
    print("ücret 65 tl")
elif gun>7:
    fark=gun-7
    ucret=fark*(65+(65*1.6))
    print('ucret:',ucret)