# creating prima number pogram
num = int(input("Enter = "))

tree = False
if num == 0:
    print(num, "Ini adalah bilangan prima")
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            tree = True
            break
    if tree:
        print(num," : anda bukan bilangan prima")
    else:
        print(num, ": anda adalah bilangan prima")
