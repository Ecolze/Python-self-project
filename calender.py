import calendar
tahun = int(input("Masukkan Tahun : "))

while True:
    m = int(input("Masukkan Bulan : "))
    if m>= 1 and m<=12:
        print(calendar.month(tahun,m))
        break
    else:
        print("Invalid Input!")