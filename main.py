### Module Description ###
import time
## İNPUT BÖLÜMÜ SAYILAR
sayi1=int(input('Enter Your Number = '))
sayi2=int(input('Enter Your Number = '))
sayi3=int(input('Enter Your Number = '))
sayi4=int(input('Enter Your Number = '))
time.sleep(1)
print('Action to be taken: Subtraction')

#######   EQUALITY CONTROL SECTION   ######
    
if sayi1==sayi2 or  sayi1==sayi3 or  sayi1==sayi4 or sayi2==sayi3 or sayi2==sayi4 or sayi3==sayi4:
    time.sleep(1)
    print('Checking the Numbers ...')
    time.sleep(3)
    print('The numbers must not be equal, please re-enter the numbers!')


#######   THE RATIOS OF SAYİ1   #######
elif sayi1>sayi2 and sayi1>sayi3 and sayi1>sayi4:
    time.sleep(2)
    print('Checking the Numbers ...')
    time.sleep(3)
    print('En Büyük Sayı ', sayi1)
    if sayi2<sayi3 and sayi2<sayi4:
        print('En Küçük Sayı ', sayi2)
        time.sleep(1.5)
        print('Fark : ',sayi1-sayi2)
    if sayi3<sayi2 and sayi3<sayi4:
        print('En Küçük Sayı ', sayi3)
        time.sleep(1.5)
        print('Fark : ',sayi1-sayi3)
    if sayi4<sayi2 and sayi4<sayi3:
        print('En Küçük Sayı ', sayi4)
        time.sleep(1.5)
        print('Fark : ',sayi1-sayi4)



#######   THE RATIOS OF SAYİ2   #######
elif sayi2>sayi1 and sayi2>sayi3 and sayi2>sayi4:
    time.sleep(2)
    print('Checking the Numbers ...')
    time.sleep(3)
    print('En Büyük sayı ', sayi2)
    if sayi1<sayi3 and sayi1<sayi4:
        print('En Küçük Sayı ', sayi1)
        time.sleep(1.5)
        print('Fark : ',sayi2-sayi1)
    if sayi3<sayi1 and sayi3<sayi4:
        print('En Küçük Sayı ', sayi3)
        time.sleep(1.5)
        print('Fark : ',sayi2-sayi3)
    if sayi4<sayi3 and sayi4<sayi1:
        print('En Küçük Sayı ', sayi4)
        time.sleep(1.5)
        print('Fark : ',sayi2-sayi4)



#######   THE RATIOS OF SAYİ3  #######
elif sayi3>sayi1 and sayi3>sayi2 and sayi3>sayi4:
    time.sleep(2)
    print('Sayılar Kontrol Ediliyor ...')
    time.sleep(3)
    print('En Büyük Sayı ', sayi3)
    if sayi1<sayi2 and sayi1<sayi4:
        print('En Küçük Sayı', sayi1)
        time.sleep(1.5)
        print('Fark : ',sayi3-sayi1)
    if sayi2<sayi1 and sayi2<sayi4:
        print('En Küçük Sayı', sayi2)
        time.sleep(1.5)
        print('Fark : ',sayi3-sayi3)
    if sayi4<sayi1 and sayi4<sayi2:
        print('En Küçük Sayı', sayi4)
        time.sleep(1.5)
        print('Fark : ',sayi3-sayi4)


#######   THE RATIOS OF SAYİ 4  #######
elif sayi4>sayi1 and sayi4>sayi2 and sayi4>sayi3:
    time.sleep(2)
    print('Sayılar Kontrol Ediliyor ...')
    time.sleep(3)
    print('En Büyük Sayı ', sayi4)
    if sayi1<sayi2 and sayi1<sayi3:
        print('En Küçük Sayı', sayi1)
        time.sleep(1.5)
        print('Fark : ',sayi4-sayi1)
    if sayi2<sayi1 and sayi2<sayi3:
        print('En Küçük Sayı', sayi2)
        time.sleep(1.5)
        print('Fark : ',sayi4-sayi2)
    if sayi3<sayi1 and sayi3<sayi2:
        print('En Küçük Sayı', sayi3)
        time.sleep(1.5)
        print('Fark : ',sayi4-sayi3)

 











