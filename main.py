# CL - total number of 'if'
# cl - (total number of operators)/CL
# CLI - max number of attachments

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

text2 = f.read()




text = f.read()  # code (str)
f1 = open('roperators.txt', 'r')
ops = f.readlines()  # operators (list)

text = re.compile(r"[#][^\n]*").sub("", text)  # delete all comments
text = re.compile(r"<.*>").sub("< >", text)  # delete all inside <...>
sth = sorted(re.compile(r"(?:(?:(?:(?:(?:[\w+\.\[\]])*)[:.])+)|(?:[ ]))*[\w\-]*\(").findall(text), reverse=True)
sth = list(filter(None, [re.sub(r"^:\w+\(", r"", i) for i in sth]))
operators = len(sth)


#print('switch (a) { case 1 {}\\ncase 2{}\\ncase 3 {}\\nelse {}}has $!name;method archetypes() {$archetypes};method add_method($obj, $name, $code_obj) { if')
pattern = re.compile(r"\s((if|elsif)[^{]*|case \d|unless|else)\s{*")
# conditions with symbols in conditions !!!!!

# buf = 0
# for i in range(10):
#     temp = re.search(pattern, text2[buf:])
#     buf = buf + temp.end()
#     print(temp)

#mas = re.finditer(pattern, text2)
# for elem in pattern.finditer(text2):
#     print(elem.start(), elem.end(), elem.group(1))
#     i1 = text2.count('{', elem.end(), 1720)
#     i2 = text2.count('}', 34, 1720)
#     print(i1, i2)
#     if i1 - i2 % 2 != 0:
#         print('OK')
#     else:
#         print('NOT OK')
# print(text2[34]



# for x in range(10):
#     i2 = i1 + i2.end()
#     i1 = i2 + re.search(pattern, text2[i2:]).end()
#     i2 = re.search(pattern, text2[i1:])
#     #print(text2[i1:i1 + i2.start()])
#     print(i1, i1 + i2.end(), text2[i1:i1 + i2.start()], len(text2[i1:i1 + i2.start()]))
#     amount = len(re.findall(r"[{}]", text2[i1:i1 + i2.start()]))
#     if amount == 0:
#         depth += 1
#     elif amount % 2 == 0 and text2[i1:i1 + i2.start()].count('{') < text2[i1:i1 + i2.start()].count('}'):
#         depth += 1
#     elif amount % 2 != 0:
#         if len(re.findall(r"[{}]", text2[text2[i1:i1 + i2.start()].rfind('}'):i1 + i2.start()])) == 0:
#             depth += 1
#     print('----------------------------------------------')
#
# print(depth)

depth = 0
i1, i2 = 0, re.search('', text2)

amount_of_iters = len(re.findall(pattern, text2))
nestlist = []

for x in range(100):
    i2 = i1 + i2.start()  # change i2 because it counting in slice and i2 not true value (old i2, i. e. from last iter)
    i1 = i2 + re.search(pattern, text2[i2:]).end()  # same as 1 up
    i2 = re.search(pattern, text2[i1:])  # count new i2
    if i2 is None:
        break
    print(i1, i1 + i2.end(), text2[i1:i1 + i2.start()], len(text2[i1:i1 + i2.start()]))
    amount = len(re.findall(r"[{}]", text2[i1:i1 + i2.start()]))
    if (amount == 0 or amount % 2 == 0) and abs(text2[i1:i1 + i2.start()].count('}') - text2[i1:i1 + i2.start()].count('{')) < 2:
        depth += 1
    elif text2[i1:i1 + i2.start()].count('}') > text2[i1:i1 + i2.start()].count('{'):
        #depth += 1
        nestlist.append(depth)
        depth = 0

print(nestlist)
print(max(nestlist))

# i2 = 0
# while i2 != -1:
#     i1 = text2.find(' if ', i2) # regex find
#     i2 = text2.find(' if ', i1+1)



#pattern = re.compile(r"(((\w+::)+)?(\w+?(\.\w+)+\(+|\w+\())")
#sth2 = pattern.findall(text)

#for i in range(len(sth2)):
#    sth2[i] = sth2[i][0]

#((\.\w+)+\()?

#((\w+::)+)?(\w+?(\.\w+)+\(?|\w+\()
#print(sth)