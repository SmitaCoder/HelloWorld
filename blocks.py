for i in range(1, 5):
    print("No. {} squared is {} and cubed is {}".format(i,i ** 2,i ** 3))

name = input("Please enter ur name : ")
age = int(input("Please enter your age : "))

if age>=18:
    print("You are eligible to vote")
else:
    print("Come back later in {0} years".format(18-age))