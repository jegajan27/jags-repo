
'''def test_func( funct, *args ):
    funct( *args )
def printer_one( arg ):
    return print (arg)
def printer_two( arg ):
    print(arg)
#CALL A REGULAR FUNCTION 
test_func( printer_one, 'printer 1 REGULAR CALL' )
test_func( printer_two, 'printer 2 REGULAR CALL \n' )
#CALL A REGULAR FUNCTION THRU A LAMBDA
test_func(lambda: printer_one('printer 1 LAMBDA CALL'))
test_func(lambda: printer_two('printer 2 LAMBDA CALL'))

sequences = [10,2,8,7,5,4,3,11,0, 1]
#filtered_result = filter (lambda x: x >= 4, sequences)
filtered_result = map (lambda x: x*x, sequences)  
print(list(filtered_result))
'''
from functools import reduce
sequences = [1,2,3,4,5]
product = reduce (lambda x, y: x-y, sequences)
print(product)
print("Hello New")