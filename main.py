# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("geeks:{0:2d}, \nportal:{1:8.2f}".format(12, 000.546))

print("the salary is: ${:10.2f}".format(20080.45))
print('*', end="")
print('jamshid', end="")

s = "hello"

print(s[2:])

# Integer arithmetic
x = 14
y = 8
c = x/y
a = int(x)
b = int(y)
d = a/b
print(d)
f = (x % y)
print(f)

print(int(c))
print(int(x/y))


x = 72
print("my favorite number is;", x)

z = input("Enter the year your car was bilt:")
v = 2021 - int(z)
print("your care is:", v, " Months old")


# program to convert Celsius to Fahrenheit.

cd = input("enter the temperature in Celsius")
c = float(cd)
f = (9/5*c+32)
print("Fahrenheit equivalent is {0:5.2f}".format(f))
