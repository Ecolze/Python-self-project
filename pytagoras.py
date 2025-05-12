# membuat rumus pytagoras
import math



def nilai_a():
    b = int(input("Enter B : "))
    c =  int(input("Enter C : "))
    a = math.sqrt(math.pow(b,2) - math.pow(c,2))
    rumus = math.pow(a,2) - math.pow(b,2)
    return rumus

def nilai_b():
    a = int(input("Enter A : "))
    c =  int(input("Enter C : "))
    b = math.sqrt(math.pow(a,2) - math.pow(c,2))
    rumus = math.pow(a,2) - math.pow(b,2)
    return rumus

def nilai_c():
    a = int(input("Enter A : "))
    b =  int(input("Enter B : "))
    c = math.sqrt(math.pow(a,2) + math.pow(b,2))
    return c


data_pilihan = int(input("Enter (1, 2, or 3): "))
if data_pilihan == 1:
    print(f"Hasil nilai_a adalah: {round(nilai_a())} Cm")
elif data_pilihan == 2:
    print(f"Hasil nilai_b adalah: {round(nilai_b())}Cm")
elif data_pilihan == 3:
    print(f"Hasil nilai_c adalah: {round(nilai_c())}Cm")
else:
    print("Pilihan tidak valid.")
