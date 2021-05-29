import sys              # For argv
from os import path     # For path.exists

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

#import library
import pandas as pd
import matplotlib.pyplot as plt

#add csv file to dataframe
df = pd.read_csv('dataset.csv')

#create histogram
histogram = df.hist(bins = 7)

plt.show()