import os

wifi = ('netsh wlan show profiles ')
# name=Hello World key=clear
with os.popen(wifi) as f:
    wifiname_list = []
    for line in f:
        if '所有用户配置文件 :' in line:
            # print(line)
            line = line.strip()
            wifiname = line.split(':')[1]
            wifiname_list.append(wifiname)
    print(wifiname_list)
for i in wifiname_list:
    get = ('netsh wlan show profiles name={} key=clear').format(i)
    with os.popen(get) as r:
        print(r.read())
    r.close()
