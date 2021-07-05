from datetime import datetime

count=-1
def fibonacci(n):
    global count
    count+=1
    if n==1 or n==2:
        return 1
    elif f[n]!=-1:
        return f[n]
    else:
        f[n]=fibonacci(n-2)+fibonacci(n-1)
        return f[n]

n=int(input())
f=[-1 for i in range(n+1)]
start=datetime.now()
result=fibonacci(n)
elapsed_time=datetime.now()-start
print('Time Elapsed: {}μs, Result: {}'.format(elapsed_time.seconds*1000000+elapsed_time.microseconds,result))
print(count)