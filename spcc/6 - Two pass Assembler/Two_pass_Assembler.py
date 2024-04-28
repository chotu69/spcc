fp = open('program.txt','r')
program = fp.read().split("\n")
# print(program)
fp.close()


mnemonic_tab = {'STOP':'00','ADD':'01', 'SUB':'02', 'MULT':'03', 'MOVER':'04', 'MOVEM':'05', 'COMP':'06', 'BC':'07', 'DIV':'08', 'READ':'09', 'PRINT':'10','DC':'01','DS':'02','START':'01','END':'02','ORIGIN':'03','EQU':'04','LTORG':'05'}
reg_code = {'AREG':1, 'BREG':2, 'CREG':3, 'DREG':4}
condition_code = {'LT':1,'LE':2,'EQ':3,'GT':4,'GE':5,'ANY':6}
optab = {'START':'AD','READ':'IS','MOVER':'IS','MOVEM':'IS','MULT':'IS','ADD':'IS','COMP':'IS','BC':'IS','PRINT':'IS','STOP':'AD','DS':'DL','DC':'DL','END':'AD','DIV':'IS'}
sym_table = {}


print('Content of Mnemonic table is-\n')
print('Mnemonic   ',    'Code\n')
for k,v in mnemonic_tab.items():
    print('{:<8}{:>8}'.format(k,v))


print()
print('Content of Opcode table is-\n')
print('Mnemonic   ',    'Class\n')
for k,v in optab.items():
    print('{:<8}{:>8}'.format(k,v))


print()
print('****Input Assembly source code*****')
print()


#print the source code
# set the value of lc


for line in program:
    a = line.split()
    if a[0]=='START':
        lc=int(a[1])
        temp = lc
    print(line)


# Build the symbol table
for line in program:
    l = line.split()
    for i in l:
        if i not in optab and i not in reg_code and i.isdigit()!=True and i not in condition_code:
            sym_table[i]=lc
            lc+=1
print()
print('Content of Symbol table is-')
print('Symbol Name   ','Address')
for k,v in sym_table.items():
    print('{:<8}{:>8}'.format(k,v))


         
lc = temp
print()
print('*******Itermediate Code After PASS-I**********')    
print()  
a= list(sym_table.keys())
for line in program:
    lexeme = line.split()
    if(len(lexeme)==4):   #if label is there,remove it exam. AGAIN MULT AREG FIVE
        lexeme.remove(lexeme[0])
    if lexeme[0] in optab:
        if optab[lexeme[0]]=='AD':
            if(len(lexeme)==1):
                print(lc,(optab[lexeme[0]],mnemonic_tab[lexeme[0]]))
                lc+=1
            else:
                if(lexeme[0]=='START'):
                    print('   ',(optab[lexeme[0]],mnemonic_tab[lexeme[0]]),'(C,',lexeme[1],')')
                   
    if lexeme[0] in optab:
        if optab[lexeme[0]]=='IS':
            if len(lexeme)==3:
                #a= list(sym_table.keys())
                if lexeme[0]=='BC':
                    print(lc,(optab[lexeme[0]],mnemonic_tab[lexeme[0]]),condition_code[lexeme[1]],'(S',a.index(lexeme[2]),')')
                    lc+=1
                else:
                    print(lc,(optab[lexeme[0]],mnemonic_tab[lexeme[0]]),reg_code[lexeme[1]],'(S',a.index(lexeme[2]),')')
                    lc+=1
            if(len(lexeme)==2):
                print(lc,(optab[lexeme[0]],mnemonic_tab[lexeme[0]]),'(S',a.index(lexeme[1]),')')
                lc+=1
               
    if lexeme[0] not in optab:
        if len(lexeme)==3:
            print(lc,(optab[lexeme[1]],mnemonic_tab[lexeme[1]]),'(C',lexeme[2],')')
            lc+=1
           
        if len(lexeme)==4:
            print(lc,(optab[lexeme[1]],mnemonic_tab[lexeme[1]]),)
            lc+=1
           
print()
print('********Machine Code After Pass II******\n')
   
lc = temp


for line in program:
    lexeme = line.split()
    if len(lexeme)==4:
        lexeme.remove(lexeme[0])
       
    if lexeme[0] in optab:
        if optab[lexeme[0]]=='AD':
            if(len(lexeme)==1):
                print()
                lc+=1
            else:
                if(lexeme[0]=='START'):pass
                    #print((optab[lexeme[0]],mnemonic_tab[lexeme[0]]),'(C,',lexeme[1],')')
                   
    if lexeme[0] in optab:
        if optab[lexeme[0]]=='IS':
            if len(lexeme)==3:
                #a= list(sym_table.keys())
                if lexeme[0]=='BC':
                    print(lc,mnemonic_tab[lexeme[0]],condition_code[lexeme[1]],sym_table[lexeme[2]])
                    lc+=1
                else:
                    print(lc,mnemonic_tab[lexeme[0]],reg_code[lexeme[1]],sym_table[lexeme[2]])
                    lc+=1
            if(len(lexeme)==2):
                print(lc,mnemonic_tab[lexeme[0]],sym_table[lexeme[1]])
                lc+=1
               
    if lexeme[0] not in optab:
        if len(lexeme)==3:
            print(lc,mnemonic_tab[lexeme[1]],lexeme[2])
            lc+=1
           
        if len(lexeme)==4:
            print(mnemonic_tab[lexeme[1]])
            lc+=1
