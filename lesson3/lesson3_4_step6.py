import requests
import re

a = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
b = "https://stepic.org/media/attachments/lesson/24472/sample2.html"

#a = input()
#b = input()

status='No'

res = requests.get(a)
if res.status_code == 200:
    list_links = re.findall('href=".*"',res.text)
    for i in list_links:
        #print(i.split('"')[1])
        res_a = requests.get(i.split('"')[1])
        if res.status_code == 200:
            #print(res_a.text)
            if b in res_a.text:
                status='Yes'
    print(status)
else:
    print(status)
