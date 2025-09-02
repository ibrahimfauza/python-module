try:
    level = input("Level kamu : ")
    level = int(level)
    level = level / 0
    print(level)

except ZeroDivisionError:
    print("Error tidak bisa dibagi 0")
except ValueError:
    print("Yang kamu masukan itu bukan angka")