#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025: Day 3
Created on Tue Dec  9 10:10:15 2025
@author: mrutala

--- Day 3: Lobby ---

You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint. When you get to the main elevators, however, you discover that each one has a red light above it: they're all offline.

"Sorry about that," an Elf apologizes as she tinkers with a nearby control panel. "Some kind of electrical surge seems to have fried them. I'll try to get them online soon."

You explain your need to get further underground. "Well, you could at least take the escalator down to the printing department, not that you'd get much further than that without the elevators working. That is, you could if the escalator weren't also offline."

"But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."

There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled with their joltage rating, a value from 1 to 9. You make a note of their joltage ratings (your puzzle input). For example:

987654321111111
811111111111119
234234234234278
818181911112111

The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

You'll need to find the largest possible joltage each bank can produce. In the above example:

    In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
    In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
    In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
    In 818181911112111, the largest joltage you can produce is 92.

The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.

There are many batteries in front of you. Find the maximum joltage possible from each bank; what is the total output joltage?

--- Part Two ---

The escalator doesn't move. The Elf explains that it probably needs more joltage to overcome the static friction of the system and hits the big red "joltage limit safety override" button. You lose count of the number of times she needs to confirm "yes, I'm sure" and decorate the lobby a bit while you wait.

Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.

The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be 12 digits in each bank's joltage output instead of two.

Consider again the example from before:

987654321111111
811111111111119
234234234234278
818181911112111

Now, the joltages are much larger:

    In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
    In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
    In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
    In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.

The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.

What is the new total output joltage?

"""

part_one = True
part_two = False

target_length = 12

# # Test inputs
# inputs = ['987654321111111',
#           '811111111111119',
#           '234234234234278',
#           '818181911112111']

# Real inputs
with open('/Users/mrutala/projects/Advent-of-Code-2025/inputs/AoC2025_Day3_input.txt', 'r') as file:
    inputs = [line.rstrip() for line in file]

# Iterate over banks, tracking the biggest 2-battery pairs in each bank
biggest_sets = []
for bank in inputs:
    
    largest_set = ''
    remaining_bank = bank
    
    while(len(largest_set) < target_length):
    
        # # Track the biggest pair in each permutation of this bank
        # biggest_set = 0
        
        print(largest_set)
    
        # Find the largest value in this bank, which is at least target_length from the end
        # Due to indexing quirks, this works until target_length - len(largest_set) = -1
        if len(largest_set) < target_length-1:
            possible_batteries = [b for b in remaining_bank[:-(target_length - len(largest_set))+1]]
        else: 
            possible_batteries = [b for b in remaining_bank]
       
        largest_value = max(possible_batteries)
        
        # index returns the first (leftmost) instance only
        largest_value_index = possible_batteries.index(largest_value)
        
        # Add the largest value to the tracker
        largest_set += largest_value
    
        # Now remove everthing before and including largest_value_index, and check for the next largest
        remaining_bank = remaining_bank[largest_value_index+1:]
        
    biggest_sets.append(int(largest_set))
    
    # for i, battery in enumerate(bank[:-1]):
        
    #     # Combine the ith battery with each following battery
    #     sets = [battery + b for b in bank[i+1:]]
        
    #     breakpoint()
        
    #     # If the result is larget than the current biggest pair, keep it instead
    #     if int(max(pairs)) > biggest_pair:
    #         biggest_pair = int(max(pairs))
            
    # biggest_pairs.append(biggest_pair)
            
    
print("Total Output Joltage: {}".format(sum(biggest_sets)))
        

