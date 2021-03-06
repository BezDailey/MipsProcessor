class Convertor:
    def hexadecimal_to_binary(self, hexadecimal):
        converted_binary = "" 
        decimal_dict = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0,
            "a": 10,
            "b": 11,
            "c": 12,
            "d": 13,
            "e": 14,
            "f": 15
        }
        for element in hexadecimal:
            decimal = decimal_dict.get(element.lower())
            binary = ""
            if decimal == "0":
                converted_binary += "0000"

            while decimal > 0:
                binary += str(decimal % 2)
                decimal /= 2
                decimal = int(decimal)

            binary = binary[::-1]

            if len(binary) == 4:
                converted_binary += binary
                binary = ""
            elif len(binary) < 4:
                zero_count = 4 - len(binary)
                converted_binary += ("0" * zero_count) + binary
                zero_count = 0
                binary = ""
        return converted_binary

    def hexadecimal_to_decimal(self, hexadecimal):
        binary = self.hexadecimal_to_binary(hexadecimal)
        decimal = self.binary_to_decimal(binary)
        return decimal

    def binary_to_decimal(self, binary):
        digit_place = int(len(binary))
        decimal = 0
        for digit in binary:
            temp = int(digit) * (pow(2, digit_place - 1))
            decimal += temp
            digit_place -= 1
        return decimal

    def decimal_to_hexadecimal(self, decimal):
        hexadecimal = ""
        decimal_dict = {
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            0: "0",
            10: "a",
            11: "b",
            12: "c",
            13: "d",
            14: "e",
            15: "f"
        }
        if decimal == 0:
            return "0"
        while decimal > 0:
            hexadecimal += decimal_dict[decimal % 16]
            decimal /= 16
            decimal = int(decimal)
        hexadecimal = hexadecimal[::-1]
        return hexadecimal

    def decimal_to_binary(self, decimal_value):
        binary = ""
        decimal = decimal_value
        if decimal_value < 0:
            decimal = decimal * (-1)
        while decimal > 0:
            binary += str(decimal % 2)
            decimal /= 2
            decimal= int(decimal)
        binary = binary[::-1]
        if(len(binary) < 31):
            padding = 31 - len(binary)
            binary = "0" * padding + binary
        if decimal_value < 0:
            binary = "-" + binary
        return binary

    def decimal_to_binary_twos_complement(self, decimal_value):
        if(decimal_value < 0):
            decimal = decimal_value * (-1)
            binary = ""
            while decimal > 0:
                binary += str(decimal % 2)
                decimal /= 2
                decimal= int(decimal)
            binary = binary[::-1]
            if(len(binary) < 32):
                padding = 32 - len(binary)
                binary = "0" * padding + binary
            binary_list = list(binary)
            for i in range(0, 32):
                if binary_list[i] == "0":
                    binary_list[i] = "1"
                else:
                    binary_list[i] = "0"
            binary = "".join(binary_list)
            binary = bin(int(binary,2) + 1)
            return binary[2:]
        else:
            binary = self.decimal_to_binary(decimal_value)
            binary = "0" + binary
            return binary

    def convert_twos_complement_binary_to_decimal(self,binary):
        if binary[0] == "0":
            return (self.binary_to_decimal(binary))
        if binary[1] == "1":
            binary_list = list(binary)
            for i in range(0, 32):
                if binary_list[i] == "0":
                    binary_list[i] = "1"
                else:
                    binary_list[i] = "0"
            binary = "".join(binary_list)
            decimal = (self.binary_to_decimal(binary) * (-1)) - 1
            return decimal


