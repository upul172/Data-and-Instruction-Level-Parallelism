#this file is to find dependancy 

import common

#'bi_dependany' function will find the depencancy between two instructions

def bi_dependancy(current, prev):
    dep=dependancy_type()
    
    #assuming the index of the opcode is 2
    if current[START_INSTR]=='lw':
        if prev[START_INSTR]=='sw':
            if prev[START_INSTR+2]==current[START_INSTR+2] and prev[START_INSTR+3]==current[START_INSTR+3]:
                dep.set_true_dep()
                #there is a dependancy
            elif prev[START_INSTR+1]==current[START_INSTR+1]:
                dep.set_name_dep()
        elif count_inputs(prev)==1 and prev[START_INSTR+2]==current[START_INSTR+1]:
            dep.set_true_dep()
            #set the values in the dependancy
        elif count_inputs(prev)==2:
            if prev[START_INSTR+2]==current[START_INSTR+1]:
                dep.set_true_dep()
            if prev[START_INSTR+3]==current[START_INSTR+1]:
                dep.set_true_dep()
    
    elif current[START_INSTR]=='sw':
        if prev[START_INSTR]=='sw':
            if prev[START_INSTR+2]==current[START_INSTR+2] and prev[START_INSTR+3]==current[START_INSTR+3]:
                dep.set_true_dep()
                #there is a dependancy
        elif count_inputs(current)==1 and prev[START_INSTR+1]==current[START_INSTR+2]:
            dep.set_true_dep()
            #set the values in the dependancy
        elif count_inputs(current)==2:
            if current[START_INSTR+2]==prev[START_INSTR+1]:
                dep.set_true_dep()
            if current[START_INSTR+3]==prev[START_INSTR+1]:
                dep.set_true_dep()
    elif count_inputs(current)==1:
    #check weather others depend on the one input instruction
        if prev[START_INSTR]=='lw' and prev[START_INSTR+1]==current[START_INSTR+2]:
            dep.set_true_dep()
        elif count_inputs(prev)==1:
            if prev[START_INSTR+1]==current[START_INSTR+2]:
                dep.set_true_dep()
        elif count_inputs(prev)==2:
            if prev[START_INSTR+1]==current[START_INSTR+2]:
                dep.set_true_dep()
    elif count_inputs(current)==2:
        if prev[START_INSTR]=='lw':
            if prev[START_INSTR+1]==current[START_INSTR+2] or prev[START_INSTR+1]==current[START_INSTR+3]:
                dep.set_true_dep()
        elif count_inputs(prev)==1:
            if prev[START_INSTR+1]==current[START_INSTR+2] or prev[START_INSTR+1]==current[START_INSTR+3]:
                dep.set_true_dep()
        elif count_inputs(prev)==2:
            if prev[START_INSTR+1]==current[START_INSTR+2] or prev[START_INSTR+1]==current[START_INSTR+3]:
                dep.set_true_dep()
    return dep

#this function is to identify loop a label is found.
#array is the instruction array and index is the index of the corresponding loop
def identify_loop(array,index):
    #identify the loop
    for i in array[index:len(array)]:
        if array[i][TYPE]==Types.instruction:
            if array[i][OPCODE]=='j':
                if array[i][OPCODE+1]==array[index][OPCODE]:
                    return i
    return -1

#this function is to count number of inputs in a particular instruction
#if the instruction is a special type of instruction(like lw sw)it will return the name of the instruction
#if the the given instruction is not a special instruction or a instruction which can be calculated the number of inputs, then it will return 'else'

def count_inputs(instr):
    count = 0

    if instr[1] == 0 : #add the other instructions here to count inputs
        count == instr[START_INSTR]
    elif instr[1] == 1 :
        count == 1
    elif instr[1] == 2 :
        count == 2

    return count  # else return '0' (when instr[1] is empty)
        
        
    

