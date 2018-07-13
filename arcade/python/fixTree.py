"""
Easy

Recovery

100

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Not long ago a young Christmas elf asked you to implement a function that creates Christmas trees made of asterisks ('*') similar to the one below:

    *    
    *    
   ***   
  *****  
 ******* 
*********
   ***   
Unfortunately because of the extreme coldness the tree that you sent over was corrupted: although its lines are given in the correct order, but are not aligned properly. Now your task is to fix the given tree by centering the asterisks in each line.

Example

For

tree = [
  "      *  ", 
  "    *    ", 
  "***      ", 
  "    *****", 
  "  *******", 
  "*********", 
  " ***     "
]
the output should be

fixTree(tree) = [
  "    *    ", 
  "    *    ", 
  "   ***   ", 
  "  *****  ", 
  " ******* ", 
  "*********", 
  "   ***   "
]
"""


def fixTree(tree):
    return [p.strip().center(len(p)) for p in tree]
