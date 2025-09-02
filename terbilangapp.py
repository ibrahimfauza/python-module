numbers = input("Masukan angka : ")

numbers_mapping = {
    "1": "Satru",
    "2": "Loro",
    "3": "Tego",
    "4": "Sempat",
    "5": "Lilo",
    "6": "Nemu",
    "7": "Tumbang",
    "8": "Wirang",
    "9": "Sayang",
}

output = ""

for n in numbers:
    terbilang = numbers_mapping.get(n, "Invalid")

    output = output + terbilang + ""

print(output)