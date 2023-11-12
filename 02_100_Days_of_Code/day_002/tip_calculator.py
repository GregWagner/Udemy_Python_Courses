''' Day 2 Challenge '''

print('Welcome to the Tip Calculator')
total_bill = float(input('What was the total bill? $'))
tip_percent = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
number_of_people = int(input('How many people to split the bill? '))

cost = total_bill + (total_bill * tip_percent / 100)
cost_per_person = cost / number_of_people

print(f'Each person should pay: ${round(cost_per_person, 2)}')
