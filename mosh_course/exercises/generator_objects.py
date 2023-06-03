from sys import getsizeof

values = (x * 2 for x in range(10000))
print("gen_obj", getsizeof(values))

values = [x * 2 for x in range(10000)]
print("list:", getsizeof(values))