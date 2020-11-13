from convertor import Convertor
from r_format import R_Format
from i_format import I_Format
from memory import Memory
from registers import Registers
import string

r_function_code_dict = {
    32: "Add",
    34: "Sub",
    41: "And",
    37: "Or",
    38: "Xor"
    }

i_op_code_dict = {
    8: "Addi",
    35: "Lw",
    43: "Sw",
    9: "Beq",
    4: "Bne"
    }

def print_registers_and_memory(Registers, Memory):
    print("")
    for key, value in registers.registers_dict.items():
        print('register[', key, "] : ", value)

    print("")

    for key, value in memory.memory_dict.items():

        print('memory[', key, "] : ", value)

    print("")

def is_hex(value):
    is_hexadecimal = True
    for letter in value:
           if letter not in string.hexdigits:
               is_hexadecimal = False
    return is_hexadecimal

def is_8_values_long(value):
    is_8_values_long = True
    if(len(value) != 8):
        is_8_values_long = False
    return is_8_values_long

def get_hex_input():
    try_again = True
    while try_again:
        hex = input("Enter an instruction: ")
        parameter_one = is_hex(hex)
        parameter_two = is_8_values_long(hex)
        if(parameter_one == True and parameter_two == True):
            try_again = False
        else:
            print("Enter a hexadecimal instruction with 8 characters")
    return hex


registers = Registers()
memory = Memory(50)
convertor = Convertor()

print_registers_and_memory(registers, memory)

