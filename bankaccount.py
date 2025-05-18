# membuat pogram akun bank

print(5*"=","Selamat Datang!",5*"=","\nApakah ada yang perlu saya bantu?\nJika ada,katakan aja!\nSemoga Pelayanan disini Memuaskan anda\n",5*"=","Terima Kasih",5*"=")
cek_saldo = 0

def menu():
    #Menampilkan pilihan menu seperti:
    print("Cek Saldo")
    print("Setor Tunai")
    print("Tarik Tunai")
    print("Transfer")
    print("Keluar")

def dana():
    return cek_saldo

def setor():
    global cek_saldo
    setor_tunai = float(input("Masukkan Nominal yang ingin Anda Setorkan :Rp "))
    cek_saldo += setor_tunai
    return cek_saldo

def tarik():
    global cek_saldo
    tarik_tunai = float(input("Masukkan Nominal yang ingin Anda Tarik :Rp "))
    if tarik_tunai > cek_saldo:
        print("Saldo tidak Mencukupi")
        return cek_saldo
    cek_saldo -= tarik_tunai
    return cek_saldo

def kirim():
    global cek_saldo
    nama = str(input("Masukkan Nama yang ingin Anda Transfer : "))
    rekening = int(input("Masukkan Nomor Rekening : "))
    nominal = float(input("Masukkan nominal yang ingin Anda Transfer : "))
    if nominal > cek_saldo:
        print("Saldo tidak cukup untuk melakukan transfer.")
    else:
        cek_saldo -= nominal
        print(f"Transfer berhasil kepada {nama} dengan nomor rekeneing {rekening} sebesar Rp {nominal}.")
    return cek_saldo

while True:
    menu()
    data_pilihan = int(input("Enter \n(1, 2, 3, 4 or 5): "))
    if data_pilihan == 1:
        print(f"Saldo anda tersisa : Rp {dana()}")
    elif data_pilihan == 2:
        print(f"Saldo anda terisa :Rp {setor()}")
    elif data_pilihan == 3:
        print(f"Saldo anda terisa :Rp {tarik()}")
    elif data_pilihan == 4:
        print(f"Saldo anda terisa :Rp {kirim()}")
    elif data_pilihan == 5:
        print(5*"=","Terima Kasih Telah Menggunakan Pelayanan Kami",5*"=")
        break
    else:
        print("Pilihan tidak valid.")
