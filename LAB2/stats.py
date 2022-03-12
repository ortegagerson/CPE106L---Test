"""
Author: Lianne Joyce D. Leynes
Filename: stats.py
Define these functions for median and mode in a module named stats.py. Also include a function named mean, which computes the average of a set of numbers. 
Each function should expect a list of numbers as an argument and return a single number. Each function should return 0 if the list is empty. 
Include a main function that tests the three statistical functions with a given list.
"""
import os
import time



def main():
    list_num = [4 , 2, 4, 3, 2, 2]
    print("Please Choose Here: \n(1) - Mean\n(2) - Median\n(3) - Mode\n")
    ans = int(input());

  

    if ans == 1:
        ans_mean = compute_mean(list_num)
        print("The mean of the List is: ",ans_mean)
    elif ans == 2:
        ans_median = compute_median(list_num)
        print("The median of the List is: ",ans_median)
    elif ans == 3:
        ans_mode = compute_mode(list_num)
        print("The mode of the List is: ",ans_mode)
    else:
        print("Not Within the Choices..\n")
        time.sleep(.55)
        os.system('cls')
        main()



def compute_median(list_num):

    if len(list_num) == 0:
        return 0
    else:
        list_num.sort()
        midpoint = len(list_num) // 2
        if len(list_num) % 2 == 1:
            return list_num[midpoint]
        else:
            return (list_num[midpoint] + list_num[midpoint - 1]) / 2

def compute_mode(list_num):

    if len(list_num) == 0:
        return 0
    else:
        y = {}
        for a in list_num:
            number = y.get(a,None)
            if number == None:
                y[a] = 1
            else:
                y[a] = number + 1

        theMaximum = max(y.values())
        for key in y:
            if y[key] == theMaximum:
                return key
                break

def compute_mean(list_num):
    
    if len(list_num) == 0:
        return 0
    else:
        get_sum = sum(list_num)
        n = len(list_num)
        mean = get_sum/n
        return mean


main()


