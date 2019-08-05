import requests
import json

client_id = '076e5e856017da13848a'
client_secret = 'cd604f1800c00383cc1a18ef73f6d299'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

with open ( "token.txt", "w") as w:

    print(token)
    if token is not None:
        w.write(token)
