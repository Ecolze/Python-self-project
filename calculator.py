# Membuat kerangka 
class calculator:
    def __init__(this):
        pass

    def tambah(this, num1, num2):
        print('Hasil anda adalah : ')
        return num1 + num2 # bila didelete eror pada pilihan 1
    
    def kurang(this, num1, num2):
        print('Hasil anda adalah : ')
        return num1 - num2
    
    def kali(this, num1, num2):
        print('Hasil anda adalah : ')
        return num1 * num2
    
    def bagi(this, num1, num2):
        print('Hasil anda adalah : ')
        if num2 == 0:
            print('Invalid')
        else:
            return num1 / num2
        
calculator = calculator()

print('1.Tambah')
print('2.Kurang')
print('3.Kali')
print('4.Bagi')

while True:
    # membuat pilihan dari user
    pilihan = input('Enter choice 1 2 3 4 = ' )
    if pilihan in ('1', '2', '3', '4'):
        num1 = float(input('Enter Number 1 = '))
        num2 = float(input('Enter Number 2 = '))

        if pilihan == '1':
            print(calculator.tambah(num1, num2))

        elif pilihan == '2':
            print(calculator.kurang(num1,num2))

        elif pilihan == '3':
            print(calculator.kali(num1, num2))

        elif pilihan == '4':
            print(calculator.bagi(num1, num2))
        break
    else:
        print('Invalid')



            



