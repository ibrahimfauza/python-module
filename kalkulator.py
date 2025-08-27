# (+-* / exit)
command = ""

while command != "exit":
    command = input("Perintah : ")

    if command == "exit" :
        break

    if command != "+" and command != "-" and command != "/" and command != "*":
        print("Perintah tidak dikenali")
        continue

    a = int(input("Angka Pertama : "))
    b = int(input("Angka kedua : "))

    if command == "+":
        result = a + b
    elif command == "-":
        result = a - b
    elif command == "*":
        result = a * b
    elif command == "/":
        result = a / b
    print(f"Hasil : {result}")

print("Terimakasih sudah menggunakan aplikasi kami")