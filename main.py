# python3
 
    
def parallel_processing(n, m, data):
    output = []
    threads = list(range(n))
    times = [0] * n
    
    for i in range(m):
        # Find the thread that will be available next
        next_thread = min(threads, key=lambda t: times[t])
        output.append([next_thread, times[next_thread]])
        
        # Update the time for the chosen thread
        times[next_thread] += data[i]
        
    return output

def main():
    # read input
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # run parallel processing
    parallel_processing(n, m, data)

if __name__ == "__main__":
    main()
