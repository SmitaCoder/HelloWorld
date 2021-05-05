# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("Hello World!!")
print(1 + 2)
print(7*6)
print()
print('The end')
print("Hello" + ' world')
#Below line# 25-27 is example of variable to store string
greeting = "Hello"
name = "Bruce"
print(greeting + ' ' + name)
#Below line# 29-31 is example of variable to read input from console to store the string value
greeting = "Hello"
name = input("Please enter ur name - ")
print(greeting + ' ' + name)

print("Number 1\t The Larch")

#Challenge 1
parrot = "Norwegian Blue"
print(parrot[3])
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

#Backwards
print(parrot[25:-26:-1])
#Python Idiom
print(parrot[::-1])

backwards = "abcdefghijklmnopqrstuvwxyz"
print(backwards[16:13:-1])
print(backwards[-22::-1])
print(backwards[25:17:-1])

#String replacement placeholders
print("There are {0} days in {1}, {2} and {3} months".format(31,"Jan","May","Dec"))

