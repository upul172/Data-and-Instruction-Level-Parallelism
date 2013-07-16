# filter.py
# http://students.cse.tamu.edu/wanglei/csce350/reference/assembler_dir.html


# input         : mips assembly file
# output        : 3D list
# Description   : 
import re
import common
class Types:
    function, label, comment, instruction, directive = range(5)
    
def filter_main(filename):
    f=open(filename,'r')

    ln = []
    for line in f:      # remove empty lines in file
        if not line.strip():
            continue
        else:
            ln.append(line)
    f.close()

    for i in ln:        # apply method
        filter_line(i)
    
# this function creates a list with opcode and operands for a given string insrtuction
# input for this function is a string(line of the assembly code)
# output is a list which holds the data of the sring
# output[0]=input string
# output[1]=type
# output[2]=instr



    
def filter_line(instr):
    oplist = []
    oplist.append(instr)
    oplist.append([])
    
    #this filter the comment lines
    if re.search(r'^[\t| ]*#',instr):
        oplist.append(Types.comment)
        
    #filter directive
    elif re.search(r'^[\t| ]*[\.][a-z]*',instr):
        oplist.append(Types.directive)
        m=re.search(r'[\.][a-z| ]*',instr)
        print m.group()
        m=m.group().split(' ');
        oplist.append(m[0]) # put the directive name in to the list
        #oplist.append(m[1]) # save all the directive data into a list element(TO BE IMPLEMENTED)
        
    #filer add instruction (add,addu,addi,addui)
    elif re.search(r'^[\t ]*add.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'add.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            #tmp = re.sub('[ ]', ',', n[2])
            m = n[2].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            print n[0]


   

    print oplist


filter_main("assembly")        # input file name
    
