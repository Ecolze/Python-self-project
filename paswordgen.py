# membuat pasword gen

import random

Up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low = "abcdefghijklmopqrsyuvwxyz"
num = "1234567890"
sys = "_."

length = 8
iden = Up+low+num+sys

username ="".join(random.sample(iden, length))
if iden != length: # membuat pengecualian untuk user
    print("Invalid")
else:
    print(f"Pasword Anda adalah: {username}")
        
