# python3

def swaping(data, i, res):
    left_child = 1 + (2*i)
    right_child = 2 + (2*i)
    n = len(data)
    
    if left_child >+ n:
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
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
