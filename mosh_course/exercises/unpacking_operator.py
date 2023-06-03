numbers = [1,2,3]
print(numbers)
print(1,2,3)
print(*numbers)

print(range(5))
values = list(range(5))
print(values)

print(*range(5),*"trace")


first = [1,2]
second = [3]
values = [*first,"a",*second]
print(values)

first = {"x":1}
second = {"x":10, "y":2}
combined = {**first, **second}
print(combined) # this one works

bad = {first, second} #results in error
print(bad) #results in error