#this file contains the common components of the program

#index of the start of the instruction
START_INSTR = 2

#TYPES OF CODE LINE IN THE PROGRAM
#---------------------------------
class Types:
    function, label, comment, instruction, directive = range(5)
#---------------------------------


#number of cycles per instruction execution
#------------------------------------------
#R-Type Instructions
CYCLE_add   =1
CYCLE_addu  =1 
CYCLE_and   =1
CYCLE_break =1
CYCLE_div   =1
CYCLE_divu  =1
CYCLE_jalr  =1
CYCLE_jr    =1
CYCLE_mfhi  =1
CYCLE_mflo  =1
CYCLE_mthi  =1
CYCLE_mtlo  =1
CYCLE_mult  =1
CYCLE_multu =1
CYCLE_nor   =1
CYCLE_or    =1
CYCLE_sll   =1
CYCLE_sllv  =1
CYCLE_slt   =1
CYCLE_sltu  =1
CYCLE_sra   =1
CYCLE_srav  =1
CYCLE_srl   =1
CYCLE_srlv  =1
CYCLE_sub   =1
CYCLE_subu  =1
CYCLE_syscall   =1
CYCLE_xor   =1

CYCLE_sll   =1
CYCLE_srl   =1
CYCLE_sra   =1
CYCLE_sllv  =1
CYCLE_srlv  =1  
CYCLE_srav  =1
CYCLE_jr    =1
CYCLE_jalr  =1
CYCLE_syscall   =1
CYCLE_break =1
CYCLE_mfhi  =1 
CYCLE_mthi  =1
CYCLE_mflo  =1
CYCLE_mtlo  =1
CYCLE_mult  =1
CYCLE_multu =1
CYCLE_div   =1
CYCLE_divu  =1
CYCLE_sub   =1
CYCLE_subu  =1
CYCLE_or    =1  
CYCLE_xor   =1
CYCLE_nor   =1
CYCLE_slt   =1
CYCLE_sltu  =1

#I-type instructions
CYCLE_addi    =1
CYCLE_addiu   =1 
CYCLE_andi    =1
CYCLE_beq     =1
CYCLE_bgez    =1
CYCLE_bgtz    =1
CYCLE_blez    =1
CYCLE_bltz    =1
CYCLE_bne     =1
CYCLE_lb      =1
CYCLE_lbu     =1
CYCLE_lh      =1
CYCLE_lhu     =1
CYCLE_lui     =1
CYCLE_lw      =1
CYCLE_lwc1    =1
CYCLE_ori     =1
CYCLE_sb      =1
CYCLE_slti    =1
CYCLE_sltiu   =1
CYCLE_sh      =1
CYCLE_sw      =1
CYCLE_swc1    =1
CYCLE_xori    =1

CYCLE_bltz    =1
CYCLE_bgez    =1
CYCLE_beq     =1
CYCLE_bne     =1
CYCLE_blez    =1
CYCLE_bgtz    =1
CYCLE_addi    =1
CYCLE_addiu   =1
CYCLE_slti    =1
CYCLE_sltiu   =1
CYCLE_andi    =1
CYCLE_ori     =1
CYCLE_xori    =1
CYCLE_lui     =1
CYCLE_lb      =1
CYCLE_lh      =1
CYCLE_lw      =1
CYCLE_lbu     =1
CYCLE_lhu     =1
CYCLE_sb      =1
CYCLE_sh      =1
CYCLE_sw      =1
CYCLE_lwc1    =1
CYCLE_swc1    =1

# J-type instructions
CYCLE_j       =1
CYCLE_jal     =1


#COPROCESSOR INSTRUCTIONS
CYCLE_add_s   =1 
CYCLE_cvt_s_w =1 
CYCLE_cvt_w_s =1
CYCLE_div_s   =1
CYCLE_mfc1    =1
CYCLE_mov_s   =1
CYCLE_mtc1    =1
CYCLE_mul_s   =1
CYCLE_sub_s   =1

#--------------------------------



#indexes of each component in the instruction array is defined here
STRING      = 0
DEPENDANCY  = 1
TYPE        = 2
OPCODE      = 3

#--------------------------------


#this class is to specyfy types of dependancy
#depending on the type, there are specific attributes
class dependancy_type:
    time_dependancy=False
    name_dependancy=True
    no_dependancy = True
    processor_dependancy=False
    def set_time_dep(self):
        no_dependancy=False
        self.time=1
    def set_true_dep():
        no_dependancy==False
        time_dependancy=True
    #to be implemented
    def set_name_dep():
        no_dependancy==False
        name_dependancy=True
    




