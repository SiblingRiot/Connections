import sys

# open local JSON file
sys.stdout=open("complimentsA.json","w")

# input
string = str(input())
  
# output
print(string)

# save output to file
sys.stdout.close()

