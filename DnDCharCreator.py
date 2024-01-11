"""
Program: DnDCharCreator.py
Author: Travis Wagner
Creation Date: 3/31/2022
Description: Asks user for class, race, and alignment for Dnd character. Then repeats it back to them in a breakdown if
they enter the correct terms in the regex. Otherwise it will show no match.
"""


import re


def main():
    print('Welcome to the DnD 5e character creator!')
    name_source = create_name()
    class_source = create_class()
    race_source = create_race()
    alignment_source = create_alignment()
    outputs(name_source, class_source, race_source, alignment_source) # sends functions to outputs


def create_name():
    print()
    new_name = input('Please enter your new character\'s name (first and last): ') # asks user for their character name
    name_regex = re.compile(r'^([a-zA-Z?\'?]{2,}\s[a-zA-Z?\'?]{1,}\'?-?[a-zA-Z?\'?]{2,}\s?([a-zA-Z?\'?]{1,})?)')
    name_source = name_regex.search(new_name) # ^ validates name to see if it fits criteria
    # ^ searches for validated name
    return name_source


def create_class(): # user enters class from given list
    print()
    print('Here the classes to choose from: Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, '
          'Sorcerer, Warlock, or Wizard')
    class_finder = input('Enter what Class do you want to be in Dungeons and Dragons? (in lowercase): ')
    class_regex = re.compile(r'''(barbarian|bard|cleric|druid|fighter|monk|paladin|ranger|rogue|sorcerer|warlock|wizard|
    )''') # validates user enters a class in the given list
    class_source = class_regex.search(class_finder)  # searches for class entered by user in regex

    return class_source # returns chosen class to main


def create_race(): # user enters race from given list
    print()
    print('Here are the races to choose from: Dragonborn, Dwarf, Elf, Gnome, Orc, Human, or Tiefling')
    race_finder = input('Enter what Race you would like to be in Dungeons and Dragons? (in lowercase): ')
    race_regex = re.compile(r'(dragonborn|dwarf|elf|gnome|halfling|orc|human|tiefling)') # races that can be validated
    race_source = race_regex.search(race_finder) # searches for race entered by user in regex

    return race_source # returns chosen race to main


def create_alignment(): # user enters alignment from given list
    print()
    alignment = input('What is your alignment? Pick Good, Neutral, or Evil. (in lowercase): ')
    alignment_regex = re.compile(r'''good|neutral|evil''') # alignments that can be validated
    alignment_source = alignment_regex.search(alignment) # searches for alignment entered by user in regex

    return alignment_source # returns alignment to main


def outputs(name_source, class_source, race_source, alignment_source):
    if name_source and class_source and race_source and alignment_source: # validates that outputs are in regexes
        print()
        print('Here is your character breakdown:')
        print('Your name is:', name_source.group().title())
        print('Your class will be:', class_source.group().title()) # prints class chosen
        print('Your race will be:', race_source.group().title()) # prints race chosen
        print('Your alignment will be:', alignment_source.group().title()) # prints alignment chosen
        print()
        print('Have fun playing DnD 5e with your new custom character!')
    else:
        print('That is not a valid character build in DnD 5e') # if inputs are not in regexes, with show a non match


main()
