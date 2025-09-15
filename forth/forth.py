def math_d(strong,stack, user_command):
    match strong:
        case "+":
            one=stack.pop()
            two=stack.pop()
            return two+one
        case "-":
            one=stack.pop()
            two=stack.pop()
            return two-one
        case "*":
            one=stack.pop()
            two=stack.pop()
            return two*one
        case "/":
            one=stack.pop()
            two=stack.pop()
            return two//one
        case "dup":
            one=stack[-1]
            return one
        case "drop":
            x=stack.pop()
        case "swap":
            one=stack.pop()
            two=stack.pop()
            return one, two
        case "over":
            item=stack[-2]
            return item
        case _:
            if strong in user_command:
                stack.extend(user_command[strong])
                return None


            


class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message=message
    
    
class MyZeroDivisionError(Exception):
    def __init__(self, message):
        self.message=message



def evaluate(input_data):
    user_command={}
    if len(input_data)==2:
        user_stack=input_data.pop(0)
        user_stack=user_stack.split(" ")
        user_stack.pop(0)
        user_stack.pop()
        user_command={
            user_stack.pop(0):user_stack
        }

    stack=input_data[0].split(" ")

    for i in range(len(stack)):
        try:
            x=int(stack[i])
            stack[i]=x
        except (AttributeError,ValueError):
            continue
    

    while True:
        string_count=len(list(filter(lambda x: isinstance(x, str), stack)))
        if string_count==0:
            break
        item=stack.pop(0)
        if type(item)==str:
            try:
                item=item.lower()
                result=math_d(item,stack, user_command)

                if result!=None and type(result)==tuple:
                    for number in result:
                        stack.append(number)

                elif result!=None:
                    stack.append(result)
                
            except IndexError:
                raise StackUnderflowError("Insufficient number of items in stack")
            except ZeroDivisionError:
                raise ZeroDivisionError("divide by zero")
        else:
            stack.append(item)
        
        
    return stack




print(evaluate([": dup-twice dup dup ;", "1 dup-twice"]))