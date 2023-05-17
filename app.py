items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

result = list(filter(lambda item: item[1] <= 10, items))
print(result)

result2 = [item for item in items if item[1] <= 10]
print(result2)

list1 = [2 , 4 , 6]
list2 = [10, 20, 30]
print(list(zip("abc",range(3),list1,list2)))

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
browsing_session.pop()
print("last number in browsing session stack", browsing_session[-1])
