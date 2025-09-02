users = open("users.txt", "r")

array=(users.readlines())

index = 1
for user in array:
    print(f"{index} - {user}")
    index += 1

users.close()