numbers = [1,1,2,4]
numbers[2] = 3

first = set(numbers)
print(first)

second = {1,5}
print(second)

union = first | second
print(union)

both = first & second
print(both)

difference = first - second
print(difference)

either = first ^ second
print(either)

if 1 in first:
    print("its in there")