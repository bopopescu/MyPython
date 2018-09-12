import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import requests
r = requests.get('https://www.douban.com/')
print(r.status_code)


r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
r.url
print(r.status_code)

r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.text)

r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(r.status_code)


import chardet
data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

import psutil
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))

# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))


psutil.virtual_memory()
psutil.swap_memory()

psutil.disk_partitions()
psutil.disk_usage('/')
psutil.disk_io_counters()

psutil.net_connections()