import random
import string

x = string.ascii_letters + string.digits + string.punctuation
y = [random.choice(x) for i in range(10)]
y = "".join(y)
y1 = "".join(y)
print(y, y1)
print(y is y1)

one1 = 12345
one2 = 12345
print(one1 is one2)
print(id(one1))
print(id(one2))
print("----" * 20)

one1 = "abc_,*!:"
one2 = "abc_,*!:"
print(one1 is one2)
print(id(one1))
print(id(one2))
print("----" * 20)

one1 = 'abc'
one2 = 'ab' + 'c'
one3 = ''.join(['ab', 'c'])
print(one1 is one2)
print(one1 is one3)
print(id(one1))
print(id(one2))
print("----" * 20)
