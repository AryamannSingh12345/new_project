import re
import numpy as np
from random import randint as rand
from math import floor
from collections import Counter

def number_set_generator(num):
    target = '100.25'
    while(eval(target) > 1000 or not(isinstance(eval(target), int))):
        large_numbers = np.floor(np.linspace(range(10, 31, 10)[rand(0, 2)], 40, num = 4))
        #print(large_numbers)
        if(num > 4): return ['Enter a value between 1 and 4', '0', '0']
        no_of_large_numbers = num
        select_large_numbers = num
        small_numbers = np.array([[x,x] for x in np.arange(1, 11, 1)])
        small_numbers = small_numbers.flatten()
        #print(small_numbers)
        pos = rand(0,13)
        number_set = np.append(large_numbers[0:select_large_numbers],small_numbers[pos:(pos + (6 - select_large_numbers))])
        print(number_set)
        bracket_pos = rand(0, 1)
        bracket1 = ['', '(']
        bracket2 = ['', ')']
        operators = ['+', '*']
        operators2 = ['+', '/', '*']
        operators3 = ['+', '-', '*']
        number_set = np.char.mod('%d', number_set)
        target = bracket1[bracket_pos] + bracket1[bracket_pos] + number_set[0] + operators2[rand(0,2)] + number_set[1] + operators[rand(0,1)] + number_set[2] + bracket2[bracket_pos] + operators2[rand(0,1)] + number_set[0] + operators[rand(0,1)] + number_set[3] + operators[rand(0,1)] + number_set[4] + bracket2[bracket_pos] + operators3[rand(0,2)] + number_set[5]
        print(number_set)
    return [number_set, target, eval(target)]
def is_correct(string, number_set, target_value):
    regex = r'[0-9]+'

    found = re.findall(regex, string)
    if (found):
        x = Counter(found)
        y = Counter(number_set)
        if(eval(string) ==  target_value and x == y):
            return 10
        elif(0 < (abs(eval(string) - target_value)) <= 5 and x==y):
            return 7
        elif(5<(abs(eval(string) - target_value))<=10 and x==y):
            return 5
        else:
            return 0
