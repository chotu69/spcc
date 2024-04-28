import re

ep = list()
fp = open("grammar.txt", "r")  # read CFG from file
cfg = dict()  # create dictionary to stored CFG
global non_terminal

def find_first(key):
    value = cfg[key]  # find RHS of key(LHS)
    if '#' in value:  # if key directly derived epsilon
        value.remove('#')
    for item in value:  # consider individual production rule
        if item[0] in ep:  # if that variable produce epsilon
            epsilon(item)
        else:
            if item[0].islower():
                if item[0] not in temp:
                    temp.append(item[0])
                else:
                    find_first(item[0])

def epsilon(item):
    find_first(item[0])  # find first of that variable
    length = len(item)
    i = 1
    while i <= length - 1:
        if item[i] in ep:
            find_first(item[i])
            i = i + 1
            if i == length:
                if '#' not in temp:
                    temp.append('#')
                break
        else:
            if item[i].islower():
                if item[i] not in temp:
                    temp.append(item[i])
                break
            else:
                find_first(item[i])
                break

def find_follow(key):
    for k, v in cfg.items():
        for item in v:
            if re.search(key, item):  # search key in RHS
                index = item.find(key)  # if found
                length = len(item) - 1
                if index == length:  # if variable found at Right most side of RHS
                    temp1 = follow[k]  # then find follow[k]
                    for i in temp1:
                        temp.append(i)  # append it
                    index = index + 1  # find next symbol
                for i in range(index, len(item)):  # try all next variable/terminal
                    if item[i].islower():  # if follow symbol is terminal
                        temp.append(item[i])  # add it to follow()
                        break  # stop
                    else:
                        temp1 = first[item[i]]  # find first[follow variable]
                        for j in temp1:
                            if j != '#':
                                temp.append(j)  # append it to follow dictionary/temp
                        if '#' in temp1:  # if first[follow item] contain epsilon
                            i = i + 1  # check for next variable
                        else:
                            break  # else stop
                        if i == len(item):  # if we reach at right most side of RHS
                            temp1 = follow[k]  # find follow[LHS]
                            for j in temp1:
                                temp.append(j)  # append result

for line in fp:
    line.strip()  # remove begining and trailing white spaces
    if re.search('\n', line):
        line = line[:line.find('\n')]  # remove \n from line
    split = line.split('->')  # split line (LHS and RHS)
    split = split[1].split('|')  # split RHS based on |
    i = 0
    for item in split:
        split[i] = item.strip()  # remove begining and trailing white spaces
        i = i + 1
    cfg[line[0]] = split  # store LHS as key and RHS as a values

print("\nGiven Context Free Grammar is =")
for key, value in cfg.items():
    print(key, " ->", value)  # print CFG
    if '#' in value:  # if any variable/non terminal generate an epsilon
        ep.append(key)  # then stored that varaible in list ep
temp = list()
first = dict()
for key, value in cfg.items():
    first[key] = []  # initialize value of key as list
    non_terminal = key
    find_first(key)
    if key in ep:
        if '#' not in temp:  # if varaible produce epsilon
            temp.append('#')  # add epsilon to first[variable]
    for item in temp:
        first[non_terminal].append(item)  # add all results to first
    temp.clear()

follow = dict()
flag = 0
temp = list()
for key, value in cfg.items():
    follow[key] = []  # initialize value of key as list
    if flag == 0:
        temp.append("$")  # follow of start symbol is $
        flag = 1
    find_follow(key)
    for k in temp:
        if k not in follow[key]:  # removed duplicate and add it to final result
            follow[key].append(k)
    temp.clear()

print(" Non Terminal First() Follow()")
print("------------------------------------------------------")
for key, value in follow.items():
    print(" ", key, " ", first[key], " ", value)
print("\n")
