from datetime import datetime

def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input())
start=datetime.now()
result=fibonacci(n)
elapsed_time=datetime.now()-start
print('Time Elapsed: {}μs, Result: {}'.format(elapsed_time.seconds*1000000+elapsed_time.microseconds,result))