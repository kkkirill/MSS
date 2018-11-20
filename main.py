# CL - total number of 'if'
# cl - (total number of operators)/CL
# CLI - max number of depth

import re


f = open('code.txt', 'r')
#####################
# CL = 0
# CLI = 0
# total_count = 0
# count = 0
# flag = False
# bracket = False
# list_str = f.readlines()
#
#
#
# for i in list_str:
#     i = i.lstrip()
#     if flag is True:
#         if i.startswith('if ') or i.startswith('unless ') or i.startswith('elsif '):
#             count += 1
#         else:
#             flag = False
#     if i.startswith('if ') or i.startswith('unless ') or i.startswith('elsif '):
#         flag = True
#     if i.find('{') != -1:
#         if flag is True:
#             count += 1
#             if count > CLI:
#                 CLI = count
#             flag = False
#         else:
#             total_count += 1
#     if i.find('}') != -1:
#         if total_count != 0:
#             total_count -= 1
#         else:
#             count -= 1
# text = str(list_str)
# CL = text.count('if ')
# CL += text.count('unless ')
# CL += text.count('elsif ')
# CL += text.count('case ')
# CLI -= 1
# print(CL)
# print(CLI)
#####################3

text = f.read()  # code (str)
f1 = open('roperators.txt', 'r')
ops = f.readlines()  # operators (list)

text = re.compile(r"[#][^\n]*").sub("", text)  # delete all comments
text = re.compile(r"<.*>").sub("< >", text)  # delete all inside <...>
sth = sorted(re.compile(r"(?:(?:(?:(?:(?:[\w+\.\[\]])*)[:.])+)|(?:[ ]))*[\w\-]*\(").findall(text), reverse=True)
sth = list(filter(None, [re.sub(r"^:\w+\(", r"", i) for i in sth]))
operators = len(sth)


#print('switch (a) { case 1 {}\\ncase 2{}\\ncase 3 {}\\nelse {}}has $!name;method archetypes() {$archetypes};method add_method($obj, $name, $code_obj) { if')
pattern = re.compile(r"(\s((?:if|elsif|while|for|until)[^{^\n;]*(?:;|{|)*)|((?:case \d|unless|else)\s*[{]*))")


foundlist = [[m.start(), m.end(), m.group(1)] for m in re.finditer(pattern, text)]
print(foundlist)
depth = []
amount_of_attachments = 0   # depth
temp_num_of_brackets = 0  # if brackets
temp_num_of_all_brackets = text[:foundlist[0][1]].count('{') - text[:foundlist[0][1]].count('}')  # all brackets
listing = [temp_num_of_all_brackets]
for i in range(len(foundlist) - 1):
    num_of_open_brackets, num_of_close_brackets = text[foundlist[i][1]:foundlist[i+1][0]].count('{'), text[foundlist[i][1]:foundlist[i+1][0]].count('}')
    amount_of_brackets = num_of_open_brackets + num_of_close_brackets
    #print(text[foundlist[i][1]:foundlist[i+1][0]].count('}'))

    if foundlist[i][2].find('{') != -1:
        temp_num_of_brackets += 1
    listing.append(num_of_open_brackets + 1 if foundlist[i][2].find('{') != -1 else 0)
    temp = len(listing) - 1
    while listing[temp] < 0:
        listing[temp] -= num_of_close_brackets
        if listing[temp] < 0:
            temp -= 1
            listing[temp] = listing[temp] + listing[temp + 1]
            listing.pop()
        elif listing[temp] == 0:
            listing.pop()

    if (amount_of_brackets % 2 != 0 or amount_of_brackets == 0) and (num_of_close_brackets < num_of_open_brackets + 1):
        amount_of_attachments += 1
    # elif text[foundlist[i][1]:(text[foundlist[i][1]:foundlist[i+1][0]].find('}'))].count('{') == 0:
    #     if text[foundlist[i][1]:(text[foundlist[i][1]:foundlist[i+1][0]].find('}'))].count('}') == temp_num_of_brackets:
    #         depth.append(amount_of_attachments)
    #         temp_num_of_brackets = 0
    #         amount_of_attachments = 0

print()
print(depth)
# depth = 0
# i1, i2 = 0, re.search('', text)
#
# amount_of_iters = len(re.findall(pattern, text))
# nestlist = []
#
# for x in range(100):
#     i2 = i1 + i2.start()  # change i2 because it counting in slice and i2 not true value (old i2, i. e. from last iter)
#     i1 = i2 + re.search(pattern, text[i2:]).end()  # same as 1 up
#     i2 = re.search(pattern, text[i1:])  # count new i2
#     if i2 is None:
#         break
#     print(i1, i1 + i2.end(), text[i1:i1 + i2.start()], len(text[i1:i1 + i2.start()]))
#     amount = len(re.findall(r"[{}]", text[i1:i1 + i2.start()]))
#     if (amount == 0 or amount % 2 == 0) and abs(text[i1:i1 + i2.start()].count('}') - text[i1:i1 + i2.start()].count('{')) < 2:
#         depth += 1
#     elif text[i1:i1 + i2.start()].count('}') > text[i1:i1 + i2.start()].count('{'):
#         #depth += 1
#         nestlist.append(depth)
#         depth = 0

# print(nestlist)
# print(max(nestlist))



#pattern = re.compile(r"(((\w+::)+)?(\w+?(\.\w+)+\(+|\w+\())")
#sth2 = pattern.findall(text)

#for i in range(len(sth2)):
#    sth2[i] = sth2[i][0]

#((\.\w+)+\()?

#((\w+::)+)?(\w+?(\.\w+)+\(?|\w+\()
#print(sth)