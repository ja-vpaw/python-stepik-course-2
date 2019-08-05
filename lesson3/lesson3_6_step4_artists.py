import requests
import json

l = list()

with open ( "token.txt", "r") as f:

    token = f.read()

    # создаем заголовок, содержащий наш токен
    headers = {"X-Xapp-Token" : token}

    with open('dataset_24476_4.txt', 'r') as id:

        for line in id:
            address = "https://api.artsy.net/api/artists/" + line.strip()
            # инициируем запрос с заголовком
            r = requests.get(address, headers=headers)

            # разбираем ответ сервера
            j = json.loads(r.text)

            l.append((j['sortable_name'], j['birthday']))

#l.append((('Warhol Bandy', '1928')))
#l.append((('Warhol Aandy', '1928')))


l = sorted(l, key=lambda tup: (tup[1], tup[0]))
for i in l:
    print(i[0])

# year = '0000'
# new_l = []
#
# k = []
#
# for i in l:
#     if i[1] != year:
#         k = []
#         k.append(i[0])
#         year = i[1]
#     else:
#         k.append(i[0])
#         k.sort()
#     print(next(name for name in k))
