# This program calculates travel expenses from amounts spent on gas, accomodation, and food.
# 9/22/22
# CTI-110 P2HW1 - Travel 
# Curtis Walker-Nepstad
#
# **************Pseudocode**************
# Display "This program calculates travel expenses
# Input budget
# Input destination
# Input gas
# Input accom
# Input food
# Set expenses = gas + accom + food
# Display "----Expenses----"
# Display "Location ", destination
# Display "Initial Budget: ", $budget
# Display "Gas: ", $gas
# Display "Accomodation: ", $accom
# Display "Food: ", $food
# Display "Remaining Balance: ", $(budget - expenses)

print('This program calculates travel expenses \n')
budget = int(input('Enter budget:'))
destination = input('\nEnter travel destination:')
gas = int(input('\nEnter approximate amount spent on gas:'))
accom = int(input('\nEnter approximate amount spent on accomodation:'))
food = int(input('\nEnter approximate amount spent on food:'))
expenses = gas + accom + food
print('\n----Expenses----')
print(f'{"Location:" : >15}  {destination : <20}')
print(f'{"Initial Budget:" : >15}  ${float(budget) : <20}')
print(f'{"Gas:" : >15}  ${float(gas) : <20}')
print(f'{"Accomodation:" : >15}  ${float(accom) : <20}')
print(f'{"Food:" : >15}  ${float(food) : <20} \n')
print(f'{"Remaining Balance:" : >15}  ${float(budget - expenses) : <20}')



