from datetime import datetime

n=int(input())
f=[0 for i in range(n+1)]
start=datetime.now()
f[1]=1
f[2]=1
for i in range(3,n+1):
    f[i]=f[i-2]+f[i-1]
elapsed_time=datetime.now()-start
print('Time Elapsed: {}μs, Result: {}'.format(elapsed_time.seconds*1000000+elapsed_time.microseconds,f[n]))