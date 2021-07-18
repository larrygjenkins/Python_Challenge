import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Creating empty arrays for each month and the value of each month  in csv file, as well as the change from month to month
months = []
values = []
monthly_change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

#   Cycles through each row in the csv file (after the header) and adds months and value to the appropriate array
    for row in csvreader:
        months.append(row[0])
        values.append(row[1])

# Converts the strings in the value array into integers
for i in range(0, len(values)):
    values[i] = int(values[i])

# Creates a varable for total months, which is equal to the length of the months array
total_months = len(months)

# Creates a variable for total value, which sums all values in the value array
total_value = sum(values)

# Loops through each integer in the values array and finds the change from one integer to the next in the array, 
# then adds teh change to a new array called "monthly_change"
for i in range(1, len(values)):
    monthly_change.append(values[i]-values[i-1])

average_change = round(sum(monthly_change)/len(monthly_change), 2)

# Established variables for the greatest positive change and greatest negative change in the monthly_change array
max_change = max(monthly_change)
min_change = min(monthly_change)

# Established variables that will correspond to the months and values of the greatest positive and negative changes
max_change_value_index = 0
max_change_month_index = 0
min_change_value_index = 0
min_change_month_index = 0

# Loops through the values in the monthly_change array and finds index of highest and lowest values
for i in range(0, len(monthly_change)):
    if monthly_change[i] == max_change:
        max_change_value_index = i
        max_change_month_index = i+1
    if monthly_change[i] == min_change:
        min_change_value_index = i
        min_change_month_index = i+1

# These print statements provide analysis on screen
print(f'Financial Analysis')
print(f'-------------------------------------')
print(f'Total Months: {total_months}')
print(f'Total Value: ${total_value}')
print(f'Average Monthly Change: ${average_change}')
print(f'Greatest Increase in Profits: {months[max_change_month_index]} (${monthly_change[max_change_value_index]})')
print(f'Greatest Decrease in Profits: {months[min_change_month_index]} (${monthly_change[min_change_value_index]})')

# Defines path for output text file
output_file = os.path.join('Analysis', 'budget_analysis.txt')

# Prints analysis to .txt file in Analysis folder
with open(output_file, "w") as textfile:
    textfile.writelines(f'Financial Analysis\n')
    textfile.writelines(f'-------------------------------------\n')
    textfile.writelines(f'Total Months: {total_months}\n')
    textfile.writelines(f'Total Value: ${total_value}\n')
    textfile.writelines(f'Average Monthly Change: ${average_change}\n')
    textfile.writelines(f'Greatest Increase in Profits: {months[max_change_month_index]} (${monthly_change[max_change_value_index]})\n')
    textfile.writelines(f'Greatest Decrease in Profits: {months[min_change_month_index]} (${monthly_change[min_change_value_index]})\n')