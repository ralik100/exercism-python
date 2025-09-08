def link(dominoes):
    linked={}

    for stone in dominoes:
        matches=[]
        for i in range (0,len(dominoes)):
            if stone[0] in dominoes[i] or stone[1] in dominoes[i]:
                matches.append(dominoes[i])
        linked[stone]=matches

    return linked

def make_chain(stone, linked):
    result=[]
    matches=linked[stone]
    for i in range(len(matches)):
        

def can_chain(dominoes):
    result=[]
    links=link(dominoes)
    
            

    return result


input_dominoes = [(1, 2), (4, 1), (2, 3)]
print(can_chain(input_dominoes))