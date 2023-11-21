import json

filename = 'input.json'
indent = None  # TODO Подставьте любое целое число
ensure_ascii = False

# TODO решите задачу
def task(dat) -> float:
    s = 0
    for i in dat:
        s +=i["score"] * i["weight"]
    print(round(s,3))


with open(filename) as file:
    data = json.load(file)
task(data)






#