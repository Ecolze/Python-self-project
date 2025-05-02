# membuat pasword gen

import random

Up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low = "abcdefghijklmopqrsyuvwxyz"
num = "1234567890"
sys = "_."

length = 8
iden = Up+low+num+sys
username ="".join(random.sample(iden, length))
print(f"Password anda adalah : " {username})

        
