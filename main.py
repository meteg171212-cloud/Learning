import random
choice = int(input("Choose your own password or make automatic one? press 1 for auto and 0 for own"))
possible_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
if choice == 1:    
    protector = ""
    length = int(input("How long would you like your passsord to be?"))
    for i in range(length):
        protector += random.choice(possible_characters)
    print("your password is", protector)
elif choice == 0:
    protector = input("Enter your password here")
    print("your password has been set to", protector)
