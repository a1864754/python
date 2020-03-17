import requests

url = "http://api.mosoteach.cn/mssvc/index.php/ccfile/get_file_url"
r = requests.get(url)
for i in r:
    print(i)
type(r)
