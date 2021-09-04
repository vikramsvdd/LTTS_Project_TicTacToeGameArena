import re

fp = open("reffile.txt")
for lineparse in fp:
    if re.search(r"9009123546", lineparse):
        print(lineparse.rstrip())


fp.close()
