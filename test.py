import json

string = str(input())

print(string)

# open local JSON file
with open('complimentsA.json', 'r+') as f:
    data = json.load(f)
    data['anytime'] = string
    f.seek(0)
    json.dump(data, f, indent=2)
    f.truncate()
