# creating suhu converter
# membuat fungsi pernyataan
class suhu:
    def __init__(self):
        pass

    def celcius(self, farenheit):
        "Merubah suhu yang diminta ke Celcius"
        return (5/9) * (farenheit - 32)
    
    def celcius(self, reamur):
        "Merubah suhu yang diminta ke Celcius"
        return reamur / 0.8
    
    def farenheit(self, celcius): 
        "Merubah suhu yang diminta ke Farenheit"
        return (celcius * 9/5) + 32
    
    def farenheit(self, reamur): 
        "Merubah suhu yang diminta ke Farenheit"
        return (reamur * 2.25) + 32

    def reamur(self, celcius):
         "Merubah suhu yang diminta ke Reamur"
         return 4/5 * celcius
    
    def reamur(self, farenheit):
         "Merubah suhu yang diminta ke Reamur"
         return 4/9 * (farenheit-32)
    
    def celcius(self, kelvin):
        "Merubah suhu yang diminta ke Celcius"
        return (kelvin - 273.15)

    def kelvin(self, celcius):
        "Merubah suhu yang diminta ke Kelvin"
        return (celcius + 273.15)

suhu = suhu()

# membuat perintah 
print('1.C To F')
print('2.F To C')
print('3.C To R')
print('4.R To C')
print('5.R To F')
print('6.F To R')
print('7.K To C')
print('8.C To K')

# membuat perulangan 
while True:
    choose = input('Enter choice : \n' 
    '1 2 3 4 5 6 7 8 = ' )
    if choose in ('1', '2', '3', '4', '5', '6', '7', '8'):
        if choose == '1':
            celcius = float(input('Enter Number for celcius = '))
            print(suhu.farenheit(celcius))
        elif choose == '2':
            farenheit = float(input('Enter Number for farenheit = '))
            print(suhu.celcius(farenheit))
        elif choose == '3':
            celcius = float(input('Enter Number for celcius = '))
            print(suhu.reamur(celcius))
        elif choose == '4':
            reamur = float(input('Enter Number for reamur = '))
            print(suhu.celcius(reamur))
        elif choose == '5':
            reamur = float(input('Enter Number for reamur = '))
            print(suhu.farenheit(reamur))
        elif choose == '6':
            farenheit = float(input('Enter Number for farenheit = '))
            print(suhu.reamur(farenheit))
        elif choose == '7':
            kelvin = float(input('Enter Number for kelvin = '))
            print(suhu.celcius(kelvin))
        elif choose == '8':
            celcius = float(input('Enter Number for celcius = '))
            print(suhu.kelvin(celcius))
        break
    else:
        print('Invalid')
