def math_d(strong, numb_one, numb_two):
    match strong:
        case "+":
            return numb_two+numb_one
        case "-":
            return numb_two-numb_one
        case "*":
            return numb_two*numb_one
        case "/":
            return numb_two//numb_one

class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message=message
    
    
    



def evaluate(input_data):
    stack=input_data[0].split(" ")

    for i in range(len(stack)):
        try:
            x=int(stack[i])
        except AttributeError:
            pass
        except ValueError:
            continue
        if x:
            stack[i]=x

    
    while stack:
        item=stack.pop()
        if type(item)==str:
            try:
                number_one=stack.pop()
                number_two=stack.pop()
                stack.append(math_d(item,number_one,number_two))
            except IndexError:
                raise StackUnderflowError("Insufficient number of items in stack")
        else:
            stack.append(item)
            break

    return stack

#necessary to change logic to pass all tests, stack must be done from beginning of list on from back

print(evaluate(["1 2 +"]))