from pathlib import Path

path = Path("../import_packages/packages/ecommerce")
print(path.exists())

""" path = Path("test_dir_python")
path.rmdir() """

path = Path()
# print(path.glob("*.*")) # this will return a generator object

for file in path.glob("*.py"):
    print(file)