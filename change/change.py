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

    for i in range(coin_list):
        
        temp=target

        while temp!=0:
             

    
    return res