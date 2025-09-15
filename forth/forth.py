def math_d(strong,stack, user_command):
    match strong:
        case "+":
            if strong not in user_command:
                one=stack.pop()
                two=stack.pop()
                return two+one
            else:
                for item in user_command[strong]:
                    try:
                        stack.append(int(item))
                    except:
                        stack.append(item)
        
        case "-":
            if strong not in user_command:
                one=stack.pop()
                two=stack.pop()
                return two-one
            else:
                for item in user_command[strong]:
                    try:
                        stack.append(int(item))
                    except:
                        stack.append(item)
        
        case "*":
            if strong not in user_command:
                one=stack.pop()
                two=stack.pop()
                return two*one
            else:
                for item in user_command[strong]:
                    try:
                        stack.append(int(item))
                    except:
                        stack.append(item)
        
        case "/":
            if strong not in user_command:
                one=stack.pop()
                two=stack.pop()
                return two//one
            else:
                for item in user_command[strong]:
                    try:
                        stack.append(int(item))
                    except:
                        stack.append(item)
        
        case "dup":
            if strong not in user_command:
                one=stack[-1]
                return one
            else:
                for item in user_command[strong]:
                    try:
                        stack.append(int(item))
                    except:
                        stack.append(item)

        case "drop":
            if strong not in user_command:
                x=stack.pop()
            else:
                for item in user_command[strong]:
                    try:
                        stack.append(int(item))
                    except:
                        stack.append(item)

        case "swap":
            if strong not in user_command:
                one=stack.pop()
                two=stack.pop()
                return one, two
            else:
                for item in user_command[strong]:
                    try:
                        stack.append(int(item))
                    except:
                        stack.append(item)

        case "over":
            if strong not in user_command:
                item=stack[-2]
                return item
            else:
                for item in user_command[strong]:
                    try:
                        stack.append(int(item))
                    except:
                        stack.append(item)

        case _:
            if strong.isdigit():
                raise ValueError("undefined operation")
            if strong in user_command:
                for item in user_command[strong]:
                    try:
                        stack.append(int(item))
                    except:
                        stack.append(item)
                return None
            elif strong not in user_command:
                raise ValueError("undefined operation")


            


class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message=message
    
    
class MyZeroDivisionError(Exception):
    def __init__(self, message):
        self.message=message



def evaluate(input_data):

    if len(input_data)==1 and input_data[0][0]==":":
        raise ValueError("illegal operation")

    user_command={}
    if len(input_data)!=1:
        while len(input_data)>1:
            user_stack=input_data.pop(0)
            user_stack=user_stack.split(" ")
            user_stack.pop(0)
            user_stack.pop()
            command=user_stack.pop(0)
            command=command.lower()
            if command not in user_command:
                user_command[command]=[]
            elif command in user_command:
                copy=user_command[command]
                user_command[command]=[]
            for item in user_stack:
                item=item.lower()
                try:
                    item=int(item)
                except:
                    pass
                
                if item not in user_command:
                    user_command[command].append(item)
                elif item == command:
                    user_command[command].extend(copy)
                else:
                    user_command[command].extend(user_command[item])

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




print(evaluate([": SWAP DUP Dup dup ;", "1 swap"]))