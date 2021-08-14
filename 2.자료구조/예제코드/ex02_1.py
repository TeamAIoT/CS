import timeit

start_time=timeit.default_timer()

sum=0

for i in range(100000000):
    sum+=i

terminate_time=timeit.default_timer()

print("수행시간:{}".format(terminate_time-start_time))