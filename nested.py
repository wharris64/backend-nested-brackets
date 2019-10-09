#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "wharris64"

import sys
openers = [ "(", "[", "{", "<", "(*"]
closers = [")", "]", "}", ">", "*)"]
def check_brackets(line):
    currentbracket = []
    temp_openers = []
    temp_closers = []
    counter = 0
    while(line):
        if line.startswith("(*"):
            token = "(*"
            counter += 1

        elif line.startswith("*)"):
            token = "*)"
            counter += 1
        elif line.startswith("<*"):
            token = "<*"
            counter +=1
        else:
            counter += 1
            token = line[0]
        line = line[len(token):]
        if token in openers:
            
            # currentbracket.append(token)
            temp_openers.append(openers.index(token))
        elif token in closers:
            
            # currentbracket.append(token)
            temp_closers.append(closers.index(token))
    if temp_openers != temp_closers[::-1]:
        no = "no"
        counter -= 1
        counter = str(counter)
        return counter
    else:
        return('YES')
        # start_line = line.startswith["(*"]
        # end_line = line.startswith['*)']
        # for char in line:
        #     if char in openers:
        #         currentbracket.append(char)
        #         print(currentbracket)
        #         temp_openers.append(openers.index(currentbracket[index])) 
        #         index += 1
        #     elif char in closers:
        #         currentbracket.append(char)
        #         temp_closers.append(closers.index(currentbracket[index]))
        #         index += 1
        
        # if temp_openers == temp_closers[::-1]:
        #     print("YES")
        #     return "YES"
        
        # else:
        #     # find index of error
        #     print('No')
        #     return "No" 
        #         # and number
        # # and number


def read_file(filename):
    with open(filename) as reader, open("output.txt", "w")as writer:
            content = reader.readlines()
            # content = [x.strip( ) for x in content]
            for i in content:
                # check_brackets(i)
                 writer.write(check_brackets(i) + "\n")
    

def main(args):
    """Add your code here"""
    read_file(args[1])
    

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
    

if __name__ == '__main__':
    main(sys.argv)
