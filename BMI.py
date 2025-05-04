# membuat pogram kalkulator bmi
height = float(input("Enter Your Height In Cm : "))
weight = float(input("Enter Your Weight In Kg : "))
height2 = height/100

BMI = weight / (height2**2)

while True:
    if BMI < 18.5:
        print("Tidak Normal")
    elif BMI > 18.5 and BMI <24.5:
        print("Normal")
    elif BMI > 25 and BMI < 29.9:
        print("Berlebihan")
    else:
        print("Obesitas")
        break