import random
import string

x = string.ascii_letters + string.digits + string.punctuation
y = [random.choice(x) for i in range(1000)]
y = "".join(y)
print('生成的1000个随机字符：', y)
d = dict()
for ch in y:
    d[ch] = d.get(ch, 0) + 1
for k, v in d.items():
    print(k, '出现的次数：', v)
