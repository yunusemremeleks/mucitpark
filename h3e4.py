#Kullanıcın girdiği sayının faktöriyelini hesaplayan ve bunu ekranda gösteren program
x=int(input('bir sayı giriniz'))

carp=1
for oku in range(x):
    carp=carp*(oku+1)
    print(oku+1,'faktöriyel:',carp)