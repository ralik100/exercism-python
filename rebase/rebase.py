def to_decimal(input_base,digits):
    total=0
    for i in range(len(digits)):
        total+=digits[i]*(pow(input_base,len(digits)-i-1))

    temp=list(str(total))
    final=list(map(int,temp))
    return final

def decimal_swap(decimaled, output_base):
    temp=[]
    final=[]
    while decimaled!=0:
        temp.append(decimaled%output_base)
        decimaled=decimaled//output_base
    temp.reverse()

    return temp
    
def rebase(input_base, digits, output_base):


    if input_base<2:
        raise ValueError("input base must be >= 2")
    if output_base<2:
        raise ValueError("output base must be >= 2")

    for digit in digits:
        if not 0<=digit<input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    decimaled=digits
    if input_base!=10:
        decimaled=to_decimal(input_base,digits)
    
    if output_base==10:
        final=decimaled
    
    else:
        temp=''
        
        for digit in decimaled:
            temp+=str(digit)
        

        if decimaled.count(0)==len(decimaled):
            
            return [0]
        
        final=decimal_swap(int(temp),output_base)

    return final