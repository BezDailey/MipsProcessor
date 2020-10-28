from convertor import Convertor
from r_format import R_Format
from i_format import I_Format

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

registers = {
    "$0": "A",
    "$1": "A",
    "$2": "A",
    "$3": "A",
    "$4": "ABB",
    "$5": "A",
    "$6": "A",
    "$7": "A",
    "$8": "A"
}

memory = {
    0: "4000",
    1: "0101",
    2: "0102",
    3: "0103",
    4: "0104",
    5: "0105",
    6: "0106",
    7: "0107",
    8: "0108"
}

convertor = Convertor()

on = True
while on:
    #instruction = input("Enter an instruction: ")
    instruction = "00823820"

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
        value = convertor.hexadecimal_to_decimal(registers[left_value]) + convertor.hexadecimal_to_decimal(registers[right_value])
        registers[destination] = convertor.decimal_to_hexadecimal(value)
        print(registers.get(destination))

    if (function == "Sub"):
        destination = "$" + str(r_instruction.rd)
        left_value = "$" + str(r_instruction.rs)
        right_value = "$" + str(r_instruction.rt)
        value = convertor.hexadecimal_to_decimal(registers[left_value]) - convertor.hexadecimal_to_decimal(registers[right_value])
        registers[destination] = convertor.decimal_to_hexadecimal(value)
        print(registers.get(destination))
    if (function == "And"):
        estination = "$" + str(r_instruction.rd)
        left_value = "$" + str(r_instruction.rs)
        right_value = "$" + str(r_instruction.rt)
        left_value_binary = convertor.hexadecimal_to_binary(registers[left_value])
        right_value_binary = convertor.hexadecimal_to_binary(registers[right_value])
        print(left_value_binary)
        print(right_value_binary)

    if (function == "Or"):
        pass
    if (function == "Xor"):
        pass
    if (function == "Addi"):
        pass
    if (function == "Lw"):
        pass
    if (function == "Sw"):
        pass
    if (function == "Beq"):
        pass
    if (function == "Bne"):
        pass

    on = False