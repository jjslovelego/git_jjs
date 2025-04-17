
def read_single_digit(d):
    if '1' in d:
        print('일')
    elif '2' in d:
        print('이')
    elif '3' in d:
        print('삼')
    elif '4' in d:
        print('사')
    elif '5' in d:
        print('오')
    elif '6' in d:
        print('육')
    elif '7' in d:
        print('칠')
    elif '8' in d:
        print('팔')
    elif '9' in d:
        print('구')
    elif '0' in d:
        print('영')
        


def read_number(n):
    
    if n==1:
        read_single_digit(d)
    elif n==2:
        read_single_digit(d), read_single_digit(d)
    elif n==3:
        read_single_digit(d), read_single_digit(d), read_single_digit(d)
        
    
        
    


    

d=input('세 자리 정수 입력: ')
n=len(d)
read_number(n)






    
