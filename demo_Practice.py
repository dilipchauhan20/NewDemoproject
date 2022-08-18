import json
import jsonpath


file = open("dev-aspen-b5b9a-DialCollection2-export.json", 'r')
json_file = file.read()
json_content = json.loads(json_file)
list1 = []
# print(json_content)

# new_val = jsonpath.jsonpath(json_content, '*.calls[*].callSidGeneratedTimestamp')
new_val = jsonpath.jsonpath(json_content, '*.calls')
# print(new_val)

print(len(new_val))
count = 0

for i in new_val:
    keys = i.keys()
    # print(keys)
    list1.append(keys)

for n in list1:
    print(n)


