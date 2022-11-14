import json

# Input message
string = str(input())

# Output message as a string
print(string)

# open local JSON file & insert string as an "anytime" compliment
with open('complimentsA.json', 'r+') as f:
    data = json.load(f)
    data['anytime'] = string
    f.seek(0)
    json.dump(data, f, indent=2)
    f.truncate()

