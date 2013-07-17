#this python script is to implement schedule the instructions 
#this code will use allthe other components to schedule the instructions in different cores

import re
import common
import dependancy
import filter



def schedule_main():
    main_instr=filter_main(filename)
    core1_instr =[]
    core2_instr =[]
    core3_instr =[]
    core4_instr =[]
    for fun in main_instr:
        reg_pool_core1=[]
        reg_pool_core2=[]
        reg_pool_core3=[]
        reg_pool_core4=[]
        for i in range(len(fun)):
            #implement the scheduling algorithm here
            #tasks in this function
            # 1. check for loops
            # 2. check the dependancy
            # 3. Keep track of registers in use
            # 4.
            j = 0
            ILP_tmp = []
            DLP_tmp = []
            while j < 4 and i < len(fun):
                
                if fun[i][2] == Types.function:
                    core1_instr.append(fun[i])
                    core2_instr.append(fun[i])
                    core3_instr.append(fun[i])
                    core4_instr.append(fun[i])
                    j=j+1
                    i=i+1
                    break
                
                elif fun[i][2] == Types.comment:
                    core1_instr.append(fun[i])
                    core2_instr.append(fun[i])
                    core3_instr.append(fun[i])
                    core4_instr.append(fun[i])
                    j=j+1
                    i=i+1
                
                elif fun[i][2] == Types.directive:
                    #to be implemented
                    #right now send all the directives to all the cores
                    core1_instr.append(fun[i])
                    core2_instr.append(fun[i])
                    core3_instr.append(fun[i])
                    core4_instr.append(fun[i])
                    j=j+1
                    i=i+1
                    break
                
                elif fun[i][2] == Types.branch:
                    #copy necessary register to all the cores
                    #send banch instruction to all the cores
                    
                    j=j+1
                    i=i+1
                    break
                   
                elif fun[i][2] == Types.label:
                    if identify_loop(fun,fun[i])!= -1:
                        #use the DLP techniques
                        end_loop = identify_loop(fun,fun[i])
                        i = end_loop + 1
                        for k in range(i,end_loop):
                            DLP_temp.append(fun[k])
                        j = end_loop - i + 1
                        i = end_loop + 1
                    else:
                        core1_instr.append(fun[i])
                        core2_instr.append(fun[i])
                        core3_instr.append(fun[i])
                        core4_instr.append(fun[i])
                        j=j+1
                        i=i+1
                    break   
                else:
                    #use the normal synarion(ILP)
                    ILP_tmp.append(fun[i])
                    j=j+1
                    i=i+1
            no_of_shifts=[]
            dependancy=[]
            for i in range(len(ILP_tmp)):
                #do the scheduling for ILP
                for j in range(i):
                
            for i in rannge(len(DLP_tmp)):
                #do the scheuling for DLP
                
        
    
#this function is to invalidate duplitcate copies when updating corresponding  register value. 
#input -    Register    -   name of the register which is updated
#           reg_pool    -   register pools of other cores to remove the register from them
def remove_duplicates(register, reg_pool,):
    for i in reg_pool:
        if register in i:
            i.remove(register)


#clean the unwanted registers from the register pool
def clean_reg_pool(reg_pool):
    for i in core_reg_pool:
        remove_register('R8', i)
        remove_register('R9', i)
        remove_register('R10',i)
        remove_register('R11',i)
        remove_register('R12',i)
        remove_register('R13',i)
        remove_register('R14',i)
        remove_register('R15',i)
        remove_register('R24',i)
        remove_register('R25',i)

#remove a register from the register pool(in single core)
def remove_register(register, core_reg_pool):
    if register in core_reg_pool:
            i.remove(register)
            



