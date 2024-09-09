def find_fewest_coins(coins, target):
    """
    params:
    coins - list : value of possible change coins
    target - int : value of change

    result - list : minimum possible list containing coins needed to give change
    """
    res=[]


    coin_list=[]
    for coin in coins:
            if coin <= target:
                coin_list.insert(0,coin)

    if len(coin_list)==1:
          res.append(coin_list[0])
          return res
    
    temp=target
    while temp!=0:
          if temp%coin_list[-1]==0:
                for i in range(temp//coin_list[-1]):
                      res.append(coin_list[-1])
                break
          if temp%coin_list[-1]!=0:
                temp=temp-coin_list[-1]
                res.append(coin_list[-1]) 
                coin_list.pop(-1)
                

    
    return res

print(find_fewest_coins([1, 5, 10, 25], 1))