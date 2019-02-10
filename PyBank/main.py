import os
import csv

#path to collect the data from file
bankCSV = os.path.join('Resources', 'budget_data.csv')

#path for output
output_path = os.path.join('bank_results.txt')

#Initialize variables
mcount = 0; total = 0; PreValue = 0; Diff = 0; DiffMax = 0; DiffMin = 0
revenues = 0
rev_change = []
avg_change = 0
initial = 0

#Open and read CSV file
with open(bankCSV, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     print(f'Financial Analysis'+'\n')
     print(f'----------------------------'+'\n')
     for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - PreValue

         #calculate the average change
         revenues = float(i[1]) - float(initial)
         rev_change.append(revenues)
         initial = float(i[1])

     avg_change = sum(rev_change)/len(rev_change)

     for i in csvreader:

         #Placeholder to track greatest increase in profits (financial analysis)
         if (DiffMax < Diff):
            DiffMax = Diff
            DiffMaxDate = month
         #Placeholder to track greatest decrease in profits (financial analysis)
         if (DiffMin > Diff):
            DiffMin = Diff
            DiffMinDate = month

         PreValue = iAmount   
         # Get total months (financial analysis)
         mcount = mcount + 1
         total += int(Amount) 

# Print Results
print(f'Total Months : {mcount}')
print(f'Total: $ {total}')
print(f'Average Change: $ + {avg_change}')
print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')
print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')


#output to a text file
with open(output_path, "w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("----------------------------")
    txt_file.write("Total Months:" + (mcount))
    txt_file.write("Total:" + (total))
    txt_file.write("Average Change:" + (avg_change))
    txt_file.write(f"Greatest Increase in Profits: {DiffMaxDate} : ${DiffMax}")
    txt_file.write(f"Greatest Decrease in Profits: {DiffMinDate} :  ${DiffMin}")