on = True
while on:
    instruction = get_hex_input()
    '''
    00430825 - or $1,$2,$3
    00430820 - add $1,$2,$3
    00430822 - sub $1,$2,$3
    00430829 - and $1,$2,$3
    00430826 - xor $1,$2,$3
    20410003 - addi $1,$2,3
    8C410003 - lw $1,3($2)
    AC410003 - sw $1,3($2)
    24410003 - beq $1,3($2)
    10410003 - bne $1,3($2)
    '''

    i_instruction = I_Format(convertor.hexadecimal_to_binary(instruction))
    r_instruction = R_Format(convertor.hexadecimal_to_binary(instruction))
    if r_instruction.op == 0:
        function = r_function_code_dict.get(r_instruction.funct)
    else:
        function = i_op_code_dict.get(i_instruction.op)

    if (function == "Add"):
        destination = "$" + str(r_instruction.rd)
        left_value = "$" + str(r_instruction.rs)
        right_value = "$" + str(r_instruction.rt)
        value = registers.get_register_value(left_value) + registers.get_register_value(right_value)
        registers.store_register_value(destination, value)
        print("add " + destination + ", " + left_value + ", " + right_value)

    if (function == "Sub"):
        destination = "$" + str(r_instruction.rd)
        left_value = "$" + str(r_instruction.rs)
        right_value = "$" + str(r_instruction.rt)
        value = registers.get_register_value(left_value) - registers.get_register_value(right_value)
        registers.store_register_value(destination, value)
        print("sub " + destination + ", " + left_value + ", " + right_value)
    if (function == "And"):
        destination = "$" + str(r_instruction.rd)
        left_value = "$" + str(r_instruction.rs)
        right_value = "$" + str(r_instruction.rt)
        left_value_binary = convertor.decimal_to_binary_twos_complement(registers.get_register_value(left_value))
        right_value_binary = convertor.decimal_to_binary_twos_complement(registers.get_register_value(right_value))
        new_value = ""
        for i in range(0, 32):
            if (left_value_binary[i] == "1" and right_value_binary[i] == "1"):
                new_value += "1"
            else:
                new_value += "0"
        decimal_value = convertor.convert_twos_complement_binary_to_decimal(new_value)
        registers.store_register_value(destination, decimal_value) 
        print("and " + destination + ", " + left_value + ", " + right_value)
    if (function == "Or"):
        destination = "$" + str(r_instruction.rd)
        left_value = "$" + str(r_instruction.rs)
        right_value = "$" + str(r_instruction.rt)
        left_value_binary = convertor.decimal_to_binary_twos_complement(registers.get_register_value(left_value))
        right_value_binary = convertor.decimal_to_binary_twos_complement(registers.get_register_value(right_value))
        new_value = ""
        for i in range(0, 32):
            if (left_value_binary[i] == "1" or right_value_binary[i] == "1"):
                new_value += "1"
            else:
                new_value += "0"
        decimal_value = convertor.convert_twos_complement_binary_to_decimal(new_value)
        registers.store_register_value(destination, decimal_value) 
        print("or " + destination + ", " + left_value + ", " + right_value)
    if (function == "Xor"):
        destination = "$" + str(r_instruction.rd)
        left_value = "$" + str(r_instruction.rs)
        right_value = "$" + str(r_instruction.rt)
        left_value_binary = convertor.decimal_to_binary_twos_complement(registers.get_register_value(left_value))
        right_value_binary = convertor.decimal_to_binary_twos_complement(registers.get_register_value(right_value))
        new_value = ""
        for i in range(0, 32):
            if (left_value_binary[i] == "1" and right_value_binary[i] == "1"):
                new_value += "0"
            elif (left_value_binary[i] == "1" or right_value_binary[i] == "1"):
                new_value += "1"
            else:
                new_value +="0"
        decimal_value = convertor.convert_twos_complement_binary_to_decimal(new_value)
        registers.store_register_value(destination, decimal_value) 
        print("xor " + destination + ", " + left_value + ", " + right_value)
    if (function == "Addi"):
        destination = "$" + str(i_instruction.rt)
        left_value = "$" + str(i_instruction.rs)
        right_value_decimal = i_instruction.address
        registers.store_register_value(destination,(registers.get_register_value(left_value) + right_value_decimal)) 
        print("addi " + destination + ", " + left_value + ", " + str(right_value_decimal))
    if (function == "Lw"):
        offset = i_instruction.rs
        address = i_instruction.address + offset
        destination = "$" + str(i_instruction.rt)
        registers.store_register_value(destination, memory.get_memory_value(address))
        print("lw " + destination + ", " + str(i_instruction.address) + "($" + str(offset) + ")")
    if (function == "Sw"):
        offset = i_instruction.rs
        address = i_instruction.address + offset
        destination = "$" + str(i_instruction.rt)
        memory.store_memory_value(address, registers.get_register_value(destination))
        print("sw " + destination + ", " + str(i_instruction.address) + "($" + str(offset) + ")")
    if (function == "Beq"):
        register_one_add = "$" + str(i_instruction.rs)
        register_two_add = "$" + str(i_instruction.rt)
        address = i_instruction.address
        if(registers.get_register_value(register_one_add) == registers.get_register_value(register_two_add)):
            memory.store_memory_value(address, 1)
        else:
            memory.store_memory_value(address, 0)
        print("beq " + register_one_add + ", " + register_two_add + ", " + str(address) + ")")
    if (function == "Bne"):
        register_one_add = "$" + str(i_instruction.rs)
        register_two_add = "$" + str(i_instruction.rt)
        address = i_instruction.address
        if(registers.get_register_value(register_one_add) != registers.get_register_value(register_two_add)):
            memory.store_memory_value(address, 1)
        else:
            memory.store_memory_value(address, 0)
        print("beq " + register_one_add + ", " + register_two_add + ", " + str(address) + ")")

    print_registers_and_memory(registers, memory)

    continue_val = input("Do you want to continue (Y/N): ")
    try_again = True
    while (try_again):
        if(continue_val == "Y"):
            on = True
            try_again = False
        elif(continue_val == "N"):
            on = False
            try_again = False
        else:
            print("You have to choose (Y/N). This is case-sensitive.")
            continue_val = input("Do you want to continue (Y/N): ")



