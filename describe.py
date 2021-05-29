import sys              # For argv
from os import path     # For path.exists
from math import sqrt   # For square root calculation

# This will check if the argument provided is a numeric value
def isNumber(arg):
    try:
        float(arg)
        return True
    except:
        return False

# This will print a single float, formatted correctly
def printSingleEntry(num):
    print("{0:>14.6f}".format(num), end='')

# Check if only 1 parameter was given, a .csv file
if len(sys.argv) == 1:
    print("Please give a .csv dataset as parameter")
    quit()
if len(sys.argv) > 2:
    print("Please only give one parameter, a .csv file")
    quit()
filename = sys.argv[1]
if (filename[-4:] != ".csv"):
    print("Please provide a .csv dataset as parameter")
    quit()
if (not path.exists(filename)):
    print("The file " + filename + " was not found.")
    quit()

# Now open the file and parse it into a 2-dimensional list
dataset = [x.split(',') for x in open(filename).readlines()]
amountEntries = len(dataset) - 1; # subtract 1 for the header

# Build a list of the indexes of the fields that have numeric data
relevantFields = []
for index in range(0, len(dataset[1])):
    if (isNumber(dataset[1][index])):
        relevantFields.append(index)
amountFields = len(relevantFields)

# Build the header for the output
header = "        "  # 8 spaces for the 'category'
for i in range(1, amountFields + 1):
    header += "{0:>14}".format("Feature " + str(i)) # 14 spaces per column
print(header)

# Create a list of empty lists for the data
data = []
for i in range(amountFields):
    data.append([])

# Put the relevant data into the data structure
for i in range(1, len(dataset)):
    row = dataset[i]
    for index in range(amountFields):
        if (row[relevantFields[index]] == ''):
            data[index].append(0.0)
        else:
            data[index].append(float(row[relevantFields[index]]))

# Sort all the lists
for i in range(amountFields):
    data[i].sort()

# Print the count of every feature
print('Count   ', end='')
for i in range(amountFields):
    printSingleEntry(len(data[i]))
print()

# Print the mean of every feature, and save them for use in standard deviation calculation
means = []
print('Mean    ', end='')
for i in range(amountFields):
    total = sum(data[i])
    mean = total/amountEntries
    means.append(mean)
    printSingleEntry(mean)
print()

# Print the standard deviation of every feature
print('Std     ', end='')
for i in range(amountFields):
    total = 0
    for num in data[i]:
        total += (num - means[i])**2
    total = sqrt(total / amountEntries)
    printSingleEntry(total)
print()

# Print the minimum of every feature.
print('Min     ', end='')
for i in range(amountFields):
    printSingleEntry(data[i][0])
print()

# Print the 25% of every feature.
print('25%     ', end='')
for i in range(amountFields):
    printSingleEntry(data[i][int(0.25*amountEntries)])
print()

# Print the 50% of every feature.
print('50%     ', end='')
for i in range(amountFields):
    printSingleEntry(data[i][int(0.5*amountEntries)])
print()

# Print the 75% of every feature.
print('75%     ', end='')
for i in range(amountFields):
    printSingleEntry(data[i][int(0.75*amountEntries)])
print()

# Print the maximum of every feature.
print('Max     ', end='')
for i in range(amountFields):
    printSingleEntry(data[i][-1])
print()