# Import JSON module to allow user to "read and write" the JSON file
import json

# Input message in terminal
string = str(input())

# Output message as a string
print(string)

# Open local JSON file (r+ means read and write)
with open('complimentsA.json', 'r+') as f:
    data = json.load(f)

# Insert output message into each respective category   
    data['anytime'] = string
    data['morning'] = string
    data['afternoon'] = string
    data['evening'] = string
   
# Reset file position to beginning   
    f.seek(0)

# Insert data in file by converting python object to json object  
    json.dump(data, f, indent=2)
   
# Remove remaining part   
    f.truncate()

