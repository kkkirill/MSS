import re

f = open('sourcecode.txt', 'r')

text = f.read()  # code (str)
f1 = open('roperators.txt', 'r')
ops = f.readlines()  # operators (list)

text = re.compile(r"[#][^\n]*").sub("", text)  # delete all comments
text = re.compile(r"<.*>").sub("< >", text)  # delete all inside <...>
text = re.compile(r"\"(.*)\"").sub("", text)  # delete all strings

sth = sorted(re.compile(r"(?:(?:(?:\w+::)+)?(?:\w+?(?:\.\w+)+\(+|\w+\())").findall(text), reverse=True)

sth = list(filter(None, [re.sub(r"^:\w+\(", r"", i) for i in sth]))
operators = len(sth)

pattern = re.compile(
    r"(\s((?:if|unless|elsif|while|until)[^{^\n;]*(?:;|{|)*)|(for[^{]*\{)|(do\s*{)|((?:case \d|else)\s*[{]*))")

conditions = [[m.start(), m.end(), m.group(1)] for m in re.finditer(pattern, text)]
print(conditions)
CL = len(conditions)
print("Абсолютная сложность программы  (CL) - " + str(CL))
print("Относительная сложность программы (Насыщенность программы условными операторами) (cl) - " + str(operators/CL))

# num of all brackets
listing = [text[:conditions[0][0]].count('{') - text[:conditions[0][0]].count('}')]  # list for calculating depth
max_count = 0  # max depth

for i in range(len(conditions) - 1):
    num_of_open_brackets, num_of_close_brackets = text[conditions[i][1]:conditions[i+1][0]].count('{'), \
                                                  text[conditions[i][1]:conditions[i+1][0]].count('}')
    amount_of_brackets = num_of_open_brackets + num_of_close_brackets

    try:
        if conditions[i][2].find('{') != -1:
            listing.append(num_of_open_brackets + 1)
        else:
            listing[len(listing) - 1] += num_of_open_brackets
            if temp > max_count:
                max_count = temp
    except IndexError:
        print('Ошибка в анализируемом коде')
        exit()
    temp = len(listing) - 1
    if temp - 1 > max_count:
        max_count = temp - 1
    listing[temp] -= num_of_close_brackets
    while listing[temp] < 0:
        temp -= 1
        listing[temp] = listing[temp] + listing[temp + 1]
        listing.pop()
    if listing[temp] == 0 and (not (conditions[i][2].find('case') != -1 or (conditions[i][2].find('else') != -1 and
                                                                           conditions[i - 1][2].find('case') != -1))):
        while listing[temp] == 0:
            listing.pop()
            temp -= 1

print("Максимальный уровень вложенности условного оператора (CLI) - " + str(max_count))