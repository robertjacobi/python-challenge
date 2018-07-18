#Import dependencies
import os
import csv

#Establish lists and variables
TotalMonths = 0
TotalRev = 0
Date = []
Revenue = []
Max = 0
Min = 0


#Read in csv file
budget_csv = os.path.join("budget_data.csv")
    
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip header
    next(csvfile)

    #Sum the total months
    for row in csvreader:
        if row[0] != "":
            TotalMonths = TotalMonths + 1
    
    #Sum the total revenue
        TotalRev += int(row[1])
    
    #Convert revenue column to an array
        Revenue.append(int(row[1]))
    
    #Convert date colunn to an array
        Date.append(row[0])

#Calculate average change
    average_change = round(int(TotalRev)/int(TotalMonths),2)

#Find the min and max revenue values
Max = max(Revenue)
Min = min(Revenue)

#Find the min and max indexes
x = Revenue.index(Max)
y = Revenue.index(Min)

#Match date to min and max indexes
max_date = Date[x]
min_date = Date[y]

#Print to terminal

print("Financial Analysis")
print("-------------------------------------------")
print("Total Months: " + str(TotalMonths))
print("Total: $" + str(TotalRev))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + max_date +" ($" + str(Max) + ")")
print("Greatest Decrease in Profits: " + min_date +" ($" + str(Min) + ")")

#Print to .txt file

PyBank_txt = os.path.join("PyBank.txt")

with open(PyBank_txt, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-------------------------------------------'])
    csvwriter.writerow(['Total Months: ' + str(TotalMonths)])
    csvwriter.writerow(['Total: $' + str(TotalRev)])
    csvwriter.writerow(['Average Change: $' + str(average_change)])
    csvwriter.writerow(['Greatest Increase in Profits: ' + max_date + ' ($' + str(Max) + ')'])
    csvwriter.writerow(['Greatest Increase in Profits: ' + min_date + ' ($' + str(Min) + ')'])





