def get_fixed_price():
    rate=int(input('할인율은?'))
    Aprice=int(input('A상품의 할인된 가격은?'))
    Bprice=int(input('B상품의 할인된 가격은?'))
    print('A상품의 정가는',Aprice*(100)/(100-rate),'원')
    print('B상품의 정가는',Bprice*(100)/(100-rate),'원')


get_fixed_price()

    
    
            
    
