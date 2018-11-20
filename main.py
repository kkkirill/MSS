# CL - total number of 'if'
# cl - (total number of operators)/CL
# CLI - max number of depth

import re

f = open('code.txt', 'r')

text = f.read()  # code (str)
f1 = open('roperators.txt', 'r')
ops = f.readlines()  # operators (list)

text = re.compile(r"[#][^\n]*").sub("", text)  # delete all comments
text = re.compile(r"<.*>").sub("< >", text)  # delete all inside <...>
text = re.compile(r"\"(.*)\"").sub("", text)  # delete all strings

#sth = sorted(re.compile(r"(?:(?:(?:(?:(?:[\w+\.\[\]])*)[:.])+)|(?:[ ]))*[\w\-]*\(").findall(text), reverse=True)
sth = sorted(re.compile(r"(?:(?:(\w+::)+)?(?:\w+?(?:\.\w+)+\(+|\w+\())").findall(text), reverse=True)

sth = list(filter(None, [re.sub(r"^:\w+\(", r"", i) for i in sth]))
operators = len(sth)

pattern = re.compile(r"(\s((?:if|unless|elsif|while|for|until)[^{^\n;]*(?:;|{|)*)|((?:case \d|else)\s*[{]*))")

conditions = [[m.start(), m.end(), m.group(1)] for m in re.finditer(pattern, text)]

CL = len(conditions)
print("Total number of conditions - " + str(CL))
print("cl - " + str(operators/CL))

temp_num_of_all_brackets = text[:conditions[0][1]].count('{') - text[:conditions[0][1]].count('}')  # num of all brackets
listing = [temp_num_of_all_brackets]  # list for calculating depth
max_count = 0  # max depth

for i in range(len(conditions) - 1):
    num_of_open_brackets, num_of_close_brackets = text[conditions[i][1]:conditions[i+1][0]].count('{'), \
                                                  text[conditions[i][1]:conditions[i+1][0]].count('}')
    amount_of_brackets = num_of_open_brackets + num_of_close_brackets

    if conditions[i][2].find('{') != -1:
        listing.append(num_of_open_brackets + 1)
    else:
        listing[len(listing) - 1] += num_of_open_brackets
    temp = len(listing) - 1
    if temp - 1 > max_count:
        max_count = temp - 1
    listing[temp] -= num_of_close_brackets
    while listing[temp - 1] < 0:
        temp -= 1
        listing[temp] = listing[temp] + listing[temp + 1]
        listing.pop()
        if listing[temp] == 0:
            listing.pop()

print("Max depth of conditions - " + str(max_count))