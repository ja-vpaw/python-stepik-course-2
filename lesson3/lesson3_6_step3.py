import requests

params = {
    'json': 'true'
}

with open("dataset_24476_3.txt", "r") as f, open ( "answer.txt", "w") as w:

    for number in f:

        api_url = "http://numbersapi.com/" + str(number).strip() + "/math"
        #print(api_url)

        res = requests.get(api_url, params=params)
        #print(res.status_code)
        #print(res.headers["Content-Type"])
        #print(res.json())  # returns json.loads(res.text) :)

        data = res.json()
        if data['found'] == True:
            w.write('Interesting\n')
        elif data['found'] == False:
            w.write('Boring\n')
        #template = 'Current temperature in {} is {}'
        #print(template.format(city, data["main"]["temp"]))
