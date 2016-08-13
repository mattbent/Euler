fibSeq = []
def fib(n):
    if(n <= 0):
        fibSeq.insert(0,0)
        return 0
    elif(n == 1):
        fibSeq.insert(1,1)
        return 1
    else:
        fibNum = fib(n-1) + fib(n-2)
        fibSeq.insert(n, fibNum)
        return fibNum 

def filfib():
    i = 0
    fibtrack = 0
    while(fibtrack < 4000000):
        fibtrack = fib(i)
        i = i + 1
def evenSum():
    count = 0
    for index in fibSeq:
        if(index%2 == 0):
            count += index
    print(count)

filfib()        
evenSum()
