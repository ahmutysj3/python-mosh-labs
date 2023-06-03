point = {"x":1, "y":2}
print(point)

point = dict(x=1, y=2)
print(point)
print(point["y"])

point["x"] = 3
print(point)

point["z"] = 4
print(point)


print(point.get("z"))

if "a" in point:
    print(point["a"])
    print("it's in there")
else:
    print("it's not in there")
    
print(point.get("b", 0))

del point["x"]
print(point)

for key in point:
    print(key,point[key])
    
print(point.items())

for key, value in point.items():
    print(key,value)