"""
(e) Predict the output: 
def divide(a, b):     
    if b == 0: 
        raise ZeroDivisionError('Cannot divide by zero')     
    return a / b 
try:     
    print(divide(10, 2))     
    print(divide(5, 0)) 
except ZeroDivisionError as e:     
    print(f'Caught: {e}') 
"""
def divide(a, b):     
    if b == 0: 
        raise ZeroDivisionError('Cannot divide by zero')     
    return a / b 
try:     
    print(divide(10, 2))     
    print(divide(5, 0)) 
except ZeroDivisionError as e:     
    print(f'Caught: {e}') 