from array import array

numbers = array("i",[1,2,3])
numbers[0] = 1.0 # produces error
print(numbers[0]) # produces error