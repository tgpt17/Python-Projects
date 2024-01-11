"""
Program: sandwich.py
Author: Travis Wagner
Creation Date: 4/7/2022
Description: Asks user for their sandwich preferences to make a sandwich. Displays choices and prices at the end
"""
import pyinputplus as pyip

print('Welcome to Trav\'s sandwich shop! Let\'s build your sandwich.')

print('Choose your bread.')
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True) # asks user to pick choice from menu
bread_price = {'wheat': 2.00, 'white': 1.00, 'sourdough': 3.00} # dictionary with choice prices
bread_final = bread_price[bread] # takes bread choice and matches with the price for that choice in the dictionary


print('Choose your protein.')
protein = pyip.inputMenu(['tofu', 'seitan', 'jackfruit'], numbered=True) # asks user to pick choice from menu
protein_price = {'tofu': 2.00, 'seitan': 4.00, 'jackfruit': 3.50} # dictionary with choice prices
protein_final = protein_price[protein] # takes protein choice and matches with the price for that choice in dictionary


cheese_response = pyip.inputYesNo(prompt='Would you like cheese? ')
if cheese_response == 'yes':
    cheese_option = pyip.inputMenu(['cheddar', 'gouda', 'provolone'], numbered=True) # ask user to pick choice from menu
    cheese_price = {'cheddar': 1.00, 'gouda': 2.50, 'provolone': 3.00} # dictionary with choice prices
    cheese_final = cheese_price[cheese_option] # takes cheese choice and matches with the price for choice in dictionary
else:
    cheese_option = 'No cheese'
    cheese_final = 0.00 # if user answers no, price will be 0


mayo_response = pyip.inputYesNo(prompt='Would you like mayo? ') # asks user if they want mayo
if mayo_response == 'yes':
    mayo_final = 0.50 # mayo price if user answers yes
else:
    mayo_final = 0.00 # mayo price if user answers no


mustard_response = pyip.inputYesNo(prompt='Would you like mustard? ') # asks user if they want mustard
if mustard_response == 'yes':
    mustard_final = 0.10 # mustard price if user answers yes
else:
    mustard_final = 0.00 # mustard price if user answers no


lettuce_response = pyip.inputYesNo(prompt='Would you like lettuce? ') # asks user if they want lettuce
if lettuce_response == 'yes':
    lettuce_final = 0.05 # lettuce price if user answers yes
else:
    lettuce_final = 0.00 # lettuce id user answers no


tomato_response = pyip.inputYesNo(prompt='Would you like tomato? ') # asks user if they want tomato
if tomato_response == 'yes':
    tomato_final = 0.10 # tomato price if user answers yes
else:
    tomato_final = 0.00 # tomato price if user answers no


num_sandwiches = pyip.inputInt(prompt='How many sandwiches would you like? ', min=1) # asks user number of sandwiches
total_sandwich = (bread_final + protein_final + mayo_final + mustard_final + lettuce_final + tomato_final)\
                 * num_sandwiches # adds all choices together multiplied by number of sandwiches

print()
print('Here is your sandwich total:') # table showing all the results
print('{:<10}{:>10}{:>10}'.format('Categories', 'Your Choices', 'Price'))
print('{:<10}{:>10}{:>5}{:>5,.2f}'.format('Bread', bread, '$', bread_final))
print('{:<10}{:>10}{:>5}{:>5,.2f}'.format('Protein', protein, '$', protein_final))
print('{:<10}{:>10}{:>5}{:>5,.2f}'.format('Cheese', cheese_option, '$', cheese_final))
print('{:<10}{:>10}{:>5}{:>5,.2f}'.format('Mayo', mayo_response, '$', mayo_final))
print('{:<10}{:>10}{:>5}{:>5,.2f}'.format('Mustard', mustard_response, '$', mustard_final))
print('{:<10}{:>10}{:>5}{:>5,.2f}'.format('Lettuce', lettuce_response, '$', lettuce_final))
print('{:<10}{:>10}{:>5}{:>5,.2f}'.format('Tomato', tomato_response, '$', tomato_final))
print('{:<10}{:>10}'.format('Number of sandwiches', num_sandwiches))
print('{:<10}{:>15}{:>5,.2f}'.format('Total', '$', total_sandwich))



