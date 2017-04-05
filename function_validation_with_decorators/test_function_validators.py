"""
Test module for function validator decorator module by Jackson Cooper.

Original Author:    Jackson Cooper
Article:            Validate Python Function Parameter & Return Types with Decorators
Published at:       http://pythoncentral.io/validate-python-function-parameters-and-return-types-with-decorators/
Published:          Tuesday 20th August 2013 
Last Updated:       Friday 23rd August 2013
"""
from function_validators import *

@accepts(int, int)
@returns(int)
def add_nums_correct(a, b):
    '''
    Adds two numbers. It accepts two
    integers, and returns an integer.
    '''
 
    return a + b
 
 
@accepts(int, int)
@returns(int)
def add_nums_incorrect(a, b):
    '''
    Adds two numbers. It accepts two
    integers, and returns an integer.
    '''
 
    return 'Not an int!'

def main():
    a = 3
    b = 2
    add_nums_correct(a, b)
    
    try:
        add_nums_incorrect(a, b)
    except InvalidReturnType as e:
        print e
    
if __name__ == "__main__":
    main()
