import random

class Memory:
    def __init__(self, length):
        self.memory_dict = {}
        self.add_random_values(length)

    def add_random_values(self, length):
        for x in range(0, length):
            memory_address = x
            random_value = random.randrange(-5,5,1)
            self.memory_dict[memory_address] = random_value

    def get_memory_value(self, memory_address):
        return self.memory_dict[memory_address]

    def store_memory_value(self, memory_address, decimal_value):
        self.memory_dict[memory_address] = decimal_value
            
    def print_values_in_dict(self):
        print("")
        for key, value in self.memory_dict.items():
            print('memory[', str(key), "] : ", str(value))