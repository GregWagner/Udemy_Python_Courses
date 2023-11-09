jabber = open("sample.txt", 'r')

for line in jabber:
    print(line, end='')

jabber.close()

print('-' * 40)

with open("sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        if "jabberwock" in line.lower():
            print(line, end='')
        line = jabber.readline()
