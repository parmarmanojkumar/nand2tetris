# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:52:08 2015

@author: Manojkumar Parmar
"""

import re

#Dictionary definition
#loop symbol storage
loop_dict = dict()
#variable symbol storage
symbol_dict = {
'SP'  :0,
'LCL' :1,
'ARG' :2,
'THIS':3,
'THAT':4,
'R0'  :0,
'R1'  :1,
'R2'  :2,
'R3'  :3,
'R4'  :4,
'R5'  :5,
'R6'  :6,
'R7'  :7,
'R8'  :8,
'R9'  :9,
'R10' :10,
'R11' :11,
'R12' :12,
'R13' :13,
'R14' :14,
'R15' :15,
'SCREEN' : 16384,
'KBD' : 24576
}
# destination bit dictionary
dest_dict = {
'M'   :'001',
'D'   :'010',
'MD'  :'011',
'A'   :'100',
'AM'  :'101',
'AD'  :'110',
'AMD' :'111'
}
#computation bit dictionary
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
#jump bit dictionary
jmp_dict = {
'JGT'   :'001',
'JEQ'   :'010',
'JGE'   :'011',
'JLT'   :'100',
'JNE'   :'101',
'JLE'   :'110',
'JMP'   :'111'
}

# input file name
fname = raw_input("Enter file to convert:")
#open file
fh = open(fname)
# to check corret opening of file
print(fh)
# parse asm lines to remove comments
asmlines = list()
for line in fh:
     words = line.split()
     if (not re.search('^//', line)) and len(words) > 0  :
         asmlines.append (words[0])


# pass 1: to collect loop vsymbols
count = 0
symbol_count = 16
for line in asmlines:
    if re.search('^\(',line):
        temp = re.split('\(|\)',line)
        loop_dict[temp[1]] = count
    else:
        count += 1


# output file name
fname = raw_input("Enter filename for storage (with.hack):")
fh = open(fname ,'w')

#symbol conversion

for line in asmlines :
    
    # if loop jump point is detected then skip it as conversion is not needed
    if re.search('^\(',line):
        continue
    
    # A type instruction
    if re.search('^@', line):
        #extract element after @
        temp  = line.split('@')[1]
        # if extracted element is not digit then special processing is needed        
        if not temp.isdigit():        
            # if element is loop symbol then replace with line no.
            if temp in loop_dict:
                temp = loop_dict[temp]
            #if element is variable symbol
            else:
                # if already exist then replace with memory no
                if temp in symbol_dict:
                   temp = symbol_dict[temp]
                # if does not exist enter in dictionary and assign memory no
                else:
                   symbol_dict[temp] = symbol_count
                   temp = symbol_count
                   symbol_count += 1
        #Now convert number in to binary form
        temp = int(bin(int(temp))[2:])
        # binary form must be 16 digit hence formating
        asmcode = ('{:016.0f}'.format(int(temp)))
    
    # C type instruction
    else:
        #initialize instruction elements
        dest = '000'
        jmp  = '000'
        comp = '000000'
        #split the instruction as per dest = comp; jmp
        word = re.split('=|;',line)
        word_len = len(word)
        # if entire instruction then assignment to elements
        if (word_len ==3) : #dest = comp;jmp
            dest = dest_dict[word[0]]
            #comp is not assigned here to improve processing of A and M operation
            comp = word[1]
            jmp = jmp_dict[word[2]]
        # if 2 element is there then determine based on '=' and assign element
        elif (line.count('=')> 0): #dest=comp
            dest = dest_dict[word[0]]
            comp = word[1]
        # if 2 element is there then determine based on ';' and assign element
        elif (line.count(';')> 0): # comp;jmp
            comp = word[0]
            jmp = jmp_dict[word[1]]
        else: #comp
            comp = word[0]
        
        # comp is processed here to reduce dictionary size of comps
        # if M is present in comp hence set a code to 1
        if (comp.count('M')> 0) :
            acode = '1' 
            # replace M with A as dictionary has only entries with D & A
            comp = comp.replace('M','A')
        # if M is not present in comp hence set a code to 0
        else:
            acode = '0'
        # extract comp bit sequence from dictionary
        comp = comp_dict[comp]
        # assemble all set with prefix of 111 as c instruction
        asmcode = ('111'+ acode+comp+dest+jmp)
        
    # write asmcode converted to file    
    fh.write(str(asmcode) + "\n")

#close the file
fh.close()
