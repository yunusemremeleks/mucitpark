#Kullanıcıdan bir üçgenin üç kenarının boyutlarını alıp, üçgen çeşidini ekrana basan programı 
a=int(input('üçgenin birinci kenarını giriniz'))
b=int(input('üçgenin ikinci kenarını giriniz'))
c=int(input('üçgenin üçüncü kenarını giriniz'))
if a==b==c:
    print('eşkenar üçgendir')
elif a==b or a==c or b==c:
    print('ikizkenar üçgendir')
else:
    print('çeşitkenar üçgendir')