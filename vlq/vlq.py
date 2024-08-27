def encode(numbers):

    """
    numbers : param - input in hexadecimal
    return : char - vlq encoded numbers

    """

    res=[]
    for number in numbers:
        hexa=number
        if hexa==0:
            res.append(0)
            continue
        temp=[]
        while hexa>0:
            byte = hexa & 0x7F
            hexa >>= 7
            if len(temp)>0:
                byte |= 0x80
            temp.insert(0, byte)
             
        res+=temp
    return res


def decode(bytes_):
    """
    bytes_ : param - input in bytes, vlq encoded
    return : char - output in hexadecimal
    """
    res=[]
    number=0

    for i in range(len(bytes_)):
        if bytes_[i] & 0x7F == 0 and i == 0 or bytes_[i]== 0xFF and i ==len(bytes_)-1:
            raise ValueError("incomplete sequence")
        number= (number << 7) | (bytes_[i] & 0x7F)
        if bytes_[i] & 0x80 == 0:
            res.append(number)
            number=0

    return res