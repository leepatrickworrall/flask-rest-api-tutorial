import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 10, "name": "How To", "views": 3},
    {"likes": 142420, "name": "Carameldansen", "views": 301113},
    {"likes": 12130, "name": "Duck Song", "views": 33131344},
    {"likes": 123230, "name": "Numa Numa", "views": 3442444524}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

response = requests.delete(BASE + "video/0")
print(response, "Video was deleted successfully...")

input()

response = requests.get(BASE + "video/2")
print(response.json())
