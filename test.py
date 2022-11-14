# Import JSON module to allow user to "read and write" the JSON file
import json

# Input message in terminal
string = str(input())

# Output message as a string
print(string)

# open local JSON file & insert string as an "anytime", "morning", "afternoon", and "evening" compliment at the beginning of the JSON file (r+ means read and write)
with open('complimentsA.json', 'r+') as f:
    data = json.load(f)
    data['anytime'] = string
    data['morning'] = string
    data['afternoon'] = string
    data['evening'] = string
    f.seek(0)
    json.dump(data, f, indent=2)
    f.truncate()

