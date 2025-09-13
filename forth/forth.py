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
        case "dup":
            pass


class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message=message
    
    
class MyZeroDivisionError(Exception):
    def __init__(self, message):
        self.message=message



def evaluate(input_data):
    stack=input_data[0].split(" ")

    for i in range(len(stack)):
        try:
            x=int(stack[i])
            stack[i]=x
        except (AttributeError,ValueError):
            continue

    for i in range(len(stack)):

        item=stack.pop(0)
        if type(item)==str:
            try:
                number_one=stack.pop(-1)
                number_two=stack.pop(-1)
                stack.append(math_d(item,number_one,number_two))
            except IndexError:
                raise StackUnderflowError("Insufficient number of items in stack")
            except ZeroDivisionError:
                raise ZeroDivisionError("divide by zero")
        else:
            stack.append(item)
    return stack




print(evaluate(["4 0 /"]))