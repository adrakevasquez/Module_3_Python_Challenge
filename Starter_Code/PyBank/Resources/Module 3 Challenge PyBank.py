import os
import csv

#path csv file

path = os.path.join("C:\\Users\\User\\Documents\\Data_Bootcamp\\Module_3\\Challenge\\Starter_Code\\Starter_Code\\PyBank\\Resources","budget_data.csv")
out_path = os.path.join("C:\\Users\\User\\Documents\\Data_Bootcamp\\Module_3\\Challenge\\Starter_Code\\Starter_Code\\PyBank\\Resources","Py_Bank_Results.txt")

#variables
previous_month = 0
total = 0
total_months = 0

#list
profit_change_list = []
months_list = []

#open/read csv file
with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headerskip = next(csvreader)

#calculate total months
    for row in (csvreader):
        total_months+= 1   

#calculating Total Profit/Loss
        total+= int(row[1])

#calculating Average Change
        change = int(row[1]) - previous_month
        profit_change_list.append(change)
        previous_month = int(row[1])
        months_list.append(row[0])
    profit_change_list = profit_change_list[1:]
    average = sum(profit_change_list)/(total_months-1)

#caluclating greatest increase/decrease
    greatest_increase = max(profit_change_list)
    greatest_decrease = min(profit_change_list)

#calculating months of greatest increase/decrease

    highest_month_index = profit_change_list.index(greatest_increase)
    lowest_month_index = profit_change_list.index(greatest_decrease)

# Assign best and worst month
    best_month = months_list[highest_month_index]
    worst_month = months_list[lowest_month_index]

#printing the result
print("Financial Analysis")
print("------------------------------------------")
print("Total Months:", total_months)
print("Total:", "$", total)
print("Average Change: $" , round(average, 2))
print("Greatest Increase in Profits:", best_month,  "$", (greatest_increase))
print("Greatest Decrease in Profits:", worst_month, "$", (greatest_decrease))

with open(out_path, "w") as txtfile:
    writer_txt_1 = (
    f"Financial Analysis\n"
    f"------------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${round(average, 20)}\n"
    f"Greatest Increase in Profits:{best_month} ${greatest_increase}\n"
    f"Greatest Decrease in Profits:{worst_month} ${greatest_decrease}\n"
    )
    txtfile.write(writer_txt_1)