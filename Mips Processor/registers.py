import random

class Registers:
    def __init__(self):
        self.registers_dict = {}
        self.add_random_values()

    def add_random_values(self):
        for x in range(0, 32):
            address = "$" + str(x)
            random_value = random.randrange(-5,5,1)
            self.registers_dict[address] = random_value

    def get_register_value(self, register_address):
        return self.registers_dict[register_address]

    def store_register_value(self, register_address, decimal_value):
        self.registers_dict[register_address] = decimal_value
            
    def print_values_in_dict(self):
        print("")
        for key, value in self.registers_dict.items():
            print('register[', key, "] : ", str(value))