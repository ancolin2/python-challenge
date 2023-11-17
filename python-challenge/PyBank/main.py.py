#import OS
import os
#import csv
import csv
#csv path to get to data file
csvpath = os.path.join("..","PyBank","Resources","budget_data.csv")
#create list for total months
total_months = []
#create a list to add to text file at the end
text_list = ["Financial Analysis", "----------------------------------------"]
#create a variable for total profit, greatest increase, greatest decrease
total_profit = 0
greatest_increase = 0
greatest_decrease = 0
#create a list for profit column
profit_list = []
#add the title and line break to terminal
print("Financial Analysis")
print("----------------------------------------")
#Open the data file
with open(csvpath) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read the header row first and skip it
    csv_header = next(csvreader, None)
    #Looping through csv reader for each element
    for element in csvreader:
        #adding months to the list
        total_months.append(element[0])
        #add profit column to list
        profit_list.append(element[1])
        #Adding total profit to loop
        current_profit = int(element[1])
        #adding current profit to the running total
        total_profit = total_profit + current_profit
        #establish variable for the profit in the last line for calculations later
        last_profit = int(element[1])

    #loop to compare changes in profit for each month
    for x in range(len(profit_list)):
        #conditional for greatest increase 
        if (int(profit_list[x]) - int(profit_list[int(x)-1])) > greatest_increase:
            greatest_increase = int(profit_list[x]) - int(profit_list[int(x)-1])
            #get the corresponding month
            increase_month = total_months[x]
        #conditional for greatest decrease 
        if (int(profit_list[x]) - int(profit_list[int(x)-1])) < greatest_decrease:
            greatest_decrease = int(profit_list[x]) - int(profit_list[int(x)-1])
            #get the corresponding month
            decrease_month = total_months[x]

#Converting months list to the length then printing result
print("Total Months: " + str(len(total_months)))
#add to text list as well for the end file
text_list.append("Total Months: " + str(len(total_months)))
#Converting total profit to string to be able to print
print("Total: $" + str(total_profit))
#add to text list
text_list.append("Total: $" + str(total_profit))
#formula for average change
average_change = (int((profit_list[len(profit_list)-1]))-int(profit_list[0]))/int((len(profit_list)-1))
#round to two decimal places
rounded = round(average_change, 2)
#print the average change,
print(f"Average Change: $", rounded)
#add to text list
text_list.append("Average Change: $"+ str(rounded))
#Print greatest increase
print(f"Greatest Increase in Profits: ", increase_month, "($", greatest_increase,")")
#add to text list
text_list.append("Greatest Increase in Profits: " + str(increase_month) + "($"+ str(greatest_increase)+ ")")
#Print greatest decrease
print(f"Greatest Decrease in Profits: ", decrease_month, "($", greatest_decrease,")")
#add to text list
text_list.append("Greatest Decrease in Profits: "+ decrease_month+ "($" + str(greatest_decrease) +")")

#open a new file and name it pybank_final
with open("pybank_final","w",newline="")as newfile:
    #loop through the text list
    for y in text_list:
        #add each item in list to the new file
        newfile.write(y)
        #make sure each item in list gets added to a new line
        newfile.write('\n')