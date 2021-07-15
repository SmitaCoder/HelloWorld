parrot = "Norwegian Blue"

letter = input("Enter charatcter : ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("{} is NOT in {}".format(letter, parrot))
