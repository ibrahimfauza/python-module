import random

# for index in range(5):
#     print(random.randint(10, 30))

users = ['Abi', 'Budi', 'Cally', 'Dani', 'Exel']

# batas_bawah = 0
# batas_atas = len(users) - 1

# random_int = random.randint(batas_bawah, batas_atas)

# for i in range(5):
#     random_int= random.randint(batas_bawah, batas_atas)
#     print(random_int)

# # random_int= random.randint(batas_bawah, batas_atas)
# winner = users[random_int]

winner = random.choice(users)
print(winner)