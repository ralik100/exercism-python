def link(dominoes):
    linked={}

    for stone in dominoes:
        matches=[]
        for i in range (0,len(dominoes)):
            if stone[0] in dominoes[i] or stone[1] in dominoes[i]:
                matches.append(dominoes[i])
        linked[stone]=matches

    return linked
    

def can_chain(dominoes):
    links=link(dominoes)
    result=[]
    length=len(dominoes)
    revd=[]

    if length==0:
        return None
    if length==1:
        stone=dominoes[0]
        if stone[0]==stone[1]:
            return stone
        else:
            return None
    
    result.append(dominoes.pop(0))
    
    
    while dominoes:

        stone=result[-1]
        x=dominoes.pop(0)
        if x in links[stone] or x == revd[-1] and tuple(x[1],x[0]) in links[stone]:
            if x[0]==stone[1] :
                result.append(x)
            else:
                dominoes.append(x)
        else:
            dominoes.append(x)

            
        
        if x in links[stone] and len(dominoes)==1:
            x=dominoes.pop(0)
            revd.append(x)
            new_x=(x[1],x[0])
            x=new_x
            dominoes.insert(0,x)
            links[stone].append(x)


        
        if x not in links[stone]:

            return None   

         

    if result[0][0]==result[-1][1]:
        print("asd")
        return result
    else:
        return None


input_dominoes = [(1, 2), (1, 3), (2, 3)]
print(can_chain(input_dominoes))