import time

def time_execution(code):
    # start the clock
    start = time.clock()
    # evaluate any string as if it is a Python command
    result = eval(code)
    # find difference in start and end time
    run_time = time.clock() - start
    # return the result of the code and time taken
    return result, run_time

time_execution("2+2")

def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1

spin_loop(10**6)
spin_loop(10**7)

time_execution("spin_loop(10**6)") # 0.08s
time_execution("spin_loop(10**7)") # 0.8s
time_execution("spin_loop(10**8)") # 8s

def hanoi_(n, src, aux, dest):
    if n == 0:
        return
    hanoi_(n-1, src, dest, aux)
    # print src, '->', dest # we only want to time it, not print the answers
    hanoi_(n-1, aux, src, dest)

hanoi_(4, 'A', 'B', 'C')

time_execution("hanoi_(4, 'A', 'B', 'C')")
time_execution("hanoi_(20, 'A', 'B', 'C')") # 0.43s
time_execution("hanoi_(21, 'A', 'B', 'C')") # 0.86s
time_execution("hanoi_(22, 'A', 'B', 'C')") # 1.71s
time_execution("hanoi_(23, 'A', 'B', 'C')") # 3.43s
