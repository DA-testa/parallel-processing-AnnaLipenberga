# python3

def swaping(data, i, res):
    left_child = 1 + (2*i)
    right_child = 2 + (2*i)
    n = len(data)
    
    if left_child >= n:
        return
    x = left_child
    if right_child < n and data[left_child] > data[right_child]:
        x = right_child
        
    if data[i] > data[x]:
        res.append([i, x])
        data[i], data[x] = data[x], data[i]
        swaping(data, x, res)
        
        
def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(int((n-2)/2), -1, -1):
        swaping(data, i, swaps)
        
    return swaps
        

def parallel_processing(n, m, data):
    output = []
    heap = data[:n]
    data_idx = n
    processing_threads = list(range(n))
    
    
    if data_idx < m:
        for i in processing_threads:
            output.append((i, 0))
            heap[i] = data[data_idx]
            data_idx += 1
            
            if data_idx == m:
                break
                
                
        swaps = build_heap(heap)
        for i, j in swaps:
            processing_threads[i], processing_threads[j] = processing_threads[j], processing_threads[i]
            
        for i in range(n):
            if data_idx < m:
                output.append((processing_threads[i], heap[i]))
                heap[i] = data[data_idx]
                data_idx += 1
            else:
                output.append((processing_threads[i], heap[i]))
    
    else:
        for i in range(n):
            output.append((i, data[i]))
    
    return output


def main():
    # create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())
    source = input()
    if "I" in source:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in source:
        source2 = input()
        if "a" in source2:
            return()
        with open ("tests/"+source2, encoding="utf-8") as fails:
            n = int (fails.readline())
            data = list(map(int, fails.readline().split()))
    else:
        return()

    # pass the input data to the function
    result = parallel_processing(n, m, data)
    
    # print out the results, each pair in its own line
    for pair in result:
        print(pair[0], pair[1])


if __name__ == "__main__":
    main()

