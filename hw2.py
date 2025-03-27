def exchange(coin):
    c=coin
    c500=c//500
    c%=500
    c100=c//100
    c%=100
    c50=c//50
    c%=50
    c10=c//10
    print('500원 동전의 개수:',c500)
    print('100원 동전의 개수:',c100)
    print('50원 동전의 개수:',c50)
    print('10원 동전의 개수:',c10)
    

def get_integer(prompt):
    res=int(input(prompt))
    return res;

coin=get_integer('동전으로 교환하고자 하는 금액은?')
exchange(coin)
    
