def collatz(number):
    try:
        if number % 2 == 0:
            print(number/2)
            return number/2
            
        if number % 2 == 1:
            print(3*number+1)
            return 3*number+1
    except:
        print('error')

def start():            
    print('please enter an integer')
    num = int(input())

    while num != 1:
        num = round(collatz(num))
    else:
        print('donners')
        num == 0
        start()

start()

    


        
