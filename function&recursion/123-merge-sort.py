def hanoi(n,start,end,middle):
    if n==1:
        print(f"moved {n} disk from {start} to {end}")
    else:
        hanoi(n-1,start,middle,end)
        print(f"moved {n} disk from {start} to {end}")
        hanoi(n-1,middle,end,start)
import time
start = time.time()
hanoi(4,"A","B","C")
end = time.time()-start
print(end)