items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

result = list(map(lambda item: item[1], items))
print(result)
