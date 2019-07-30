import requests
import re

# Test 3
link = "http://pastebin.com/raw/7543p0ns"

# Test 2
#link = "http://pastebin.com/raw/hfMThaGb"

# For Test 2
text = '''
<a href=\"http://stepic.org/courses\">
<a href=\"ftp://www.mya.ru\">
<a href='https://stepic.org'>
<a link href='http://neerc.ifmo.ru:1345'>
<a target=\"blank\" href='http://sasd.ifmo.ru:1345'>
<a href='http://neerc.ifmo.ru:1345'>
<a href=\"../some_path/index.html\">
<a href=\"https://www.ya.ru\">
<a href=\"ftp://mail.ru/distib\" >
<a href=\"bya.ru\">
<a href=\"http://www.ya.ru\">
<a href=\"www.kya.ru\">
<a href=\"../skip_relative_links\">
<a href="http://turbo.ru/">Turbo.ru</a>
<a href="http://drink-time.ru">DrinkTime.ru</a>
<a href="/users/79/def" class="top-link ember-link">
<a site=? href=s-http://www1.work.site.com/def#!-/cgi?=12:8080
<a href='https://www-abc.com.uk:443'
<a ver-m_n=1 href="smb://192.168.1.1/file"</a>
<a role="button" class="toggle link link_style"></a>
<a link rel="icon" sizes="32x32" href="/static/icon32.png?v=59">
<a site=? href=s-http://www1.work.site.com>
<a site=? href=s-http://qwe1-rty2.zzz>
<a href="http://valid1.site/redirect.cgi?http://valid2.site
<a href="http://redir.rbc.ru/cgi-bin/redirect.cgi?http://hc.ru/ru/">Хостинг</a>
<a title=test class="my test" href= "test1.com:8080/test/path?get=http://test2.ru/?true"; rel="nofollow" style=>
<a title=test meta="whatever http://test1.com"; href = "test.com?get=http://test2.ru/?true"; class="my test" style= >
"
'''

domens = set()

#link = input()

res = requests.get(link)
if res.status_code == 200:

    list_links = re.findall('<a.*href=.*', res.text)
    for i in list_links:
        a=None
        print(i)
        if '@' not in i:
            pattern1 = r'\?(.*://.*)'
            if re.search(pattern1, i):
                i = re.sub(pattern1, "", i)
            print(i)
            pattern2 = r'src(.*://.*)'
            if re.search(pattern2, i):
                i = re.sub(pattern2, "", i)
            print(i)
            a = re.match(r".*href=(\"|\')+(.*://)*(\w((\w|\.|\-)+))", i)
        if a:
            print(a.group(3))
            domens.add(a.group(3))
            print()



# res = requests.get(link)
# if res.status_code == 200:
#
#     list_links = re.findall('(<a.*href=".*?" )', res.text)
#     print(list_links)
#     for i in list_links:
#         print(i)
#         # if '@' not in i:
#         #     a = re.match(r"(.*://)*(\"|\'|\=)*(\w((\w|\.|\-)+))", i.split('href')[1].split('>')[0].split('?')[0])
#         # else:
#         #     a = None
#         # if a:
#         #     print(a.group(3))
#         #     domens.add(a.group(3))
#         #     print()
#
#
with open("text.txt", "w") as f:
    for i in sorted(domens):
        f.write(i+"\n")


# # Test 2
#
# list_links = re.findall('href=.*',text)
# for i in list_links:
#     print(i)
#     a = re.match(r"href=(.*://)*(\"|\')*(\w((\w|\.|\-)+))", i)
#     print(a)
#     if a:
#         print(a.group(3))
#         domens.add(a.group(2))
#     print()


# for i in sorted(domens):
#      print(i)
