fruit = {}
print('[구입]')
while True:
    g=input('상품명?')
    if g == '':
        break
    n=input('수량은?')
    fruit[g]=n
    print(f'장바구니에 {g} {n} 개가 담겼습니다.\n')
    

print(f'\n>>> 장바구니 보기:{fruit}\n')
print('[검색]')
f=input('장바구니에서 확인하고자 하는 상품은?')
print(f,'은(는)', fruit.get(f),'개 담겨있습니다.')

