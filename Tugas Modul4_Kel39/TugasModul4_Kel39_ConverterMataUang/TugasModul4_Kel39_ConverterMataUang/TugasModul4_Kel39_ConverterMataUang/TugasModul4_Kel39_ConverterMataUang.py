import os;
import time

def awal():
    os.system('cls');
    print('Program Converter Mata Uang')
    print("Disusun oleh : ")
    print('1.Farrel Ahmad Yudithia - 21120119130067\n2.Mohamad Iqbal Amrullah - 21120119140136\n')
    x=int(input('tekan [0] untuk memulai program\n'))
    if x == 0:
        pilihan1()
    while x != 0:
        print('\ninvalid number! please insert the correct number')
        time.sleep(1)
        awal()

def pilihan1():
    os.system('cls');
    print('Kemana anda akan menukar uang ?')
    print('1. Rupiah ke Asing\n2. Asing ke Rupiah\n3. Back\n4. Home')
    p1=int(input('Masukkan pilihan : '))
    while (x > 4 or x < 1) :
        print('\ninvalid number! please insert the correct number')
        time.sleep(1)
        os.system('cls');
        print('Kemana anda akan menukar uang ?')
        print('1. Rupiah ke Asing\n2. Asing ke Rupiah\n3. Back\n4. Home')
        p1=int(input('Masukkan pilihan : '))
    if p1==1:
        pilihan2()
    elif p1==2:
        pilihan3()
    elif p1==3:
        awal()
    else:
        awal()


def pilihan2():
    os.system('cls');
    print('Pilihan Mata Uang Tujuan:')
    print('1. USD\n2. MYR\n3. EUR\n4. SGD\n5. AUD\n6. Back\n7. Home')
    p2=int(input('Masukkan pilihan : '))

    while x > 7 or x < 1:
         print('\ninvalid number! please insert the correct number')
         time.sleep(1)
         print('Pilihan Mata Uang Tujuan:')
         print('1. USD\n2. MYR\n3. EUR\n4. SGD\n5. AUD\n6. Back\n7. Home')
         p2=int(input('Masukkan pilihan : '))
    if p2==1:
        uang1=float(input('Masukan nominal rupiah = '))
        hasil=uang1/16444
        print(uang1, 'IDR = ', hasil, 'USD')
    elif p2==2:
        uang1=float(input('Masukan nominal rupiah = '))
        hasil=uang1/3815
        print(uang1, 'IDR = ', hasil, 'MYR')
    elif p2== 3:
        uang1=float(input('Masukan nominal rupiah = '))
        hasil=uang1/18146
        print(uang1, 'IDR = ', hasil, 'EUR')
    elif p2==4:
        uang1=float(input('Masukan nominal rupiah = '))
        hasil=uang1/11560
        print(uang1, 'IDR = ', hasil, 'SGd')
    elif p2==5:
        uang1=float(input('Masukan nominal rupiah = '))
        hasil=uang1/10157
        print(uang1, 'IDR = ', hasil, 'AUD')
    elif p2==6:
        pilihan1()
    else:
        awal()
    
    akhir()

def pilihan3():
    os.system('cls');
    print('Pilihan Mata Uang Asal:')
    print('1. USD\n2. MYR\n3. EUR\n4. SGD\n5. AUD\n6. Back\n7. Home')
    p3=int(input('Masukkan pilihan : '))

    while x < 1 or x > 7:
        print('invalid number! Please insert the correct number')
        time.sleep(1)
        os.system('cls');
        print('Pilihan Mata Uang Asal:')
        print('1. USD\n2. MYR\n3. EUR\n4. SGD\n5. AUD\n6. Back\n7. Home')
        p3=int(input('Masukkan pilihan : '))
    if p3==1:
        uang=float(input('Masukan nominal USD = '))
        hasil=uang*16280
        print(uang, 'USD = ', hasil, 'Rupiah')
    elif p3==2:
        uang=float(input('Masukan nominal MYR = '))
        hasil=uang*3773
        print(uang, 'MYR = ', hasil, 'Rupiah')
    elif p3==3:
        uang=float(input('Masukkan nominal EUR = '))
        hasil=uang*17959
        print(uang, 'EUR = ', hasil, 'Rupiah')
    elif p3==4:
        uang=float(input('Masukkan nominal SGD = '))
        hasil=uang*11444
        print(uang, 'SGD = ', hasil, 'Rupiah')
    elif p3==5:
        uang=float(input('Masukkan nominal AUD = '))
        hasil=uang*10055
        print(uang, 'AUD = ', hasil, 'Rupiah')
    elif p3==6:
        pilihan1()
    else:
        awal()
    

    akhir()

def selesai():
    print('\nUlangi Program?\n1. YA\n2. TIDAK')
    x = int(input('Masukan Pilihan (1 or 2) : '))
    
    if x == 1:
        awal()
    elif x == 2:
        os.system('cls')
        print('Program Telah Selesai\n')
        print('Terima Kasih')
    else:
        print('\ninvalid number! please insert the correct number')
        time.sleep(1)
        selesai()
        
def akhir():
    time.sleep(1)
    selesai()

awal()




        





