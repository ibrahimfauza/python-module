trying = 0
secret_number = 7
limit = 3

while trying < limit:
    guess_number = input("Masukan angka (1-9) : ")
    guess_number = int(guess_number)

    if guess_number == secret_number:
        print("Selamat Kamu Benar")
        break
    trying += 1

if trying == limit:
    print("Coba Lagi")