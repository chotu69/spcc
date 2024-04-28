fp = open('program3.txt','r')
program = fp.read().split('\n')
print('\nGiven assembly code \n')
for line in program:
    print(line)
fp.close()
fp = open('program3.txt','r')
program = fp.read().split('MEND\n')
fp.close()
mnt = []
mdt = {}
for line in program:
    line.strip()
    a = line.split('\n')
    if a[0] == 'MACRO':
        #print('Macro Name is: ', a[1])
        mnt.append(a[1])
        #print('Macro Instruction are:', a[2:])
        mdt[a[1]] = a[2:len(a)-1]
    else:
        prog = a
print('\nContent of MNT:\n')
for each_mn in mnt:
    print(each_mn)    
print('\nContent of MDT:\n')
for k,v in mdt.items():
    for command in v:
        print(command)
print('\nAfter Macro Expansion\n')
for line in prog:
    identify_mc = line.split()
    for word in identify_mc:
        if word in mnt:
            value = mdt[word]
            for i in value:
                print(i)
        else:
            print(word,end=" ")
    else:
        print()
