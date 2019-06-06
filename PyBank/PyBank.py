import os
import csv
list=[]
max = 0
min = 0
month_count = 0
total = 0
sum_of_change = 0
csvpath = os.path.join("budget_data.csv")
with open (csvpath, newline = "", encoding="utf8")  as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
#Convert all the data into a single list
    for month, profits in csvreader:
        list.append(month + " " + profits)
        month_count = month_count + 1
        total = total + int(profits)

#Traverse through the length of this list
for i in range(len(list)-1):
    monthly_difference = int((list[i + 1]).split(" ")[1]) - int((list[i].split(" "))[1])
    sum_of_change += monthly_difference

    if monthly_difference > max:
        max = monthly_difference
        month_max_difference = (list[i + 1]).split(" ")[0]
    if monthly_difference < min:
        min = monthly_difference
        month_min_difference = (list[i + 1]).split(" ")[0]

#Format month-year format to required output format
formatted_month_max_diff = month_max_difference.split("-")[0]+"-20"+month_max_difference.split("-")[1]
formatted_month_min_diff = month_min_difference.split("-")[0]+"-20"+month_min_difference.split("-")[1]

# Print on screen
print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(month_count))
print("Total: $" +"{:.0f}".format(total))
print("Average  Change: $" +"{:.2f}".format(sum_of_change/(len(list)-1)))
print("Greatest Increase in Profits: "+ formatted_month_max_diff + " ($" +str(max) +")" )
print("Greatest Decrease in Profits: "+ formatted_month_min_diff + " ($" +str(min) +")" )

# Print on file
write_file = open("PyBank.txt","w+")
write_file.write("Financial Analysis")
write_file.write("\n---------------------------")
write_file.write("\nTotal Months: " + str(month_count))
write_file.write("\nTotal: $" +"{:.0f}".format(total))
write_file.write("\nAverage  Change: $" + "{:.2f}".format(sum_of_change/(len(list)-1)))
write_file.write("\nGreatest Increase in Profits: "+ formatted_month_max_diff + " ($" +str(max) +")" )
write_file.write("\nGreatest Decrease in Profits: "+ formatted_month_min_diff + " ($" +str(min) +")" )
