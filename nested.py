#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.

Part 1: Open and read the file of test strings
Part 2: Call the `is_nested` function with each test string
"""
__author__ = "mosaafir74"

import sys


openers = ['[','(','{','(*','<']
closers = [']',')','}','*)','>']

'''
def valid_parentheses(string):
    stack=[]
    for n in string:
        if n == "(":
            stack.append(n)   
        if n == ")":            
            if len(stack) == 0 or stack.pop() != "(":
                return False
    if len(stack) !=0:
        return False
    return True
'''

def is_nested(s):
    stack = []
    for n in s:
        if n in openers:
            stack.append(n)
        if n in closers:  # for example, `}`
            matching_opener = openers[closers.index(n)]
            if len(stack) == 0 or stack.pop() != matching_opener:
                return "NO "
    if len(stack) !=0:
        return "NO "
    return "Yes "


    # for char in s:
    #   print(char, end=' ', flush=True)

    while s:
        token = s[0]
        if s[:2] == '(*':
            token = '(*'
        if s[:2] == '*)':
            token = '*)'
        #print(token, sep=' ', flush=True)
        s = s[len(token):]

def main():
    
    # open the input file
    # k =open('input.txt')
    # for line in k:
    #     print(line)
    # k.close()

    with open('input.txt') as infile:
        for line in infile:
            result = is_nested(line)
            print (result)
            #print(line)

    pass  # Guaranteed now that k gets closed automatically
    #k.close()
    

if __name__ == '__main__':
    main()
def valid_parentheses(string):
    stack=[]
    for n in string:
        if n == "(":
            stack.append(n)   
        if n == ")":            
            if len(stack) == 0 or stack.pop() != "(":
                return False
    if len(stack) !=0:
        return False
    return True