import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 69, "name": "How To", "views": 5353},
    {"likes": 2525, "name": "Duck Song", "views": 585222},
    {"likes": 596214, "name": "Numa Numa", "views": 21235231}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), json=data[i])
    print(response.json())

input()

response = requests.get(BASE + "video/2")
print(response.json())

# If I add 'db.create_all()' to the main.py file, run it, and then remove the
# line, the database doesn't populate correctly. However, if I manually start
# a Python shell and type `from main import db` and then on the next line type
# 'db.create_all()' again, the database is created and populated.

# I have no idea.

# However, if I add 'from main import db' into the `main.py` file, the location
# of where the database should be created, it says how I am trying to import
# that module from the same file, due to the line 'db = SQLAlchemy(app)' but
# it has shown how that doesn't work.

# So from the tutorial we are using, it must be deprecated, or a step must've
# been skipped.
