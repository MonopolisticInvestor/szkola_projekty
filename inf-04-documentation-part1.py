import random

# a random number
for i in range (0, 5):
    n = random.random()
    print(n)

print("Enter a number range 0-x: ")
x = input()

if (x == "str"):
    print("Wrong input")
else:
    for i in range(0, 5):
        n = random.randint(0, int(x))
        print(str(n))

print("numbers over x:")
for i in range(0,5):
    n = random.randint(int(x), 100)
    print(n)

print("a-b numbers:")
print("Enter a:")
a = int(input())
print("Enter b:")
b = int(input())

for i in range(0, 5):
    n = random.randint(a, b)
    print(n)