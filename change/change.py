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
            if coin==target:
                res.append(coin)
                return res
            if coin < target:
                coin_list.append(coin)

    print(coin_list)
    
    temp=target
    while True:
        print(coin_list)
        print(temp)
        for coin in coin_list:           
            if temp%coin==0 and coin!=1:
                print("asd")
                for i in range(temp//coin):
                    res.append(coin)
                    temp=temp-coin
                break
        if temp==0:
             break
        temp=temp-coin_list[-1]
        res.append(coin_list[-1])
        if coin_list[-1]>temp:
             coin_list.pop(-1)
    
    return res

print(find_fewest_coins([1, 5, 10, 25, 100], 15))