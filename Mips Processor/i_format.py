from convertor import Convertor

class I_Format:
    def __init__(self, binary):
        self.binary = binary
        self.op = ''
        self.rs = ''
        self.rt = ''
        self.address = ""
        self.get_fields()
        self.convert_fields()

    def get_fields(self):
        i = 0
        for bit in self.binary:
            i += 1
            if i < 7:
                self.op += bit
            elif i < 12:
                self.rs += bit
            elif i < 17:
                self.rt += bit
            else:
                self.address += bit
    
    def convert_fields(self):
        converter = Convertor()
        self.op = converter.binary_to_decimal(self.op)
        self.rs = converter.binary_to_decimal(self.rs)
        self.rt = converter.binary_to_decimal(self.rt)
        self.address = converter.binary_to_decimal(self.address)
