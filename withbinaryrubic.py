from binaryconvert import convert

def toDecimal(n):
        return int(n,2)

def toBinary(text, bit):
        binary_list = []
        for char in text:
            binary_char = format(ord(char), f'0{bit}b')
            binary_list.append(binary_char)
        return ' '.join(binary_list)

print("SirVon Andre Thomas")
print("S =" ,toBinary("S",8),"=",toDecimal(convert.ToBinary("S",8)))
print("i =" ,toBinary("i",8),"=",toDecimal(convert.ToBinary("i",8)))
print("r =" ,toBinary("r",8),"=",toDecimal(convert.ToBinary("r",8)))
print("V =" ,toBinary("V",8),"=",toDecimal(convert.ToBinary("V",8)))
print("o =" ,toBinary("o",8),"=",toDecimal(convert.ToBinary("o",8)))
print("n =" ,toBinary("n",8),"=",toDecimal(convert.ToBinary("n",8)))
print("A =" ,toBinary("A",8),"=",toDecimal(convert.ToBinary("A",8)))
print("T =" ,toBinary("T",8),"=",toDecimal(convert.ToBinary("T",8)))
print("h =" ,toBinary("h",8),"=",toDecimal(convert.ToBinary("h",8)))
print("o =" ,toBinary("o",8),"=",toDecimal(convert.ToBinary("o",8)))
print("m =" ,toBinary("m",8),"=",toDecimal(convert.ToBinary("m",8)))
print("a =" ,toBinary("a",8),"=",toDecimal(convert.ToBinary("a",8)))
print("s =" ,toBinary("s",8),"=",toDecimal(convert.ToBinary("s",8)))
print("I like to code, travel and spend time with Family")
print("I expect to understand the Python Language more from this class.")
