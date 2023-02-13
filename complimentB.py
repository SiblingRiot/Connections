# Import JSON module to allow user to "read and write" the JSON file
import json

compliments=[]

# Input message in terminal
string = str(input())

# Check and push to json file


# Clean up the string
newstring = string.rstrip()

# Output message as a string
print(newstring)

compliments.append(newstring)

# Open local JSON file (r+ means read and write)
with open('complimentsB.json', 'r+') as f:
    data = json.load(f)

# Assign string value into "anytime"
    data['anytime'] = compliments
   
# Reset file position to beginning   
    f.seek(0)

# Insert doutput message in file by converting python object to json object  
    json.dump(data, f, indent=2)
   
# Remove remaining part   
    f.truncate()

