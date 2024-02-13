import json

# DICT
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(x["name"])
print(x["children"])
print(x["children"][0])
print(x["cars"][0]["model"])

# some JSON:
x2 = '{ "name":"John", "age":30, "city":"New York"}'
y2 = json.loads(x2)

# JSON
a = json.loads('{"X":"value1","Y":"value2","Z":[{"A":"value3","B":"value4"}]}')
print(a["Z"][0]["A"])
