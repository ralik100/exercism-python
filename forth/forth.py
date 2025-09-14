def math_d(strong,stack):
    match strong:
        case "+":
            one=stack.pop(-1)
            two=stack.pop(-1)
            return two+one
        case "-":
            one=stack.pop(-1)
            two=stack.pop(-1)
            return two-one
        case "*":
            one=stack.pop(-1)
            two=stack.pop(-1)
            return two*one
        case "/":
            one=stack.pop(-1)
            two=stack.pop(-1)
            return two//one
        case "dup":
            one=stack[-1]
            return one
        case "drop":
            x=stack.pop()

            


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
                item=item.lower()
                result=math_d(item,stack)
                if result!=None:
                    stack.append(result)
            except IndexError:
                raise StackUnderflowError("Insufficient number of items in stack")
            except ZeroDivisionError:
                raise ZeroDivisionError("divide by zero")
        else:
            stack.append(item)
    return stack




print(evaluate(["1 drop"]))