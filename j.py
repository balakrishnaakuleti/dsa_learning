from json import dumps, load, dump

# JSON data
data = { "name": "John", "age": 30, "city": "New York" }
with open("./data.json", "w") as file:
    dump(data, file, indent=4)


with open("./data.json", "r") as file:
    data = load(file)
    print(data)
