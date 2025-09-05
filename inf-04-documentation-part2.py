import random
tableSize = int(input("Enter table size: "))

numbers = []
for i in range(0, tableSize):
    n = random.randint(0, 20)
    numbers.append(n)

for i in range(0, tableSize):
    print("(" + str(i) + "): " + str(numbers[i]))

def totalOfArray(array):
    if (type(array) == list):
        total = 0
        for i in range(0, tableSize):
            total += numbers[i]

        return total

def evenNumbers_N(array):
    if (type(array) == list):
        total = 0
        for i in range(0, tableSize):
            if (numbers[i] % 2 == 0):
                total += 1
        
        return total

print("Total of array: " + str(totalOfArray(numbers)))
print("Total even numbers: " + str(evenNumbers_N(numbers)))