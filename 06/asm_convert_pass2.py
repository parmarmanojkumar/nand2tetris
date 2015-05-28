# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:52:08 2015
Modified on Wed May 20 14:38:21 2015

@author: Manojkumar Parmar
"""
import re # for regular expression usage
#function to convert A type instruction in asm binary code
def a_instruction(line):
    global symbol_count,symbol_dict
    word  = line.split('@')[1]
    # if extracted element is not digit then special processing is needed        
    if not word.isdigit():        
        # if already exist then replace with memory address
        if word in symbol_dict:
           word = symbol_dict[word]
        # if does not exist enter in dictionary and assign memory address
        # variable symbol only is available
        else:
           symbol_dict[word] = symbol_count
           word = symbol_count
           symbol_count += 1
    #Now convert number in to binary form
    word = int(bin(int(word))[2:])
    # binary form must be 16 digit hence formating
    return(('{:016.0f}'.format(int(word))))
#function to convert C type instruction in asm binary code
def c_instruction (line) :
    #initialize instruction elements
    dest, jmp = '000' , '000'
    acode = '0'
    # check for structure dest = comp ; jmp
    if (line.count('=') > 0 ) :  #dest = xxxxx
        # = sign indicates dest is present and hence split around it to get dest
        word = line.split('=')
        # replace destination with equivalent bit code
        dest = dest_dict[word[0]]
        # remaining portion after = is assigned back to line for 
        # further processing
        line = word[1]
    # check for structure comp; jmp as dest is either not present or removed
    if (line.count(';')>0) :  #xxx;jmp
        # split around ; and extract jmp part
        word = line.split(';')
        # replace jump with equivalent bit code
        jmp = jmp_dict[word[1]]
        # remianing portion left which is comp is assigned back to line for 
        # further processing
        line = word[0]     
    # determine acode based on whether memory access or address
    if (line.count('M')> 0) :
        # Memory is used in comp hence acode  is changed
        acode = '1' 
        # replace M with A as dictionary has only entries with D & A
        line = line.replace('M','A')
    # extract comp bit sequence from dictionary
    comp = comp_dict[line]
    # assemble all set with prefix of 111 as c instruction
    return('111'+ acode+comp+dest+jmp)
    
#Dictionary definition
#variable and loop symbol storage
symbol_dict = {
'SP'  :0, 'LCL' :1, 'ARG' :2, 'THIS':3, 'THAT':4, 'R0'  :0, 'R1'  :1,
'R2'  :2, 'R3'  :3, 'R4'  :4, 'R5'  :5, 'R6'  :6, 'R7'  :7, 'R8'  :8,
'R9'  :9, 'R10' :10,'R11' :11,'R12' :12,'R13' :13,'R14' :14,'R15' :15,
'SCREEN' : 16384, 'KBD' : 24576 }
# storage destination resolution bit dictionary
dest_dict = { 'M'   :'001', 'D'   :'010', 'MD'  :'011', 'A'   :'100',
              'AM'  :'101', 'AD'  :'110', 'AMD' :'111' }
#ALU computation resolution bit dictionary
comp_dict = { 
'0'  :'101010', '1'  :'111111', '-1' :'111010', 'D'  :'001100', 'A'  :'110000',
'!D' :'001101', '!A' :'110001', '-D' :'001111', '-A' :'110011', 'D+1':'011111',
'A+1':'110111', 'D-1':'001110', 'A-1':'110010', 'D+A':'000010', 'D-A':'010011',
'A-D':'000111', 'D&A':'000000', 'D|A':'010101' }
#Jump destination resolution bit dictionary
jmp_dict = {'JGT'   :'001', 'JEQ'   :'010', 'JGE'   :'011', 'JLT'   :'100',
            'JNE'   :'101', 'JLE'   :'110', 'JMP'   :'111'}
# input file name to be converted
fname = raw_input("Enter file to convert:")
#open file
fh = open(fname)
# to check corret opening of file
print(fh)
# To store loop symbols used. Here it represents line number
symbol_count = 0
# list to store preprocessed asm lines
asmlines = list()
#Pass1 : To ignore comment and pre-process lines. Also append loop symbols
#        with corresponding line numbers.
for line in fh:
    # to remove white spaces and remove new line character
    line = line.strip()
    # check if line is blank or starting with comment then ignore line
    if (line == '') or re.search('^//', line):
        continue
    # to remove white spaces in istruction for improved processing
    line = line.replace(' ','')
    #to split comment portion and ignore later portion
    word = line.split('/')
    # To check if asm line is loop sumbol e.g. (LOOP_SYMBOL).
    # check starting line '('
    if re.search('^\(',word[0]):
        # extract loop symbol
        word = re.split('\(|\)',word[0])
        #append symbol dictionary with new symbol name and line count
        symbol_dict[word[1]] = symbol_count
    else:
        # its normal instrunction hence asm code will be generated
        #increase line count
        symbol_count  += 1
        # record instruction in asmlines
        asmlines.append (word[0])
#close the file which was used to read asm file
fh.close()
# input file name to be converted
fname = raw_input("Enter filename for storage:")
fh = open(fname +'.hack' ,'w')
#symbol conversion
symbol_count = 16
for line in asmlines :
    # detect type of instructioninstruction
    if re.search('^@', line):
        # A type instruction which starts  like @value so extract element after @
        word = a_instruction (line)    
    else:
        #c type instruction
        word = c_instruction (line)
    # write asmcode converted to file    
    fh.write(str(word) + "\n")
#close the file
fh.close()