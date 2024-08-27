def encode(numbers):

    """
    numbers : param - input in hexadecimal
    return : char - vlq encoded numbers

    """

    res=[]

    #print(str([0x7F]))

    #in_binary=bin(int(str(numbers[0]), 16))[2:].zfill(len(numbers) * 4)
    print(numbers[0])
    while numbers[0]>0:
        byte = numbers[0] & 0x7F
        numbers[0] >>= 7
        if numbers[0]>0:
            byte |= 0x80
        res.insert(0, byte)
        print(byte)  

    return res

def decode(bytes_):
    """
    bytes_ : param - input in bytes, vlq encoded
    return : char - output in hexadecimal
    """
    res=[]

    return res


print(encode([0x7F]))