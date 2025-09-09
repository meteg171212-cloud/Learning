import random
possible_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("How long would you like yoru passsord to be?"))
protector = ""
for i in range(length):
    protector += random.choice(possible_characters)
print("your password is", protector)
