import os
import csv
#reminder the variable type might have to be change to int()
# a variable refereing to another variable in a For or While loop needs 2 ==
#Ne pas oublier de ne pas read the header quand je ferai le travail

#Listing all my paths
budgetdoc = r"C:\Users\tadip\OneDrive\Documents\BAC\Data Analytics\Module 3 - Python\python-challenge\PyBank\Resources\budget_data.csv"
analysis = r"C:\Users\tadip\OneDrive\Documents\BAC\Data Analytics\Module 3 - Python\python-challenge\PyBank\Analysis\Financial Analysis.txt"
#Since the data is not seperated in two colomns, we create lists to store them.
date = []
profitloss = []
change =[]
#Read the budget_data.csv file
with open(budgetdoc, 'r', encoding = "UTF-8") as f: 
    csvreader = csv.reader(f,delimiter=",")

    #ensure we do not read/include the header
    header = next(csvreader)

    #Below, we are filling the list with data from the csv file. That creates columns.
    for row in csvreader :

        #Add dates
        date.append(row[0])

        #Add profit/loss and change the type to integer
        profitloss.append(row[1])
        profit_loss = [int(num) for num in profitloss]

        #Add changes by calculating the values of (i+1) - i where i is the row
        for i in profit_loss:
            difference = (i+1) - i
            change.append(difference)
    #Find total months
    totalmonths = len(date)
    print(totalmonths)    

    #Find the net amount of profit and loss by defining a function
    def amount (numbers): 

        net = 0
        for num in numbers:  
            net = net + num
        return net

    
    net_amount = amount(profit_loss)
    print(net_amount)

    #Find average change
    
    #Find greatest increase in profits
    def maximum(numbers): 

        max_num = 0
        for num in numbers: 
            if num > max_num: 
                max_num = num

        return max_num

    maximus = maximum(change)
    print(maximus)

    #Find greatest decrease in profits

    def minimum(numbers): 

        min_num = 0
        for num in numbers: 
            if num < min_num: 
                min_num = num

        return min_num

    minimus = minimum(change)
    print(minimus)

#Creating the txt file to display the analysis
with open(analysis, "w") as f:
    writer = csv.writer(f)
    #Write the title
    writer.writerow(["Financial analysis"])
    writer.writerow(["-------------------------------------------------------------------------------"])
    writer.writerow([f"Total Months: {totalmonths}"])
    writer.writerow([f"Total: $ {net_amount}"])
    writer.writerow([f"Average Change:"])
    writer.writerow([f"Greatest Increase in Profits: $ {maximus}"])
    writer.writerow([f"Greatet Decrease in Profits: $ ({minimus})"])