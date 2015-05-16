# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:52:08 2015

@author: VirKrupa
"""

import re
# input file name
fname = raw_input("Enter file to convert:")
#open file
fh = open(fname)
# parse asm lines
asmlines = list()
for line in fh:
     words = line.split()
     if (not re.search('^//', line)) and len(words) > 0  :
         asmlines.append (words[0])
fh.close()

dest_dict = {
'M'   :'001',
'D'   :'010',
'MD'  :'011',
'A'   :'100',
'AM'  :'101',
'AD'  :'110',
'AMD' :'111'
}
comp_dict = {
'0'  :'101010',
'1'  :'111111',
'-1' :'111010',
'D'  :'001100',
'A'  :'110000',
'!D' :'001101',
'!A' :'110001',
'-D' :'001111',
'-A' :'110011',
'D+1':'011111',
'A+1':'110111',
'D-1':'001110',
'A-1':'110010',
'D+A':'000010',
'D-A':'010011',
'A-D':'000111',
'D&A':'000000',
'D|A':'010101',
}
jmp_dict = {
'JGT'   :'001',
'JEQ'   :'010',
'JGE'   :'011',
'JLT'   :'100',
'JNE'   :'101',
'JLE'   :'110',
'JMP'   :'111'
}

fname = raw_input("Enter filename for storage (with.hack):")
fh = open(fname ,'w')
#symbol conversion
#asmcode = list()
for line in asmlines :
    if re.search('^@', line):
        temp  = line.split('@')[1]
        temp = int(bin(int(temp))[2:])
        asmcode = ('{:016.0f}'.format(int(temp)))
    else:
        dest = '000'
        jmp  = '000'
        comp = '000000'

        word = re.split('=|;',line)
        word_len = len(word)
        if (word_len ==3) :
            dest = dest_dict[word[0]]
            comp = word[1]
            jmp = jmp_dict[word[2]]
        elif (line.count('=')> 0):
            dest = dest_dict[word[0]]
            comp = word[1]
        elif (line.count(';')> 0):
            comp = word[0]
            jmp = jmp_dict[word[1]]
        else:
            comp = word[0]
        
        if (comp.count('M')> 0) :
            acode = '1111' 
            comp = comp.replace('M','A')
        else:
            acode = '1110'

        comp = comp_dict[comp]
        asmcode = (acode+comp+dest+jmp)
    fh.write(str(asmcode) + "\n")
fh.close()
 
            

     
