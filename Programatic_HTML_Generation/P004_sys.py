import sys

# in terminal run
# python 004_sys.py 123

print(sys.argv)  # ['004_sys.py', '123']
print(sys.argv[1])  # 123
print(sys.argv[0])  # 004_sys.py
print(type(sys.argv))  # <class 'list'>
print(type(sys.argv[0]))  # <class 'str'>