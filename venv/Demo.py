import json

data = {
    'name' : 'Connor',
    'sex' : 'boy',
    'age' : 26
}
# print(data)

with open('1.json', 'r')as f:
    data1=f.read()
    data2 = json.loads(data1)
    print(data2)