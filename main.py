# python3
 
    
  import heapq

def parallel_processing(n, m, data):
    output = []
    for i in range(n):
        heapq.heappush(output, (0, i))
    for i in range(m):
        f, s = heapq.heappop(output)
        output.append((f + data[i], s))
        print(s, f)
    return output

def main():
    # read input
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # run parallel processing
    parallel_processing(n, m, data)

if __name__ == "__main__":
    main()
