'''
Author: Trisha Kaye Wong, Gerson Ortega
Filename: LR2_2.py
Program Description: This program takes the input of the file name of a .txt file and evaluates the number of lines within the
file. The user can select which line they want to output. 
'''

openfile = input("Enter the file name: ")
file = open(openfile, 'r')
linecount = 0
for line in file:
    linecount = linecount + 1

print("\nThe number of lines in this file is", linecount, "...")

while True:
    no = 0
    num = int(input("\nEnter line number or press 0 to quit: "))

    if num >=1 and num <= linecount:
        file = open(openfile, 'r')
        for lines in file:
            no = no + 1
            if no == num:
                print(lines)

    else: 
        if num > linecount or num < 0:
            print("\nInvalid line number! Input numbers up to", linecount, "only.")
        if num == 0:
            print("\nThank you for using the Program.")
            break
    