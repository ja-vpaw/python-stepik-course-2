import json

#json_str = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]' #\
              #{"name": "D", "parents": ["B"]}]'

json_str = input()

json_data = json.loads(json_str)

already_handle = dict()

switch = True
while switch:
    switch = False

    for i in json_data:

        try:
            already_handle[i['name']].add(i['name'])
        except KeyError:
            already_handle[i['name']] = set()
            already_handle[i['name']].add(i['name'])

        for parent in i['parents']:
            try:
                already_handle[parent].add(i['name'])
            except KeyError:
                already_handle[parent] = set()
                already_handle[parent].add(i['name'])

            for item in already_handle.keys():
                #print(already_handle)
                if parent in already_handle[item] and i['name'] not in already_handle[item]:
                    already_handle[item].add(i['name'])
                    switch = True

#print(sorted(already_handle.items()))

for i in sorted(already_handle.keys()):
    print(i, ':', len(already_handle[i]))