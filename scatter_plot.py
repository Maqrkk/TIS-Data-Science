import matplotlib.pyplot as plt

# This will check if the argument provided is a numeric value
def isNumber(arg):
    try:
        float(arg)
        return True
    except:
        return False

# Now open the file and parse it into a 2-dimensional list
dataset = [x.split(',') for x in open("dataset_train.csv").readlines()]
amountEntries = len(dataset) - 1; # subtract 1 for the header

# Build a list of the indexes of the fields that have numeric data
relevantFields = []
for index in range(0, len(dataset[1])):
    if (isNumber(dataset[1][index])):
        relevantFields.append(index)
amountFields = len(relevantFields)

# Create 4 multidimensional lists, one for each house
data = []
for i in range(4):
    newList = []
    for i in range(amountFields):
        newList.append([])
    data.append(newList)

# Define the house names
houseNames = ["Hufflepuff", "Ravenclaw", "Slytherin", "Gryffindor"]

# Put the relevant data into the data structure
for i in range(1, len(dataset)):
    row = dataset[i]
    school = row[1]
    schoolIndex = houseNames.index(school)
    for index in range(amountFields):
        if (row[relevantFields[index]] == ''):
            data[schoolIndex][index].append(0.0)
        else:
            data[schoolIndex][index].append(float(row[relevantFields[index]]))

# I don't know what it means for two features to be 'similar'. So I chose these features because all colours are just big blobs here.
course1 = 1
course2 = 11
for i in range(4):
    plt.scatter(data[i][course1], data[i][course2])
plt.xlabel(dataset[0][relevantFields[course1]])
plt.ylabel(dataset[0][relevantFields[course2]])
plt.show()