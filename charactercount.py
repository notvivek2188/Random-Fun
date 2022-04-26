import pprint

print("Enter your message here:")
mssage = str(input())
count = {}

upperrcase = mssage.upper()

for character in upperrcase:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
