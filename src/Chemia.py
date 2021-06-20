import math
print('WYBIERZ CO MASZ DANE >>> ')
print('---------------------------')
print('|  1 - WZÓR SUMARYCZNY    | ')
print('|  2 - STOSUNEK MASOWY    | ')
print('|  3 - MASA CZĄSTECZKOWA  | ')
print('|  4 - SKŁAD PROCENTOWY   |  ')
print('---------------------------')
wybor=int(input('twoj wybor to >> '))
if wybor == 1:

    n=int(input('PODAJ n = '))
    wegiel=12*n
    wodor=2*n+2
    masa=wegiel+wodor
    sklwegiel=round(wegiel/masa,2)*100
    sklwodor=round(wodor/masa,2)*100
    for i in range(2,12*n+1):
        while (wegiel%i==0) and (wodor%i==0):
            wegiel=wegiel/i
            wodor=wodor/i
    print('STOSUNEK MASOWY TO '+str(wegiel)+' : '+str(wodor))
    print('MASA CZĄSTECZKOWA T0 '+str(masa)+' u')
    print('SKŁAD PROCENTOWY TO '+str(sklwegiel)+'%-C  '+str(sklwodor)+'%-H')


if wybor == 2:

    wc=int(input('PODAJ WART WEGLA = '))
    wh=int(input('PODAJ WART WODORU = '))

    wynikn=0
    for i in range(2,12):
        if 6*i*wh==(i+1)*wc:
            wynikn=wynikn+i
    wegiel=12*wynikn
    wodor=2*wynikn+2


    masa=wegiel+wodor
    sklwegiel=round(wegiel/masa,2)*100
    sklwodor=round(wodor/masa,2)*100
    print('WZÓR SUMARYCZNY TO  C('+str(wynikn)+')  H('+str(2*wynikn+2)+')')
    print('MASA CZĄSTECZKOWA T0 '+str(masa)+' u')
    print('SKŁAD PROCENTOWY TO '+str(sklwegiel)+'%-C  '+str(sklwodor)+'%-H')
if wybor == 3:

    unity=int(input('PODAJ MASĘ CZĄSTECZKOWĄ W UNITACH  = '))
    wynikn=0

    for i in range(1,12):
        if 14*i+2==unity:
            wynikn=i
        wegiel=12*wynikn
        wodor=2*wynikn+2
    for i in range(2,12*wynikn+1):
        while (wegiel%i==0) and (wodor%i==0):
            wegiel=wegiel/i
            wodor=wodor/i
    masa=wegiel+wodor
    sklwegiel=round(wegiel/masa,2)*100
    sklwodor=round(wodor/masa,2)*100
    print('WZÓR SUMARYCZNY TO  C('+str(wynikn)+')  H('+str(2*wynikn+2)+')')
    print('STOSUNEK MASOWY TO '+str(wegiel)+' : '+str(wodor))
    print('SKŁAD PROCENTOWY TO '+str(sklwegiel)+'%-C  '+str(sklwodor)+'%-H')
if wybor == 4:

    cp=int(input('PODAJ ZAWARTOŚĆ WEGLA W PROCENTACH( % ) = '))
    hp=int(input('PODAJ ZAWARTOŚĆ WODORU W PROCENTACH( % ) = '))


    for i in range(2,11):
        while (cp%i==0) and (hp%i==0):
            cp=cp/i
            hp=hp/i
    wynikn=0
    for i in range(2,12):
        if 6*i*hp==(i+1)*cp:
            wynikn=wynikn+i
    wegiel=12*wynikn
    wodor=2*wynikn+2
    masa=wegiel+wodor
    print('WZÓR SUMARYCZNY TO  C('+str(wynikn)+')  H('+str(2*wynikn+2)+')')
    print('MASA CZĄSTECZKOWA T0 '+str(masa)+' u')
    print('STOSUNEK MASOWY TO '+str(cp)+' : '+str(hp))   