from convertor import Convertor

class R_Format:
    def __init__(self, binary):
        self.binary = binary
        self.op = ''
        self.rs = ''
        self.rt = ''
        self.rd = ''
        self.shamt = ''
        self.funct = ''
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
            elif i < 22:
                self.rd += bit
            elif i < 27:
                self.shamt += bit
            elif i < 33:
                self.funct += bit

    def convert_fields(self):
        converter = Convertor()
        self.op = converter.binary_to_decimal(self.op)
        self.rs = converter.binary_to_decimal(self.rs)
        self.rt = converter.binary_to_decimal(self.rt)
        self.rd = converter.binary_to_decimal(self.rd)
        self.shamt = converter.binary_to_decimal(self.shamt)
        self.funct = converter.binary_to_decimal(self.funct)