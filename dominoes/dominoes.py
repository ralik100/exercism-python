def link(dominoes):
    linked={}

    for stone in dominoes:
        matches=[]
        for i in range (0,len(dominoes)):
            if stone[0] in dominoes[i] or stone[1] in dominoes[i]:
                matches.append(dominoes[i])
        linked[stone]=matches

    return linked
    
def reverse_stone(stone,links):
    new_stone=(stone[1],stone[0])
    for key in links:
        if stone in links[key]:
            links[key].remove(stone)
            links[key].append(new_stone)
    return new_stone

def can_chain(dominoes):
    
    result=[]
    length=len(dominoes)


    if length==0:
        return []
    if length==1:
        stone=dominoes[0]
        if stone[0]==stone[1]:
            return stone
        else:
            return None
    links=link(dominoes)
    result.append(dominoes.pop(0))
    
    
    while dominoes:

        stone=result[-1]
        x=dominoes.pop(0)
        if x in links[stone]:
            if x[0]==stone[1]:
                result.append(x)
            else:
                dominoes.append(x)
        else:
            dominoes.append(x)

        if x in links[stone] and x[0]!=stone[1]:
            x=reverse_stone(x,links)   
            dominoes.pop()
            dominoes.append(x)

             
        if x not in links[stone]:
            return None   

         

    if result[0][0]==result[-1][1]:
        return result
    else:
        return None


input_dominoes = [(1, 2), (3, 1), (2, 3)]
print(can_chain(input_dominoes))