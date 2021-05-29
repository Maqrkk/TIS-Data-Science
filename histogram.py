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

# Put the relevant data into the data structure
for i in range(1, len(dataset)):
    row = dataset[i]
    school = row[1]
    schoolIndex = 0
    if (school == "Ravenclaw"):
        schoolIndex = 1
    elif (school == "Slytherin"):
        schoolIndex = 2
    elif (school == "Gryffindor"):
        schoolIndex = 3
        
    for index in range(amountFields):
        if (row[relevantFields[index]] == ''):
            data[schoolIndex][index].append(0.0)
        else:
            data[schoolIndex][index].append(float(row[relevantFields[index]]))

# Sort all the lists
for school in range(4):
    for i in range(amountFields):
        data[school][i].sort()
    
# Since the assignment asks to show one histogram, I'll show the one that I think to be homogeneous.
courseIndex = 11
plt.hist(data[0][courseIndex], density=True, alpha=0.5, label="Hufflepuff")
plt.hist(data[1][courseIndex], density=True, alpha=0.5, label="Ravenclaw")
plt.hist(data[2][courseIndex], density=True, alpha=0.5, label="Slytherin")
plt.hist(data[3][courseIndex], density=True, alpha=0.5, label="Gryffindor")
plt.title(dataset[0][relevantFields[courseIndex]])
plt.ylabel("Count")
plt.xlabel("Scores")
plt.show()