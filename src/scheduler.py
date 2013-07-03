#this python script is to implement schedule the instructions 
#this code will use allthe other components to schedule the instructions in different cores

import re
import common
import dependancy
import filter



def schedule_main():
    main_instr=filter_main(filename)
    for fun in main_instr:
        for instr in fun:
            #implement the scheduling algorithm here
            #tasks in this function
            # 1. check for loops
            # 2. check the dependancy
            # 3. Keep track of registers in use
            # 4. 