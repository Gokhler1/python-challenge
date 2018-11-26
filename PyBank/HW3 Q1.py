import os

import csv

csvpath = "budget_data.csv"
month = []
amount = []
next_amount=[]
difference = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
    budget = csv.reader(csvfile, delimiter=",")
    month_counter = 0
    total_budget= 0
    header = next(budget)

    for raw in budget:
        month_counter = month_counter +1
        amount.append(int(raw[1]))
        month.append(raw[0])
        next_amount.append(int(raw[1]))

    next_amount.pop(0)

    for x in amount :
        total_budget = total_budget + x

    new_csv = zip(amount, next_amount)

    for line in new_csv:
        diff = line[1] -line[0]
        difference.append(diff)

    def average(numbers):
        length = len(numbers)
        total = 0.0
        for number in numbers:
            total += number
        return total / length
    average_num= average(difference)
    max_diff=max(difference)
    min_diff=min(difference)
    max_index = difference.index(max_diff)
    min_index = difference.index(min_diff)

    # print(difference)
    # print(amount)
    # print(next_amount)
    print ("total months : " + str(month_counter))
    print ("total: $" + str(total_budget))
    print("Average  Change: $" +str(round(average_num,2)))
    print("Greatest Increase in Profits: " + month[max_index + 1] + " ($" + str(max_diff) + ")")
    print("Greatest Decrease in Profits: " + month[min_index + 1] + " ($" + str(min_diff) + ")")