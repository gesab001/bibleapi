import json

f = open("booklist.json", "r")
json_data = json.loads(f.read())
list = {}
totalbooks = len(json_data["books"])
books = json_data["books"]
new_json_data = {}
print(totalbooks)
for x in range(0, totalbooks):
  book = books[x]["name"]
  booknumber = x+1
  print(str(booknumber))
  print(book)
  new_json_data[book] = str(booknumber)

print(new_json_data)
with open("booklist2.json", "w") as outfile:
  json.dump(new_json_data, outfile)

