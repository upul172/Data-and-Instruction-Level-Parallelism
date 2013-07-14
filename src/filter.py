# filter.py
# http://students.cse.tamu.edu/wanglei/csce350/reference/assembler_dir.html


# input        : mips assembly file
# output        : 3D list
# Description    : 

import re

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

class Types:
    function, label, comment, instruction, directive = range(5)


# Separate comments in each line from the code

def separate_cmnt(line):
    op = []
    if re.search(r'[\t]*\#',line):
        oneTab = re.sub(r'\t+','\t',line)
        splt = oneTab.split('\t')
        op.append(splt[0])
        op.append(splt[1])
    else:
        op.append(line)
        op.append('')

    return op


# separate offset and base of memory addresses in load and store

def mem_address(addr):
    return re.split(r'\(|\)',addr)


# Filtering each line
    
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
        m=re.search(r'\.[a-z].*',instr)
        if m is not None:
            n = m.group().partition('\t')
            oplist.append(n[0]) #opcode
            if n[2]!='':
                op = separate_cmnt(n[2])
                m = op[0].split(',')  # separate each operand
                for val in m:
                    oplist.append(re.sub('[ ]','',val)) #operands
                oplist.append(op[1])  # comment
                print op[0]


    # Arithmatic operations
         
    #filer add instruction (add,addu,addi,addui)
    if re.search(r'^[\t ]*add.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'add.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]
            
            
    #filter count leading instruction (CLO, CLZ)
    elif re.search(r'^[\t ]*cl.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'cl.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            oplist[1] = 1
            print oplist[1]
            
    
    #filter move instruction (MOVE)
    elif re.search(r'^[\t ]*\bmove\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'move.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            oplist[1] = 1
            print oplist[1]
            
    #filter ......... instruction (NEGU)
    elif re.search(r'^[\t ]*negu.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'negu.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            oplist[1] = 1
            print oplist[1]
            
    #filter ..... instruction (SEB)
    elif re.search(r'^[\t ]*seb.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'seb.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            oplist[1] = 1
            print oplist[1]
            
    #filter ...... instruction (SEH)
    elif re.search(r'^[\t ]*seh.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'seh.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            oplist[1] = 1
            print oplist[1]

    #filter ...... instruction (SUB, SUBU)
    elif re.search(r'^[\t ]*sub.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'sub.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]
            
    #filter ...... instruction (LA)
    elif re.search(r'^[\t ]*la.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'la.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            oplist[1] = 1
            print oplist[1]

    #filter ...... instruction (LI)
    elif re.search(r'^[\t ]*li.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'li.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            oplist[1] = 1
            print oplist[1]
            
    #filter ...... instruction (LUI)
    elif re.search(r'^[\t ]*lui.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'lui.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            oplist[1] = 1
            print oplist[1]


    # Shift and rotate
    
    #filter SRA shift operation instruction (sra, srav)
    elif re.search(r'^[\t ]*sra.*',instr):
        print ",,,,,,,,,sra works"
        oplist.append(Types.instruction)
        m = re.search(r'sra.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]


    #filter SLL shift operation instruction (sll, sllv)
    elif re.search(r'^[\t ]*sll.*',instr):
        print ",,,,,,,,,sll works"
        oplist.append(Types.instruction)
        m = re.search(r'sll.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]


    #filter SRL shift operation instruction (sll, sllv)
    elif re.search(r'^[\t ]*srl.*',instr):
        print ",,,,,,,,,srl works"
        oplist.append(Types.instruction)
        m = re.search(r'srl.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]


    # Logic and bit-field

    #filter AND operation instruction (and, andi)
    elif re.search(r'^[\t ]*and.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'and.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]

    # NOP
    elif re.search(r'^[\t ]*nop.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'nop.*',instr)
        n = m.group().partition('\t')
        oplist.append(n[0])
        oplist[1] = 0
        print oplist[1]

    # NOR
    elif re.search(r'^[\t ]*nor.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'nor.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]

    # NOT
    elif re.search(r'^[\t ]*not.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'not.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            oplist[1] = 1
            print oplist[1]
            
    # OR
    elif re.search(r'^[\t ]*or.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'or.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]

    # XOR
    elif re.search(r'^[\t ]*xor.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'xor.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]


    # Condition testing and conditional move
    
    # MOVN
    elif re.search(r'^[\t ]*\bmovn\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'mov.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]

    # MOVZ
    elif re.search(r'^[\t ]*\bmovz\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'mov.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]
            

    # SLT
    elif re.search(r'^[\t ]*slt.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'slt.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]


    # Multiply and divide

    # DIV
    elif re.search(r'^[\t ]*div.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'div.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]

    # MADD
    elif re.search(r'^[\t ]*madd.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'madd.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]

    # MSUB
    elif re.search(r'^[\t ]*msub.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'msub.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]

    # MULT, MULTU
    elif re.search(r'^[\t ]*mult.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'mult.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]

    # MUL
    elif re.search(r'^[\t ]*\bmul\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'mul.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            oplist.append(op[1])
            oplist[1] = 2
            print oplist[1]


    # Accumulator access

    # MFHI, MFLO
    elif re.search(r'^[\t ]*mf.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'mf.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(op[1])
            print n[0]

    # MTHI, MTLO
    elif re.search(r'^[\t ]*mt.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'mt.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(op[1])
            oplist[1] = 1
            print oplist[1]


    # Jumps and branches

    # BAL
    elif re.search(r'^[\t ]*bal',instr):
        oplist.append(Types.instruction)
        m = re.search(r'bal.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #value
            oplist.append(op[1])
            print "BAL"

    # BEQZ
    elif re.search(r'^[\t ]*beqz',instr):
        oplist.append(Types.instruction)
        m = re.search(r'beqz.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            print "beqz.."

    # BEQ
    elif re.search(r'^[\t ]*\bbeq\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'beq.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            oplist.append(op[1])
            print "beq.."

    # B
    elif re.search(r'^[\t ]*\bb\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'b.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #value
            oplist.append(op[1])
            print "B"

    # BGEZ
    elif re.search(r'^[\t ]*bgez.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'bgez.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            print "Bgez"

    # BGTZ
    elif re.search(r'^[\t ]*bgtz.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'bgtz.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            print "Bgtz"

    # BLEZ
    elif re.search(r'^[\t ]*blez.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'blez.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            print "Blez"

    # BLTZ
    elif re.search(r'^[\t ]*bltz.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'bltz.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            print "Bltz"

    # BNE
    elif re.search(r'^[\t ]*\bbne\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'bne.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(re.sub('[ ]','',m[2])) #operand 3
            oplist.append(op[1])
            print "Bne"

    # BNEZ
    elif re.search(r'^[\t ]*\bbnez\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'bnez.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            print "Bnez"

    # J
    elif re.search(r'^[\t ]*\bj\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'j.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(op[1])
            print "J"

    # JAL
    elif re.search(r'^[\t ]*\bjal\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'jal.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(op[1])
            print "Jal"

    # JALR
    elif re.search(r'^[\t ]*\bjalr\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'jalr.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',m[1])) #operand 2
            oplist.append(op[1])
            oplist[1] = 1
            print oplist[1]

    # JR
    elif re.search(r'^[\t ]*\bjr\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'jr.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(op[1])
            oplist[1] = 1
            print oplist[1]


    # Load and Store

    # LB, LBU
    elif re.search(r'^[\t ]*lb.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'lb.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            mem = mem_address(m[1])
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',mem[0])) #offset
            oplist.append(re.sub('[ ]','',mem[1])) #base
            oplist.append(op[1])
            oplist[1] = 0
            print oplist[1]

    # LH, LHU
    elif re.search(r'^[\t ]*lh.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'lh.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            mem = mem_address(m[1])
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',mem[0])) #offset
            oplist.append(re.sub('[ ]','',mem[1])) #base
            oplist.append(op[1])
            oplist[1] = 0
            print oplist[1]

    # LW, LWL, LWR
    elif re.search(r'^[\t ]*lw.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'lw.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            mem = mem_address(m[1])
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',mem[0])) #offset
            oplist.append(re.sub('[ ]','',mem[1])) #base
            oplist.append(op[1])
            oplist[1] = 0
            print oplist[1]

    # SB
    elif re.search(r'^[\t ]*\bsb\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'sb.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            mem = mem_address(m[1])
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',mem[0])) #offset
            oplist.append(re.sub('[ ]','',mem[1])) #base
            oplist.append(op[1])
            oplist[1] = 0
            print oplist[1]

    # SH
    elif re.search(r'^[\t ]*\bsh\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'sh.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            mem = mem_address(m[1])
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',mem[0])) #offset
            oplist.append(re.sub('[ ]','',mem[1])) #base
            oplist.append(op[1])
            oplist[1] = 0
            print oplist[1]

    # SW
    elif re.search(r'^[\t ]*sw.*',instr):
        oplist.append(Types.instruction)
        m = re.search(r'sw.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            mem = mem_address(m[1])
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',mem[0])) #offset
            oplist.append(re.sub('[ ]','',mem[1])) #base
            oplist.append(op[1])
            oplist[1] = 0
            print oplist[1]

    # ULW
    elif re.search(r'^[\t ]*\bulw\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'ulw.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            mem = mem_address(m[1])
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',mem[0])) #offset
            oplist.append(re.sub('[ ]','',mem[1])) #base
            oplist.append(op[1])
            oplist[1] = 0
            print oplist[1]

    # USW
    elif re.search(r'^[\t ]*\busw\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'usw.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            mem = mem_address(m[1])
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',mem[0])) #offset
            oplist.append(re.sub('[ ]','',mem[1])) #base
            oplist.append(op[1])
            oplist[1] = 0
            print oplist[1]


    # Atomic read-modify-write

    # LL
    elif re.search(r'^[\t ]*\bll\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'll.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            mem = mem_address(m[1])
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',mem[0])) #offset
            oplist.append(re.sub('[ ]','',mem[1])) #base
            oplist.append(op[1])
            oplist[1] = 0
            print oplist[1]

    # SC
    elif re.search(r'^[\t ]*\bsc\b',instr):
        oplist.append(Types.instruction)
        m = re.search(r'sc.*',instr)
        if m is not None:
            n = m.group().partition('\t')
            op = separate_cmnt(n[2])
            m = op[0].split(',');
            mem = mem_address(m[1])
            oplist.append(n[0]) #opcode
            oplist.append(re.sub('[ ]','',m[0])) #operand 1
            oplist.append(re.sub('[ ]','',mem[0])) #offset
            oplist.append(re.sub('[ ]','',mem[1])) #base
            oplist.append(op[1])
            oplist[1] = 0
            print oplist[1]


    print oplist


filter_main("assembly")        # input file name
    
